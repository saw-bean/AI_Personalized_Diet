# AI_Personalized_Diet
# Food Nutrition Analysis Project
# Overview
This project analyzes daily food nutrition data to provide simple, actionable insights into dietary habits. It focuses on calculating basic nutritional statistics such as calories, protein, carbohydrates, fat, fiber, and water intake from a dataset of food consumption records. The goal is to deliver clear, practical recommendations without relying on complex models or data structures, making the analysis accessible and easy to understand.
# Features
* Calculates average nutritional values per meal and per food category.
* Provides basic statistical summaries (mean, counts).
* Generates simple visualizations for nutritional patterns.
* Offers practical dietary recommendations based on analysis.
* Easy-to-understand code suitable for manual verification and modification.
# Dataset
* Contains 10,000 daily food records from 1,000 users.
* Covers 35 food items across 7 categories: Fruits, Vegetables, Meat, Grains, Dairy, Beverages, and Snacks.
* Includes key nutritional attributes: Calories (kcal), Protein (g), Carbohydrates (g), Fat (g), Fiber (g), Water Intake (ml).

# Tools and Technologies Used
* Google Colab: For collaborative coding, data analysis, and model development.
* Python: Core programming language for all data processing, modeling, and logic.
* scikit-learn: Used for machine learning model development (Random Forest, Logistic Regression), preprocessing, and evaluation.
* SMOTE (Synthetic Minority Oversampling Technique): Applied to balance the dataset and address class imbalance in the target variable.
* Streamlit: For building an interactive user interface and deploying the recommendation system.
* Pandas & NumPy: For data manipulation and numerical operations.
* Seaborn & Matplotlib: For data visualization, including charts and graphs.
* Google Drive: For storing and sharing datasets and model artifacts

# Ethical Considerations and Disclaimers
## Data Privacy:
* Only public datasets were used; no personal or real health data was collected.
* All user logs and profiles are fully synthetic, created with Python scripts.
## Bias Mitigation:
* Eight diverse user personas were designed to represent different ages, genders, professions, and health goals, reducing bias and promoting inclusivity.
## Medical Disclaimer:
* NutriAI is intended for academic and educational purposes only.
* It is not a substitute for professional medical advice, diagnosis, or treatment.
* All recommendations are general and advisory, not medical prescriptions.
## Safe and Transparent Suggestions:
* The rule engine provides only safe, everyday tips (e.g., increase water intake, choose healthier snacks).
* No extreme diets or unsafe advice are given.
* All code and logic are openly shared, with clear explanations for model predictions and rule-based outputs.
## Open Source and Transparency:
* The complete codebase and documentation are shared on Google Colab and GitHub, ensuring transparency and enabling review by others

# Link to Dataset
* https://drive.google.com/file/d/1vlLWTOZbd3He7rTTX9ZPFgSfqjUx4J_l/view?usp=sharing

# Team Member & Main Responsibilities
* Meet Patel - Developed and tuned the Random Forest machine learning model, managed training/evaluation, handled SMOTE.
* Aashish Giri - Built and refined user personas, drafted rule-based health suggestions, organized documentation, reviewed outputs for clarity and user-friendliness.
* Sabin Khatri - Led data preprocessing: cleaning, normalization, handling missing values, and preparing the dataset for training.
* Jaykesh J Awal - Designed and implemented data visualizations, structured the notebook, ensured clear presentation of outputs (charts, tables).
