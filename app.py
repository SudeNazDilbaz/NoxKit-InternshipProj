import streamlit as st

from noxkit.password_analyzer import analyze_password

st.set_page_config(
    page_title="NOXKIT",
    page_icon="🌙",
    layout="wide"
)

st.title("🌙 NOXKIT")
st.subheader("Python Security Toolkit")

st.write("Welcome to NOXKIT!")
st.write("This toolkit provides simple security-related utilities.")

st.divider()
st.header("🔑Password Analyzer")

password = st.text_input("Enter a password:", type="password")

if st.button("Analyze Password"):
    if not password:
        st.warning("Please enter a password.")
    else:
        result = analyze_password(password)
        checks = result["checks"]
        score = result["score"]

        st.subheader("Analysis Results")

        st.write(f"Score: {score}/5")
        st.progress(score / 5)

        if score <= 2:
            st.error("Weak Password")
            
        elif score <= 4:
            st.warning("Medium Password")
        
        else:
            st.success("Strong Password")

        if checks["length"]: 
            st.success("At least 8 characters") 
        else: 
            st.error("At least 8 characters") 
            
        if checks["uppercase"]: 
            st.success("Contains an uppercase letter") 
        else: 
            st.error("Contains an uppercase letter") 
            
        if checks["lowercase"]: 
            st.success("Contains a lowercase letter") 
        else: 
            st.error("Contains a lowercase letter") 
            
        if checks["number"]: 
            st.success("Contains a number") 
        else: 
            st.error("Contains a number") 
            
        if checks["special"]: 
            st.success("Contains a special character") 
        else: 
            st.error("Contains a special character")
        
        st.subheader("Suggestions")
        
        if not checks["length"]:
            st.write("• Increase password length (at least 8 characters).")
        
        if not checks["uppercase"]:
            st.write("• Add an uppercase letter.")
            
        if not checks["lowercase"]:
            st.write("• Add a lowercase letter.")
            
        if not checks["number"]:
            st.write("• Add a number.")
            
        if not checks["special"]:
            st.write("• Add a special character.")
        
        if score == 5:
            st.success("Excellent! Your password meets all recommended security criteria.")
