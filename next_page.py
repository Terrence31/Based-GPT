import streamlit as st
from datetime import datetime


# Configure page layout
st.set_page_config(
    page_title="BasedGPT",
    page_icon=":speech_balloon:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set primary colors
PRIMARY_COLOR = "#566D7E"
PRIMARY_TEXT_COLOR = "#FFFFFF"

# Set secondary colors
SECONDARY_COLOR = "#F7F7F7"
SECONDARY_TEXT_COLOR = "#333333"

# Set accent colors
ACCENT_COLOR = "#A2AD9C"
ACCENT_TEXT_COLOR = "#FFFFFF"

# Set font sizes
LARGE_FONT_SIZE = "24px"
MEDIUM_FONT_SIZE = "18px"
SMALL_FONT_SIZE = "14px"

# Set chat message colors
USER_MESSAGE_COLOR = PRIMARY_COLOR
ASSISTANT_MESSAGE_COLOR = ACCENT_COLOR

# Set chat message styles
USER_MESSAGE_STYLE = f"""
    background-color: {USER_MESSAGE_COLOR};
    color: {PRIMARY_TEXT_COLOR};
    padding: 5px;
"""

ASSISTANT_MESSAGE_STYLE = f"""
    background-color: {ASSISTANT_MESSAGE_COLOR};
    color: {ACCENT_TEXT_COLOR};
    padding: 10px;
"""
#commands

col1, col2 = st.columns(2)

col1.markdown(
    """
        <h3><strong>FEATURES</strong></h3>
        <div style="background-color:beige; border: 2px solid black; border-radius: 10px; padding: 10px; color:black;">
        <p>
            <strong>Text generation:</strong> Based GPT can generate coherent and relevant text based on a given prompt
            or context.<br>
            <strong>Language translation:</strong> Based GPT supports 14 different languages and can translate text from
            one language to another.<br>
            <strong>Text summarization:</strong> Based GPT summarizes long texts into shorter and more concise
            text.<br>
            <strong> Question-answering:</strong> Based GPT can answer questions based on a given context or
            prompt.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col2.markdown(
    """
        <h3><strong>LIMITATIONS</strong></h3>
        <div style="background-color:beige; border: 2px solid black; border-radius: 10px; padding: 10px; color:black;">
        <p>May occasionally generate incorrect information.<br><br>
            May occasionally produce harmful instructions or biased content.<br><br>
            Supports only a few language translations.<br>
            </p>
    </div>
    """,
    unsafe_allow_html=True
)


# Page title
st.title("BasedGPT")

# Sidebar
st.sidebar.title("BasedGPT")


with st.sidebar.container():
    st.header("Settings")
    user_name = st.text_input("Your Name", "User")
    show_timestamps = st.checkbox("Show Timestamps")

    st.markdown(
        """
        <style>
        .sidebar .element-container {
            background-color: gray;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

#logic
#def translate(text):
 #   trans_text          #add the translated text


# Main content

chat_history = []
button=st.button("Translation")
message_input = st.text_input("Welcome " + user_name)

if button:
    col3,col4=st.columns(2)
    with col3:
        col3.header("Original Text")
        languages = ["AUTO-DETECT","ARABIC","CHINESE","CZECH","ENGLISH","FRENCH","GERMAN","HINDI","INDONESIAN","ITALIAN","MALAYALAM","MARATHI","RUSSIAN","UKRAINIAN","VIETNAMESE"]
        language_selected= st.selectbox("",options=languages)
        input_text = col3.text_input("Enter the text to be Translated")
    
    with col4:
        col4.header("Translated Text")
        languages = ["ARABIC","CHINESE","CZECH","ENGLISH","FRENCH","GERMAN","HINDI","INDONESIAN","ITALIAN","MALAYALAM","MARATHI","RUSSIAN","UKRAINIAN","VIETNAMESE"]
        language_selected= st.selectbox(" ",options=languages)
        col4.write("The translation is")
        col4.markdown(
        """
        <div style="background-color:gray; border: 2px solid black; border-radius: 10px; padding: 10px;">
        </div>
        """,
        unsafe_allow_html=True
        )
    

    

if message_input:
    # Add user message to chat history
    chat_history.append({
        "timestamp": datetime.now(),
        "name": user_name,
        "message": message_input,
        "is_user": True,
    })

    # Generate assistant response (dummy response in this example)
    assistant_response = "This is the assistant's response."

    # Add assistant message to chat history
    chat_history.append({
        "timestamp": datetime.now(),
        "name": "Assistant",
        "message": assistant_response,
        "is_user": False,
    })

# Display chat history
for chat in chat_history:
    # Display timestamp if enabled
    if show_timestamps:
        st.write(chat["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))

    # Display user message
    if chat["is_user"]:
        st.markdown(f'<div style="{USER_MESSAGE_STYLE}">{chat["message"]}</div>', unsafe_allow_html=True)
    # Display assistant message
    else:
        st.markdown(f'<div style="{ASSISTANT_MESSAGE_STYLE}">{chat["message"]}</div>', unsafe_allow_html=True)
