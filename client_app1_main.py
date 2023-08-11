import streamlit as st
from backend import index_documents, my_chatGPT_bot
from os.path import exists
import pickle
# Set page configuration and title
st.set_page_config(layout="wide")
def main_content():
    # Center-align the text using CSS styling
    st.markdown(
        """
        <style>
        .centered-text {
            display: flex;
            justify-content: center;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    frame_style = """
        <style>
        .frame {
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 10px;
            margin-left:20px;
            margin-right:20px;
        }
        </style>
    """
    # Set page title
    # Display the centered text
    st.markdown('<p class="centered-text"><h1>STEVE Customized PDF Q&A</h1></p>', unsafe_allow_html=True)
    # Initialize the list
    question_answer_list = []

    # Load the list from a pickle file if it exists
    if "qa_list" in st.session_state:
        question_answer_list = st.session_state.qa_list

    # Display the existing questions and answers
    if question_answer_list:
        st.subheader("Previous Questions and Answers")
        for qa_pair in question_answer_list:
            question, answer = qa_pair
            st.markdown(frame_style, unsafe_allow_html=True)
            st.markdown(f'<div class="frame"><i><strong><span style="color:#00BFFF">Question</span></strong></i>: {question}\n\n\n<br> <i><strong><span style="color:#00BFFF">Response</span></strong></i>: {answer}</div>', unsafe_allow_html=True)
            # st.write("---")

    # Check if a question is entered
    # Define the CSS styling for the frame-like container
    # Create the form
    with st.form("my_form"):
        # Add the input text field
        new_question = st.text_input("Ask a question")

        # Add the submit button
        submit_button = st.form_submit_button("Submit")
        

    # Wrap the output values in a frame-like container    
    if new_question:
        if submit_button:
            # Perform actions or process the user input
            # Create the form
            new_answer = my_chatGPT_bot(new_question)            
            # Add the input text field
            question_answer_list.append((new_question, new_answer))
            st.session_state.qa_list = question_answer_list
            # Save the list to a pickle file
            with open("question_answer_list.pkl", "wb") as file:
                pickle.dump(question_answer_list, file)
        st.subheader("Latest Question and Answer")
        st.markdown(frame_style, unsafe_allow_html=True)
        st.markdown(f'<div class="frame"><i><strong><span style="color:#00BFFF">Question</span></strong></i>: {new_question}\n\n\n<br> <i><strong><span style="color:#00BFFF">Response</span></strong></i>: {new_answer}</div>', unsafe_allow_html=True)
        st.write("---")
if __name__ == '__main__':
    main_content()