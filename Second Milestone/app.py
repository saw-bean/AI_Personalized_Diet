# ==============================================================================
# AIE1014 - AI Applied Project: Final Milestone
# NutriAI - Streamlit Application (Final Version)
# Team: Meet Patel, Aashish Giri, Sabin Khatri, Jaykesh J Awal
# ==============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- 1. Load Pre-trained Model and Data ---

# Load the Random Forest model
# Make sure the 'nutriai_rf_model.pkl' file is in the same directory as app.py
try:
    with open('nutriai_rf_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'nutriai_rf_model.pkl' is in the correct directory.")
    st.stop()

# Load the scaler used during training
try:
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
except FileNotFoundError:
    st.error("Scaler file not found. Please ensure 'scaler.pkl' is in the correct directory.")
    st.stop()


# Load the curated food dataset for user selection
try:
    food_df = pd.read_csv('curated_food_dataset.csv')
except FileNotFoundError:
    st.error("Food dataset not found. Please ensure 'curated_food_dataset.csv' is in the correct directory.")
    st.stop()
    
# ROBUST DATA TYPE CONVERSION (Safety check)
nutrient_cols_to_convert = [
    'Calories (kcal)', 'Protein (g)', 'Carbohydrates (g)', 
    'Fat (g)', 'Fiber (g)', 'Sugars (g)'
]
for col in nutrient_cols_to_convert:
    food_df[col] = pd.to_numeric(food_df[col], errors='coerce')
food_df.dropna(subset=nutrient_cols_to_convert, inplace=True)


# --- 2. Define Helper Functions ---

# Dictionary of MET values for activities
activities = {
    'Running': 8.0,
    'Weightlifting': 5.0,
    'Cycling': 6.0,
    'Walking': 3.5,
    'Desk Work': 1.5,
    'Resting': 1.0
}

def estimate_calories_burned(activity, duration_minutes, weight_kg=70):
    """Estimates calories burned based on MET values."""
    met = activities.get(activity, 1.0)
    return (met * 3.5 * weight_kg) / 200 * duration_minutes

def get_daily_recommendation(row_data, prediction):
    """
    Generates a recommendation based on a row of daily user data and AI prediction.
    This function is adapted from the Colab notebook.
    """
    recommendations = []
    
    # Rule 1: Based on AI prediction
    if prediction == 0:
        protein_needed = row_data['protein_target_g'] - row_data['total_protein_g']
        if protein_needed > 20:
             recommendations.append(f"AI predicts you'll miss your protein goal. Consider a high-protein snack like Greek yogurt or a protein shake to add ~{protein_needed:.0f}g.")

    # Rule 2: Based on Calorie balance
    calorie_balance = row_data['total_calories_kcal'] - row_data['calorie_target_kcal']
    if calorie_balance > 300:
        recommendations.append("Your calorie intake is significantly over target. Consider opting for a lighter dinner.")

    # Rule 3: Based on Fat intake
    if row_data['total_fat_g'] > 90:
        recommendations.append("Your fat intake seems high today. Consider leaner protein sources.")

    if not recommendations:
        return "Your nutrition looks balanced for the day. Keep it up!"
        
    return " | ".join(recommendations)

# --- 3. Streamlit App Interface ---

st.set_page_config(page_title="NutriAI Assistant", layout="wide")

# Title and Team Info
st.title("🍏 NutriAI - Your AI-Enhanced Personal Nutrition Assistant")
st.markdown("Developed by: Aashish Giri, Jaykesh J Awal, Meet Patel, Sabin Khatri")
st.markdown("---")


# --- User Profile and Goal Selection ---
st.header("Step 1: Define Your Profile and Goals")

col1, col2 = st.columns(2)

with col1:
    persona_type = st.selectbox(
        'Select a Persona (this will set your goals)',
        ('Weight_Loss_Focus', 'Muscle_Gain_Focus', 'Sedentary_Lifestyle')
    )
    
with col2:
    if persona_type == 'Weight_Loss_Focus':
        calorie_target = 1800
        protein_target = 120
    elif persona_type == 'Muscle_Gain_Focus':
        calorie_target = 2800
        protein_target = 180
    else: # Sedentary_Lifestyle
        calorie_target = 2000
        protein_target = 80
        
    st.write("### Your Daily Targets:")
    st.metric(label="Calorie Target (kcal)", value=f"{calorie_target}")
    st.metric(label="Protein Target (g)", value=f"{protein_target}")


st.markdown("---")

# --- Daily Log Input ---
st.header("Step 2: Log Your Daily Food and Activity")

col3, col4 = st.columns(2)

with col3:
    st.subheader("🍳 Food Log")
    logged_foods = st.multiselect(
        'Select the foods you ate today:',
        options=food_df['Food_Item'].unique(),
        default=["Apple", "Chicken Breast", "Oats"]
    )
    
    if logged_foods:
        daily_intake_df = food_df[food_df['Food_Item'].isin(logged_foods)]
        total_calories = int(daily_intake_df['Calories (kcal)'].sum())
        total_protein = int(daily_intake_df['Protein (g)'].sum())
        total_carbs = int(daily_intake_df['Carbohydrates (g)'].sum())
        total_fat = int(daily_intake_df['Fat (g)'].sum())
    else:
        total_calories = total_protein = total_carbs = total_fat = 0

    st.write("#### Today's Nutritional Intake:")
    st.metric(label="Total Calories (kcal)", value=f"{total_calories}")
    st.metric(label="Total Protein (g)", value=f"{total_protein}")
    st.metric(label="Total Carbs (g)", value=f"{total_carbs}")
    st.metric(label="Total Fat (g)", value=f"{total_fat}")


with col4:
    st.subheader("🏃 Activity Log")
    activity_type_selection = st.selectbox(
        'Select your main activity today:',
        options=list(activities.keys())
    )
    duration = st.slider(
        'Duration (in minutes):', 
        min_value=0, max_value=240, value=60, step=15
    )
    
    calories_expended = estimate_calories_burned(activity_type_selection, duration)

    st.write("#### Today's Activity Expenditure:")
    st.metric(label="Calories Burned (kcal)", value=f"{int(calories_expended)}")

st.markdown("---")


# --- 4. AI Prediction and Recommendation (FINAL CORRECTED BLOCK) ---
st.header("Step 3: Get Your AI-Powered Recommendation")

if st.button('Analyze My Day'):
    if not logged_foods:
        st.warning("Please log at least one food item to get a recommendation.")
    else:
        # --- Prepare data for the model ---
        
        # 1. Create the initial dictionary with original text values
        input_data = {
            'total_calories_kcal': total_calories,
            'total_carbs_g': total_carbs,
            'total_fat_g': total_fat,
            'calories_expended': calories_expended,
            'calorie_target_kcal': calorie_target,
            'persona_type': persona_type,
            'activity_level': 'low' # Start with a default
        }

        # Convert the selected activity to the persona's activity_level category
        if activity_type_selection in ['Running', 'Weightlifting']:
            input_data['activity_level'] = 'high'
        elif activity_type_selection in ['Cycling', 'Walking']:
            input_data['activity_level'] = 'moderate'
        else:
            input_data['activity_level'] = 'low'

        # Convert dictionary to a DataFrame
        input_df = pd.DataFrame([input_data])

        # 2. Apply one-hot encoding exactly as done in training
        input_df_encoded = pd.get_dummies(input_df, columns=['persona_type', 'activity_level'], drop_first=True)

        # 3. Align columns with the training set to ensure a perfect match
        # This is the exact list from your final Colab notebook output
        training_columns = [
            'calories_expended', 'total_calories_kcal', 'total_carbs_g', 'total_fat_g',
            'calorie_target_kcal', 'persona_type_Sedentary_Lifestyle',
            'persona_type_Weight_Loss_Focus', 'activity_level_low',
            'activity_level_moderate'
        ]
        
        # Add any missing columns and fill with 0, then ensure final order is identical
        for col in training_columns:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0
        input_df_encoded = input_df_encoded[training_columns]

        # 4. Scale ONLY the numerical features using the loaded scaler
        numerical_cols = [
            'calories_expended', 'total_calories_kcal', 'total_carbs_g',
            'total_fat_g', 'calorie_target_kcal'
        ]
        input_df_encoded[numerical_cols] = scaler.transform(input_df_encoded[numerical_cols])

        # --- Make a prediction ---
        prediction = model.predict(input_df_encoded)[0]

        st.subheader("🤖 AI Prediction:")
        if prediction == 1:
            st.success("Our AI predicts you are on track to meet your primary protein goal!")
        else:
            st.warning("Our AI predicts you are likely to miss your primary protein goal.")

        # --- Generate and display recommendation ---
        recommendation_context = {
            'total_calories_kcal': total_calories,
            'total_protein_g': total_protein,
            'total_fat_g': total_fat,
            'calorie_target_kcal': calorie_target,
            'protein_target_g': protein_target
        }
        recommendation = get_daily_recommendation(recommendation_context, prediction)

        st.subheader("💡 Your Personalized Recommendation:")
        st.info(recommendation)