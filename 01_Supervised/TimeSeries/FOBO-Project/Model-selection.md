## Model selection 
- This is the beautiful concept we can add the models as much as we want in the MLops pipeline and it will generate the forecast but it will not be selected as the best model untill it will beat all the other existing models by having the highest score for that particular series 
## Current parameters 
difference_close = 50 
difference_far = 50 
importanct_exec = [4,2]
ranking_penality_modifier = 10
consistency = 0
default_model_flag()
   │
   ├─ PHASE 0: Prepare + union actuals & forecasts, merge, drop null actuals
   │
   ├─ PHASE 1 (per execution):
   │     acc_calc()    → WMean_acc  (in-execution weighted accuracy)
   │     weight_calc() → Weights    (# periods available)
   │
   ├─ PHASE 2: filter FORECAST_YEAR >= 2022
   │
   ├─ PHASE 3 (per model):
   │     weighted_avg()                 → WAvg   (reference only)
   │     weighted_score()               → WScore (U-shaped time weights + period penalties)
   │     min_accuracy_ranking_penalty() → min_acc (worst execution)
   │
   ├─ PHASE 4 (per series):
   │     ranking_penalty() → MODEL_ID (best after consistency penalty)
   │
   └─ PHASE 5: flag DEFAULT_MODEL, dedupe per CNTRY/SUBBRAND, return