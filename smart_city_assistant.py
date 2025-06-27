import streamlit as st
import requests

st.set_page_config(page_title="🌆 Smart City Assistant", layout="wide")

# Optional basic CSS styling
st.markdown("""
    <style>
    .main .block-container {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #006699;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌇 Sustainable Smart City Assistant")

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Choose an option", ["💬 Chat", "📊 Dashboard", "📄 Report", "ℹ️ About"])

# 🔐 Hugging Face API config — Replace with your token
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": "Bearer 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"}  # <- Replace YOUR_HF_TOKEN

def query_huggingface(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"❌ API Error: {response.status_code} - {response.reason}"

# 💬 Chat Page
if menu == "💬 Chat":
    st.header("Ask the Assistant 💬")
    question = st.text_input("Ask something about sustainability, smart energy, or waste...")
    if st.button("Ask"):
        if question:
            with st.spinner("Thinking..."):
                response = query_huggingface(f"You are a sustainability assistant. Answer this: {question}")
                st.success("Assistant says:")
                st.write(response)

# 📊 Dashboard Page
elif menu == "📊 Dashboard":
    st.header("Smart City Dashboard 📊")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🌡 AQI", "85", "-5")
        st.metric("⚡ Electricity", "320 MW", "+12")
    with col2:
        st.metric("💧 Water", "1200 ML", "-50")
        st.metric("🗑 Waste", "200 T", "+10")

# 📄 Report Page
elif menu == "📄 Report":
    st.header("Generate Sustainability Report 📄")
    prompt = """
    Create a sustainability report:
    - Air Quality Index: 85 (↓5)
    - Electricity: +12%
    - Water: -4%
    - Waste: +10 tons
    Provide summary and suggestions.
    """
    if st.button("Generate Report"):
        with st.spinner("Generating report..."):
            report = query_huggingface(prompt)
            st.success("📄 Report:")
            st.write(report)

# ℹ️ About Page
elif menu == "ℹ️ About":
    st.header("About This Project ℹ️")
    st.markdown("""
    - Internship: **SmartInternz (2025)**
    - Tech Used: **Hugging Face**, **Streamlit**
    - Purpose: Provide sustainable insights for smart city planning using Generative AI.
    """)

st.markdown("---")
st.markdown("🚀 Smart City Assistant • Hugging Face • Built with ❤ for sustainability.")


