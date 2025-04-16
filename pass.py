#import streamlit
import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Meter")
st.markdown("""
##  Welcome to the ultimate password strength checker! 
###  use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
#### we will you helpful tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌ Password should be 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case character.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    if re.search(r'[!@#%^*()]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character [!@#%^*()]")
    if score == 4:
        feedback.append("✔ Your password is Strong!")
    elif score == 3:
        feedback.append("✔ Your passwaord is Medium!")
    else:
        feedback.append("❌ Your password is weak please make it stronger")
    if feedback:
        st.markdown("## Improvement Suggetions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter Your password to get started.")