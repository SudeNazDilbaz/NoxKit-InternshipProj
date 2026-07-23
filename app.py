import streamlit as st

from noxkit.file_integrity import generate_file_hash
from noxkit.hash_generator import generate_hash
from noxkit.password_analyzer import analyze_password


st.set_page_config(
    page_title="NOXKIT",
    page_icon="🌙",
    layout="wide",
)


APP_STYLE = """
<style>

/* Background */
.stApp {
    background: #1E1E2F;
    color: #F3F4F6;
}

/* All text */
html, body, p, label, span, div {
    color: #F3F4F6;
}

/* Titles */
h1, h2, h3 {
    color: #A78BFA !important;
}

h1 {
    text-shadow:
        0 0 8px rgba(139, 92, 246, 0.45),
        0 0 18px rgba(139, 92, 246, 0.25);
}

/* Caption */
[data-testid="stCaptionContainer"] {
    color: #C4C4D4 !important;
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
.stTextInput input {
    background: #2A2A40 !important;
    color: white !important;
    border: 1px solid #555;
}

/* Selectbox */
[data-baseweb="select"] > div {
    background: #2A2A40 !important;
    color: white !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    color: white;
}

/* Buttons */
.stButton > button {
    background: #8B5CF6;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background: #7C3AED;
}

</style>
"""


CHECK_MESSAGES = {
    "length": "At least 8 characters",
    "uppercase": "Contains an uppercase letter",
    "lowercase": "Contains a lowercase letter",
    "number": "Contains a number",
    "special": "Contains a special character",
}


SUGGESTION_MESSAGES = {
    "length": "Increase password length (at least 8 characters).",
    "uppercase": "Add an uppercase letter.",
    "lowercase": "Add a lowercase letter.",
    "number": "Add a number.",
    "special": "Add a special character.",
}


def display_password_strength(score: int) -> None:
    """Displays the password strength according to it's score."""

    if score <= 2:
        st.error("Weak Password")

    elif score <= 4:
        st.warning("Medium Password")

    else:
        st.success("Strong Password")


def display_password_checks(checks: dict[str, bool]) -> None:
    """Displays the result of each password security check."""

    for check_name, message in CHECK_MESSAGES.items():

        if checks[check_name]:
            st.success(message)

        else:
            st.error(message)


def display_password_suggestions(checks: dict[str, bool]) -> None:
    """Displays suggestions for failed password checks."""

    failed_checks = [
        check_name
        for check_name, passed in checks.items()
        if not passed
    ]

    if not failed_checks:
        st.success(
            "Excellent! Your password meets all "
            "recommended security criteria."
        )
        return

    st.subheader("Suggestions")

    for check_name in failed_checks:
        st.write(f"• {SUGGESTION_MESSAGES[check_name]}")


def render_password_analyzer() -> None:
    """Renders the Password Analyzer module."""

    with st.container(border=True):

        st.subheader("🔑 Password Analyzer")

        st.caption(
            "Check whether your password meets "
            "common security requirements."
        )

        password = st.text_input(
            "Enter a password:",
            type="password",
        )

        if not st.button("Analyze Password"):
            return

        if not password:
            st.warning("Please enter a password.")
            return

        result = analyze_password(password)
        checks = result["checks"]
        score = result["score"]

        st.subheader("Analysis Results")

        st.write(f"Score: {score}/5")
        st.progress(score / 5)

        display_password_strength(score)
        display_password_checks(checks)
        display_password_suggestions(checks)


def render_hash_generator() -> None:
    """Renders the Hash Generator module."""

    with st.container(border=True):

        st.subheader("🔒 Hash Generator")

        st.caption(
            "Generate cryptographic hash values "
            "using different algorithms."
        )

        text = st.text_input("Enter text to hash")

        algorithm = st.selectbox(
            "Select an algorithm",
            [
                "MD5",
                "SHA-1",
                "SHA-256",
                "SHA-512",
            ],
        )

        if not st.button("Generate Hash"):
            return

        if not text:
            st.warning("Please enter some text.")
            return

        hash_result = generate_hash(text, algorithm)

        if hash_result is None:
            st.error("Unsupported hash algorithm.")
            return

        st.subheader("Hash Result")
        st.code(hash_result)
        st.success("Hash generated successfully.")


def render_file_integrity_checker() -> None:
    """Renders the File Integrity Checker module."""

    with st.container(border=True):

        st.subheader("📁 File Integrity Checker")

        st.caption(
            "Calculate the SHA-256 hash of an uploaded file."
        )

        uploaded_file = st.file_uploader(
            "Upload a file",
            type=None,
        )

        if uploaded_file is None:
            return

        st.write(f"File name: {uploaded_file.name}")
        st.write(f"File size: {uploaded_file.size} bytes")

        if not st.button("Generate File Hash"):
            return

        file_data = uploaded_file.getvalue()
        file_hash = generate_file_hash(file_data)

        if file_hash is None:
            st.error("The file hash could not be generated.")
            return

        st.subheader("SHA-256 Hash")
        st.code(file_hash)
        st.success("File hash generated successfully.")


def main() -> None:
    """Runs the NoxKit Streamlit application."""

    st.markdown(APP_STYLE, unsafe_allow_html=True)

    st.markdown(
        """
        <h1 style="text-align:center; color:#6C63FF;">
            🌙 NOXKIT
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center;'>Security Toolkit</p>",
        unsafe_allow_html=True,
    )

    st.divider()

    st.write("Welcome to NOXKIT!")
    st.write(
        "This toolkit provides simple "
        "security-related utilities."
    )

    st.divider()

    render_password_analyzer()

    st.divider()

    render_hash_generator()

    st.divider()

    render_file_integrity_checker()

    st.divider()

    st.caption("NoxKit v1.0 • Security Toolkit")


if __name__ == "__main__":
    main()