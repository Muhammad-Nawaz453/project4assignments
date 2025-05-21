import pandas as pd
import streamlit as st

st.title('BMI Calculator')

height = st.number_input('Enter your height in cm: ',100,250,175)
weight = st.number_input('Enter your weight in kg: ',40,200,70)

bmi = weight / ((height/100)**2)
st.write('Your BMI is: ',bmi)

st.write('BMI Categories: ')
st.write('Underweight: BMI < 18.5')
st.write('Normal weight: 18.5 <= BMI < 24.9')
st.write('Overweight: 25 <= BMI < 29.9')
st.write('Obesity: BMI >= 30')  