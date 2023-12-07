# 📖 Purchase Card Transactions

In this [dataset](https://www.cityobservatory.birmingham.gov.uk/@birmingham-city-council/purchase-card-transactions/) you have a collection of purchase card transactions for the Birmingham City Council. This is a historical dataset, you’re able to perform any of the following tasks:

- 1.  (Clustering) Discovering profiles (whether the case) or unusual transactions (anomalies detection) ...
- 2.  (Forecasting) Try to guess future transactional behaviors. For instance, what would be the next purchase? Expenditures forecasting? ...
- 3.  (Creativity) State a problem.

It’s up to you defining the time window in which your analysis will take place

# Notebooks

1_data_etl_eda.ipynb - Data loading and EDA

2_data_preprocessing.ipynb  - Data cleaning and trasnformation

3_model_trainig.ipynb (unsupervised approach) - Kmeans Model.

4_model_evaluation.ipynb (Selected Model) - Eval Model.


# Project Organization
------------

    ├── README.md          <- README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained models, model predictions, or model summaries
    │   ├── predict_model.py
    │   └── train_model.py
    │
    ├── notebooks          <- Jupyter notebooks.
    |   |── data_etl_eda    
    │   ├── data_preprocessing      
    │   └── model_training            
    │   └── model_evaluation            
    │
    ├── references         <- Data dictionaries, papers, research.
    │
    ├── requirements.txt   <- For reproducing-generated with `pip freeze > requirements.txt`
   

--------
