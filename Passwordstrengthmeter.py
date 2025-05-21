import streamlit as st
import re

def load_common_passwords():
    """Return a list of common passwords to blacklist"""
    common_passwords = [
        "password", "123456", "qwerty", "admin", "welcome", 
        "password123", "abc123", "letmein", "monkey", "1234567890",
        "trustno1", "dragon", "baseball", "football", "111111",
        "iloveyou", "master", "sunshine", "ashley", "bailey"
    ]
    return common_passwords

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Load common passwords
    common_passwords = load_common_passwords()
    
    # Check if password is in common password list
    if password.lower() in common_passwords:
        return -1, ["❌ This is a commonly used password and can be easily guessed!"], "BLACKLISTED", 0
    
    # Length check (weight: 1.5)
    if len(password) >= 8:
        score += 1.5
    else:
        feedback.append("❌ Password must be at least 8 characters long")

    # Case check (weight: 1.0)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1.0
    else:
        feedback.append("❌ Password must contain both uppercase and lowercase letters")

    # Number check (weight: 1.0)
    if re.search(r"\d", password):
        score += 1.0
    else:
        feedback.append("❌ Password must contain at least one number (0-9)")

    # Special character check (weight: 1.5)
    if re.search(r"[!@#$%^&*]", password):
        score += 1.5
    else:
        feedback.append("❌ Password must contain at least one special character (!@#$%^&*)")

    # No spaces check (weight: 0.5)
    if re.search(r"[a-zA-Z0-9!@#$%^&*]{8,}", password) and not re.search(r"\s", password):
        score += 0.5
    else:
        feedback.append("❌ Password must not contain spaces")

    # No repeating characters check (weight: 0.5)
    if re.search(r"(.)\1\1\1", password):
        score -= 0.5
        feedback.append("❌ Password should not contain repeating characters (e.g., 'aaaa')")

    # Extra: Length bonus
    if len(password) >= 12:
        score += 0.5
    
    # Strength Rating
    max_score = 6.0
    percentage = (score / max_score) * 100
    
    strength_message = ""
    if percentage >= 80:
        strength_message = f"✅ Strong Password! (Score: {score:.1f}/{max_score})"
    elif percentage >= 60:
        strength_message = f"⚠️ Moderate Password (Score: {score:.1f}/{max_score})"
    else:
        strength_message = f"❌ Weak Password (Score: {score:.1f}/{max_score})"
    
    return score, feedback, strength_message, percentage

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")
st.write("Check how strong your password is")

password_input = st.text_input("Enter your password:", type="password")

if password_input:
    score, feedback, strength_message, percentage = check_password_strength(password_input)
    
    st.write("### Results")
    st.progress(percentage/100)
    st.write(strength_message)
    
    if feedback:
        st.write("### Suggestions for improvement:")
        for item in feedback:
            st.write(item)
    else:
        st.success("Your password meets all the criteria!")

st.sidebar.header("About")
st.sidebar.info(
    """
    This app helps you check how strong your passwords are.
    
    **Features:**
    - Custom scoring weights for different criteria
    - Common password blacklist
    - Detailed feedback
    """
)