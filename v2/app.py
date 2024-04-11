import streamlit as st

from utils import *



# function to get output on the screen
def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User 👤: ", message.content)
        else:
            st.write("BudgetBot 🤖 : ", message.content)


# Main function
def main():
    
    st.set_page_config(page_title='BudgetBotUK',page_icon='📝')
    st.image('files/hills1.jpeg')

    if "conversation" not in st.session_state: #st.session_state is used for make variables persistent during a session
        st.session_state.conversation = None
    
    
    st.header("BudgetBotUK") 
    st.subheader("Chatbot for Uttarakhand budget: 2024")
    user_question = st.text_input('Ask a Question related to budget speech.')

    if user_question:
        user_input(user_question)
    
    with st.sidebar:
        st.image('files/map.png')
        st.subheader('Click below to start Chatbot')
        
        if  st.button('Start'):
            with st.spinner('Initializing chatbot'):
                # get pdfs
                pdf_docs = 'files/speech.pdf'
                raw_text = load_pdf(pdf_docs)
                
                #get the text chunks
                text_chunks = chunk_data(raw_text)
                #st.write(text_chunks)

                # create vector db
                vectorstore = vector_store(text_chunks)

                #conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
                
                st.success("Done.Please Ask Questions!")

if __name__ == '__main__':
    main()