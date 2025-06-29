import streamlit as st
import requests

st.set_page_config(page_title="ITSM AI Assistant", page_icon="🤖")

st.title("🤖 FixBot:AI for IT Support")

API_URL = "http://localhost:8000"  # Update to your FastAPI server address if needed

# Initialize session state for conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for selecting API mode
st.sidebar.header("Assistant Mode")
mode = st.sidebar.radio(
    "Choose what you want to do:",
    [
        "Conversational Assistant (Chat)",
        "Recommend Resolution",
        "Search Similar Incidents"
    ]
)

def ask_assistant(question, history):
    """Send a question (with history) to the /ask-assistant endpoint."""
    try:
        response = requests.post(
            f"{API_URL}/ask-assistant",
            json={
                "question": question,
                "history": history
            },
            timeout=50
        )
        response.raise_for_status()
        return response.json().get("answer", str(response.json()))
    except Exception as e:
        return f"Error: {e}"

def recommend_resolution(description):
    """Call /recommend-resolution with incident description."""
    try:
        response = requests.post(
            f"{API_URL}/recommend-resolution",
            json={"description": description},
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("resolutions", response.json())
    except Exception as e:
        return f"Error: {e}"

def search_similar(incident):
    """Call /search-similar-incidents with incident description."""
    try:
        response = requests.post(
            f"{API_URL}/search-similar-incidents",
            json={"description": incident},
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("similar_incidents", response.json())
    except Exception as e:
        return f"Error: {e}"

# Conversational Assistant (multi-turn chat)
if mode == "Conversational Assistant (Chat)":
    st.markdown("Ask anything about past incidents, solutions, or ITSM knowledge.")

    # Show chat history
    for entry in st.session_state.chat_history:
        with st.chat_message(entry["role"]):
            st.markdown(entry["content"])

    # User input
    user_input = st.chat_input("Type your question and press Enter")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        # Build conversational history as list of dicts (role/content)
        history = [
            {"role": entry["role"], "content": entry["content"]}
            for entry in st.session_state.chat_history
        ]
        with st.chat_message("assistant"):
            answer = ask_assistant(user_input, history)
            st.markdown(answer)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

    if st.button("Clear Conversation"):
        st.session_state.chat_history = []

# Recommend Resolution
elif mode == "Recommend Resolution":
    st.markdown("Enter a new incident description to get probable resolutions.")
    incident_desc = st.text_area("Incident Description", height=100)
    if st.button("Recommend Resolution"):
        if incident_desc.strip():
            resolutions = recommend_resolution(incident_desc)
            st.subheader("Suggested Resolutions:")
            if isinstance(resolutions, list):
                for idx, res in enumerate(resolutions, 1):
                    st.write(f"{idx}. {res}")
            else:
                st.write(resolutions)
        else:
            st.warning("Please enter an incident description.")

# Search Similar Incidents
elif mode == "Search Similar Incidents":
    st.markdown("Find similar past incidents by description.")
    similar_desc = st.text_area("Incident Description", height=100, key="sim_desc")
    if st.button("Search Similar Incidents"):
        if similar_desc.strip():
            similar_incidents = search_similar(similar_desc)
            st.subheader("Similar Incidents:")
            if isinstance(similar_incidents, list):
                for idx, inc in enumerate(similar_incidents, 1):
                    st.write(f"{idx}. {inc}")
            else:
                st.write(similar_incidents)
        else:
            st.warning("Please enter an incident description.")

st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ for Code For Bharat 2")