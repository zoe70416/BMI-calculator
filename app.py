import streamlit as st

def calculate_bmi(height_in_inches, weight_in_pounds):
    #convert height from inches to meters 
    height_in_meters = height_in_inches * 0.0254

    #convert weight from pounds to kilograms
    weight_in_kilograms = weight_in_pounds * 0.453592

    #calcualte the bmi 
    bmi = weight_in_kilograms / (height_in_meters ** 2)
    return bmi


#streamlist app title
st.title("BMI Calculator")

#Get user input for height and weight 

user_height = st.number_input("Enter your height in inches", min_value=0.0)
user_weight = st.number_input("Enter your weight in pounds", min_value=0.0)

#calculate BMI
if st.button("Calculate BMI"):
  bmi = calculate_bmi(user_height,user_weight)
  #print out statement for streamlit
  st.write(f"BMI result {bmi:.2f}") 
