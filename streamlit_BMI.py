import streamlit as st

st.title("BMI Calculator")

st.header("Track your health with a simple calculation")
st.subheader("A healthy outside starts from the inside!")
st.text("Welcome to the BMI Calculator! Just enter your height and weight to see your Body Mass Index and find out where you stand.")

def BMI_calc(weight, height):
    height_m = height * 0.0254
    BMI_result = weight / (height_m**2)
    return BMI_result

weight = st.number_input("**Enter your Weight (kgs)**: ")
height = st.number_input("**Enter your Height (in)**: ")

btn = st.button("Submit")
if btn:
    if weight > 0 and height > 0:
        final_result = BMI_calc(weight, height)
        st.write(f"According to your Weight and Height, your BMI calculation is **{final_result:.2f}**")

        if final_result < 16:
            st.error("You are **Extremely Underweight**.")
        elif final_result >= 16 and final_result < 18.5:
            st.warning("You are **Underweight**.")
        elif final_result >= 18.5 and final_result < 25:
            st.success("You are **Healthy**.")
        elif final_result >= 25 and final_result < 30:
            st.info("You are **Overweight**.")
        elif final_result >= 30:
            st.error("You are **Extremely Overweight**.")

    else:
        st.error("An Error Occured. Please input the valid values for both Weight and Height.")

