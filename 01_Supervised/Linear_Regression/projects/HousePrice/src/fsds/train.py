import os

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer

from fsds.ingestion import fetch_housing_data, load_housing_data


def prepare_data(data):
    data["income_cat"] = pd.cut(
        data["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_idx, test_idx in split.split(data, data["income_cat"]):
        strat_train_set = data.loc[train_idx].drop("income_cat", axis=1)
        strat_test_set = data.loc[test_idx].drop("income_cat", axis=1)

    return strat_train_set, strat_test_set


def create_pipeline(num_features, cat_features):
    num_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("std_scaler", StandardScaler()),
        ]
    )

    full_pipeline = ColumnTransformer(
        [
            ("num", num_pipeline, num_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features),
        ]
    )

    return full_pipeline


class MLpipeline(BaseEstimator, TransformerMixin):
    """
    BaseEstimator: it is uses to give free method like 
    get_params(), set_params()
    TransformerMixin: this add fit_tranform() method 
    automatically.
    """
    def __init__(self, add_bedrooms_per_household=True,
                 add_total_rooms_per_household=True,
                 population_per_household=True):
        self.add_bedrooms_per_household = add_bedrooms_per_household
        self.add_total_rooms_per_household = add_total_rooms_per_household
        self.population_per_household = population_per_household 

    def fit(self, X ,y=None):
        return self

    def transform(self, X):
        # We start with the original data
        res_X = X    
        # Condition 1: Add Rooms per Household
        if self.add_total_rooms_per_household:
            rooms_per_household = X[:, 3] / X[:, 6]
            # Index 3=total rooms, 6=households
            res_X = np.c_[res_X, rooms_per_household]      
        # Condition 2: Add Bedrooms per Room
        if self.add_bedrooms_per_household:
            bedrooms_per_room = X[:, 4] / X[:, 6]
            # Index 4=total bedrooms, 6 = households
            res_X = np.c_[res_X, bedrooms_per_room]
        if self.population_per_household:
            pop_per_household = X[:, 5] / X[:, 6] 
            # Index 4=total bedrooms, 6 = households
            res_X = np.c_[res_X, pop_per_household]  
        return res_X


def create_preprocessor_pipeline(num_features, cat_features):
    num_transformer = Pipeline([('imputer', SimpleImputer(strategy="median")),
                                ('attribs_adder', MLpipeline(
                                    add_bedrooms_per_household=True,
                                    add_total_rooms_per_household=True)),
                                    ('std_scaler', StandardScaler()),])
    # Creating the categorical pipeline
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(transformers=[
        ('num', num_transformer, num_features),
        ('cat', categorical_transformer, cat_features)
    ], remainder='drop')
    return preprocessor


def train_and_save_model(
    model_path="models/best_model.pkl", input_data_path="./datasets/housing"
):
    fetch_housing_data()
    housing = load_housing_data(input_data_path)
    train_set, _ = prepare_data(housing)

    housing_labels = train_set["median_house_value"].copy()
    housing_features = train_set.drop("median_house_value", axis=1)
    num_attribs = housing_features.drop("ocean_proximity", axis=1).columns\
        .tolist()
    cat_attribs = ["ocean_proximity"]

    pipeline = create_preprocessor_pipeline(num_attribs, cat_attribs)
    full_pipeline = Pipeline([("prep", pipeline), ("regressor", LinearRegression())])
    housing_prepared = pipeline.fit_transform(housing_features)

    param_grid = [{
        # SEARCH SPACE 1: Linear Models (Ridge) and (Lasso)
        'regressor': [Ridge(), Lasso()],
        'regressor__alpha': [1, 10, 100],
        # Check if custom features help Linear models
        'prep__num__attribs_adder__add_bedrooms_per_household': [True, False],
    }, {
        # SEARCH SPACE 2: Ensemble Models (Random Forest)
        'regressor': [RandomForestRegressor(random_state=42)],
        'regressor__n_estimators': [50, 100],
        'regressor__max_features': [4, 6],
        # Random Forest often handles raw data better; check if features are needed
        'prep__num__attribs_adder__add_bedrooms_per_household': [True, False],
    }]
    grid_search = GridSearchCV(
        full_pipeline, param_grid, cv=3, scoring="neg_mean_squared_error"
    )
    grid_search.fit(housing_prepared, housing_labels)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump((grid_search.best_estimator_, pipeline), model_path)
    print(f"Model saved to {model_path}")
    return grid_search.best_params_, grid_search.best_estimator_
