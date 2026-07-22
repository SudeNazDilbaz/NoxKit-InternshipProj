import streamlit as st

from noxkit.password_analyzer import analyze_password

from noxkit.hash_generator import generate_hash

from noxkit.file_integrity import generate_file_hash

st.set_page_config(
    page_title="NOXKIT",
    page_icon="🌙",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background:#1E1E2F;
    color:#F3F4F6;
}

/* All text */
html, body, p, label, span, div{
    color:#F3F4F6;
}

/* Titles */
h1,h2,h3{
    color:#A78BFA !important;
}
h1{
    text-shadow:
        0 0 8px rgba(139, 92, 246, 0.45),
        0 0 18px rgba(139, 92, 246, 0.25);
}

/* Caption */
[data-testid="stCaptionContainer"]{
    color:#C4C4D4 !important;
}

/* Streamlit containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #2A2A40;
    border: 1px solid #404060 !important;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 25px;
}
   
/* Text Input */
.stTextInput input{
    background:#2A2A40 !important;
    color:white !important;
    border:1px solid #555;
}

/* Selectbox */
[data-baseweb="select"] > div{
    background:#2A2A40 !important;
    color:white !important;
}

/* File uploader */
[data-testid="stFileUploader"]{
    color:white;
}

/* Buttons */
.stButton > button{
    background:#8B5CF6;
    color:white;
    border-radius:10px;
    border:none;
    font-weight:bold;
}

.stButton > button:hover{
    background:#7C3AED;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;color:#6C63FF;'>
🌙 NOXKIT
</h1>
""", unsafe_allow_html=True)

st.markdown(
"<p style='text-align:center;'>Security Toolkit</p>",
unsafe_allow_html=True
)

st.divider()

st.write("Welcome to NOXKIT!")
st.write("This toolkit provides simple security-related utilities.")

st.divider()

with st.container(border=True):

    st.subheader("🔑 Password Analyzer")

    st.caption(
        "Check whether your password meets common security requirements."
    )

    password = st.text_input(
        "Enter a password:",
        type="password"
    )

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
                st.success(
                    "Excellent! Your password meets all recommended security criteria."
                )

st.divider()

with st.container(border=True):

    st.subheader("🔒 Hash Generator")

    st.caption(
        "Generate cryptographic hash values using different algorithms."
    )

    text = st.text_input("Enter text to hash")

    algorithm = st.selectbox(
        "Select an algorithm",
        [
            "MD5",
            "SHA-1",
            "SHA-256",
            "SHA-512",
        ]
    )

    if st.button("Generate Hash"):

        if not text:
            st.warning("Please enter some text.")

        else:
            hash_result = generate_hash(text, algorithm)

            st.subheader("Hash Result")
            st.code(hash_result)
            st.success("Hash generated successfully.")

st.divider()

with st.container(border=True):

    st.subheader("📁 File Integrity Checker")

    st.caption(
        "Calculate the SHA-256 hash of an uploaded file."
    )

    uploaded_file = st.file_uploader(
        "Upload a file",
        type=None
    )

    if uploaded_file is not None:

        st.write(f"File name: {uploaded_file.name}")
        st.write(f"File size: {uploaded_file.size} bytes")

        if st.button("Generate File Hash"):

            file_data = uploaded_file.getvalue()
            file_hash = generate_file_hash(file_data)

            if file_hash is None:
                st.error("The file hash could not be generated.")

            else:
                st.subheader("SHA-256 Hash")
                st.code(file_hash)
                st.success("File hash generated successfully.")

st.divider()

st.caption("NoxKit v1.0 • Security Toolkit")