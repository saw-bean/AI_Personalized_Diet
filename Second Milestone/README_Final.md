# NutriAI - AI-Enhanced Personal Nutrition & Activity Assistant

**Course:** AIE1014 - AI Applied Project  
**Program:** Cambrian College - AIGC Program  
**Team (JAMS):** Aashish Giri, Jaykesh J Awal, Meet Patel, Sabin Khatri

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📖 Project Overview

NutriAI is a prototype of a smart personal assistant designed to provide personalized nutrition and activity recommendations. The system addresses the challenge that generic health advice often fails, by leveraging AI to offer guidance tailored to an individual's specific goals and daily context.

The project demonstrates an end-to-end data science workflow, from data sourcing and synthetic data generation to model training, evaluation, and deployment in an interactive web application.

### Core Features
*   **Persona-Based Personalization:** Users select a persona (e.g., 'Weight Loss Focus', 'Muscle Gain Focus') to set their unique daily nutritional targets.
*   **Daily Logging:** Simple interface to log daily food intake and physical activities.
*   **Real-Time Calculations:** Instantly calculates total calories, macronutrients, and estimated calorie expenditure.
*   **AI-Powered Prediction:** A trained Random Forest model predicts the likelihood of the user meeting their primary nutritional goal (e.g., protein target) for the day.
*   **Intelligent Recommendations:** A rule-based engine, informed by the AI's prediction and the user's daily data, provides simple, actionable "nudges" to help them stay on track.

## 🛠️ Technical Architecture

The project utilizes a hybrid architecture that separates the intensive AI development from the lightweight user interface.

*   **Backend Development (AI & Data):** All data processing, synthetic data generation, and model training were performed in **Google Colaboratory** notebooks. This allowed for a collaborative environment with powerful compute resources. The final trained model and data scaler were saved as `.pkl` files.
*   **Frontend (User Interface):** The interactive user-facing application is built with **Streamlit**. It runs locally and loads the pre-trained model to provide real-time predictions and recommendations.

## 🚀 Getting Started

Follow these instructions to set up the environment and run the NutriAI Streamlit application on your local machine.

### Prerequisites

*   Python (version 3.9+)
*   Conda package manager (Miniconda or Anaconda)

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/NutriAi.git
    cd NutriAi
    ```

2.  **Create and activate the Conda environment:**
    The project requires specific packages. We recommend using Conda to manage the environment to avoid dependency conflicts.
    ```bash
    # Create the conda environment named 'nutriai' with Python 3.11
    conda create --name nutriai python=3.11 -y

    # Activate the environment
    conda activate nutriai
    ```

3.  **Install dependencies:**
    This project has a dependency (`pyarrow`) that is best installed via Conda first, followed by the rest via pip.
    ```bash
    # Install pyarrow with conda
    conda install pyarrow -y

    # Install the remaining packages with pip
    pip install pandas numpy scikit-learn matplotlib seaborn streamlit
    ```

### Running the Application

1.  **Ensure you are in the project's root directory** and that your `nutriai` conda environment is active.

2.  **Place the required files** in the root directory. You must have:
    *   `app.py`
    *   `nutriai_rf_model.pkl` (the trained model)
    *   `scaler.pkl` (the data scaler)
    *   `curated_food_dataset.csv` (the food database)

3.  **Run the Streamlit application** from your terminal:
    ```bash
    streamlit run app.py
    ```

4.  The application should automatically open in a new tab in your web browser at `http://localhost:8501`.

## 📂 Repository Structure
NutriAi/
├── app.py # The main Streamlit application script
├── Milestone2-JAMS - Colab.ipynb # The Colab notebook for data generation and model training
├── nutriai_rf_model.pkl # Saved Random Forest model artifact
├── scaler.pkl # Saved StandardScaler artifact
├── curated_food_dataset.csv # The curated and de-duplicated food database
└── README.md # This file
code
Code
## 🧠 The AI Model

*   **Model:** `RandomForestClassifier` from Scikit-learn.
*   **Task:** Binary classification to predict if a user will meet their daily protein target (`protein_target_met`).
*   **Key Features:** `total_calories_kcal`, `total_fat_g`, `total_carbs_g`, `calories_expended`, and persona-related features.
*   **Performance:** The model achieved **~81% accuracy** and a **0.72 F1-score** on the test set, demonstrating a strong ability to learn from the generated user data.

## 🤝 Team Contributions

*   **Aashish Giri:** Led the design of user personas and the logic for the rule-based recommendation engine.
*   **Jaykesh J Awal:** Managed data visualization, EDA, and the overall structure and documentation of the Colab notebook.
*   **Meet Patel:** Focused on the development, training, and evaluation of the Random Forest machine learning model.
*   **Sabin Khatri:** Handled the data curation and preprocessing pipeline, preparing the foundational dataset for the project.