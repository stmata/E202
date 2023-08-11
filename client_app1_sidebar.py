import streamlit as st
import os
# Call the folder containing your documents: 
doc_path = '../Docs/'    

def sidebar_content():
    # Create a sidebar
    st.sidebar.title("Welcome Human!")

    # Dropdown list
    option = st.sidebar.selectbox(" Select Model", ("ChatOpenAI", "BERT", "ChatOpenAI & BERT"))
    # Display selected values
    # st.sidebar.write("Selected Option:", option)
    # Radio buttons
    file_option = st.sidebar.radio("Select File Option", ("Existing", "Upload New File")) 
    # Existing files selection
    if file_option == "Existing":
        docs_folder = doc_path  # Specify the folder name here
        files = os.listdir(docs_folder)
        # Alow user to filder
        selected_files = st.sidebar.multiselect("Select Files", files)
        # Create file paths for selected files to be used for Q&A (subset)
        selected_file_paths = [os.path.join(docs_folder, file) for file in selected_files]

    # Upload new files section
    else:
        uploaded_files = st.sidebar.file_uploader("Upload one or more PDFs", accept_multiple_files=True, type="pdf")
        selected_files = []

        if uploaded_files:
            # Create a "Docs" folder if it doesn't exist
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)


            for file in uploaded_files:
                file_path = os.path.join(doc_path, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                selected_files.append(file_path)

        
        

