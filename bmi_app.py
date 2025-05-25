import streamlit as st 

# App Title
st.title("BMI Calculator")

# User Inputs
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=250.0, step=1.0)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=1.0)

# Calculate BMI
if st.button("Calculate BMI"):
    if height and weight:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.success(f"Your BMI is {bmi:.2f} ({category})")
    else:
        st.error("Please enter valid height and weight.")
