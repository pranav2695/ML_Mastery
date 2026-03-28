# 01. Linear Regression (Statistical Fundamentals)

> **Status:**  | **Interview Readiness:**

This module covers the theoretical foundations, implementation from scratch, and a product-based case study for Linear Regression.

---

## 🧠 1. Core Theory (The "Interview" Check)

### Mathematical Formulation
The objective is to find the best-fitting line by minimizing the **Mean Squared Error (MSE)** loss function:
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$$

### Key Interview Questions
* **Assumptions:** Linearity, Homoscedasticity, Independence of errors, Normality of residuals.
* **Optimization:** How does **Gradient Descent** update the weights? $\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)$.
* **Regularization:** Difference between **L1 (Lasso)** for feature selection and **L2 (Ridge)** for preventing overfitting.
* **Metrics:** R-squared vs. Adjusted R-squared (Why use Adjusted for multiple features?).

---

## 💻 2. Implementation Logic
* **[scratch_implementation.py](./src/scratch.py):** Simple Gradient Descent using pure NumPy.
* **[scikit_workflow.ipynb](./notebooks/workflow.ipynb):** Professional pipeline using `StandardScaler` and `Pipeline`.

---

## 🚀 3. Product Case Study: "Expedia Booking Valuation"
**Problem Statement:** Predict the "Booking Value" of a hotel room in Gurgaon based on historical user behavior and seasonal features.

* **Impact:** Helped identify under-priced rooms, potentially increasing revenue by 4%.
* **Technical Highlight:** Handled high-cardinality categorical variables (City/Region) using Target Encoding.
* **Full Project Link:** [Link to Project Folder]

---

## 📂 4. Archives & Reference Links
* [Elements of Statistical Learning (Chapter 3)](https://web.stanford.edu/~hastie/ElemStatLearn/) - The "Bible" for this algo.
* [Medium: Why my OLS model failed?](link-to-your-saved-article) - Common pitfalls in production.
* **Self-Note (2026):** Remember that for 30L+ roles, they always ask about "Feature Multi-collinearity" (VIF > 5 is a red flag).

---

## 🛠️ Requirements & Reproducibility
```bash
# To run the code in this folder:
pip install -r requirements.txt
python src/main.py