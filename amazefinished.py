
import streamlit as st
import pandas as pd

# Load data
df = pd.read_excel("indigenous_translation_phrases_cleaned.xlsx", engine="openpyxl")

# Page setup
st.set_page_config(page_title="Talkwithamaze", layout="wide")
st.markdown(
    '''
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f6f8;
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #008080;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    .stTextInput input {
        border-radius: 0.5rem;
        padding: 0.4rem;
    }
    .stSelectbox > div > div {
        border-radius: 0.5rem;
    }
    </style>
    ''', unsafe_allow_html=True
)

st.title("🌿 Talkwithamaze")
st.caption("Empowering healthcare through language. Built for the Hackathon: *Nigerian Pharmacists in the AI Lab*")

tab = st.sidebar.radio("Navigate", [
    "📚 Translate Phrases",
    "💬 Chat with Amaze",
    "🌍 Join Our Mission",
    "🚀 Exciting Features"
])

if tab == "📚 Translate Phrases":
    st.subheader("📖 Translate Phrases")
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox("Choose Language", ["Berom", "Afizere", "Mwaghavul", "Rukuba"])
    with col2:
        direction = st.selectbox("Direction", ["English → Indigenous", "Indigenous → English"])

    options = df["english"].dropna().tolist() if direction.startswith("English") else df[language.lower()].dropna().tolist()
    user_input = st.selectbox("Select a phrase", [""] + options)

    col3, col4 = st.columns(2)
    with col3:
        st.button("🎤 Talk to AI (Coming Soon)", disabled=True)
    with col4:
        st.button("🔊 Read Aloud (Coming Soon)", disabled=True)

    if st.button("Translate"):
        if user_input:
            if direction.startswith("English"):
                match = df[df["english"].str.lower() == user_input.lower()]
                result = match[language.lower()].values[0] if not match.empty else None
            else:
                match = df[df[language.lower()].str.lower() == user_input.lower()]
                result = match["english"].values[0] if not match.empty else None

            if result:
                st.success(f"**Translation:**\n\n{result}")
            else:
                st.error("Phrase not found.")
        else:
            st.warning("Please select a phrase.")

elif tab == "💬 Chat with Amaze":
    st.subheader("💬 Simulated Pharmacy Chat")
    st.markdown("This chat uses rule-based logic to simulate basic consultation.")

    lang = st.selectbox("What language are you speaking?", ["English", "Berom", "Afizere", "Mwaghavul", "Rukuba"])
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Type your message:")

    col3, col4 = st.columns(2)
    with col3:
        st.button("🎤 Talk to Amaze (Coming Soon)", disabled=True)
    with col4:
        st.button("🔊 Read Aloud (Coming Soon)", disabled=True)

    if st.button("Send"):
        if user_input:
            if lang != "English":
                reply = f"I'm not yet trained to reply in {lang}, but we're working on it!"
            else:
                l = user_input.lower()
                if "headache" in l:
                    reply = "Do you also have a fever or just the headache?"
                elif "fever" in l:
                    reply = "Take one tablet of Paracetamol. Drink plenty water."
                elif "pregnant" in l:
                    reply = "Please confirm with a doctor before taking any medication."
                else:
                    reply = "Can you describe your symptoms more clearly?"
            st.session_state.history.append((user_input, reply))

    if st.session_state.history:
        st.markdown("### 🗣️ Conversation")
        for msg, res in reversed(st.session_state.history[-5:]):
            st.markdown(f"**You:** {msg}")
            st.markdown(f"**PharmaLingua:** {res}")

    if st.button("🗑 Clear Chat History"):
        st.session_state.history = []
        st.success("Chat cleared.")

elif tab == "🌍 Join Our Mission":
    st.subheader("🌍 Help Us Improve")
    st.markdown("We're building this for real-world impact. Can you help improve language support in Nigerian healthcare?")
    with st.form("join"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        lang_support = st.text_area("Message / Languages you can help with")
        if st.form_submit_button("Submit"):
            st.success("Thank you for joining our mission!")

    st.subheader("⭐ Rate Talkwithamaze")
    rating = st.slider("How would you rate this app?", 1, 5, 3)
    if st.button("Submit Rating"):
        st.success(f"Thanks for your rating: {rating}/5")

elif tab == "🚀 Exciting Features":
    st.subheader("🚀 Coming Soon to Talkwithamaze")
    st.markdown("Here's what we're working on for the next version:")
    st.markdown("✅ **📜 Chat History** — Save and revisit previous chats")
    st.markdown("✅ **🎤 Voice Input** — Talk directly to the chatbot using your mic")
    st.markdown("✅ **🔊 Read Aloud** — Let the AI read translations or responses aloud")
    st.markdown("✅ **📍 Location-Based Language** — Auto-suggest language by state/LGA")
    st.markdown("✅ **🧍‍♂️ Patient Mode** — Simplified interface for less tech-savvy users")
    st.markdown("✅ **💡 Suggested Phrases** — Get related translations or follow-up phrases")
    st.markdown("✅ **📥 Download Conversation Log** — Export chat history as .txt or .pdf")
    st.markdown("✅ **🌐 Offline Support** — Use in remote areas with no internet")
    st.markdown("✅ **🧠 Learn from Users** — Add new words and feedback to grow smarter")
    st.info("We're always looking for collaborators and feedback. Let's build this together!")
