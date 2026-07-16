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

        st.subheader("Analysis Results")

        if result["length"]:
            st.success("At least 8 characters")
        else:
            st.error("At least 8 characters")

        if result["uppercase"]:
            st.success("Contains an uppercase letter")
        else:
            st.error("Contains an uppercase letter")

        if result["lowercase"]:
            st.success("Contains a lowercase letter")
        else:
            st.error("Contains a lowercase letter")

        if result["number"]:
            st.success("Contains a number")
        else:
            st.error("Contains a number")

        if result["special"]:
            st.success("Contains a special character")
        else:
            st.error("Contains a special character")