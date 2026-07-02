import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write("This app calculates the power of a number given a base and an exponent.")

#get the user input for base and exponent
n = st.number_input("Enter the base (n):", value=1, step=1)

#calculate result
square = n ** 2
cube = n ** 3
fifth_power = n ** 5

#Display the results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")