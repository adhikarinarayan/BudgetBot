# BudgetBotUK
BudgetBotUK is an LLM-powered chatbot that leverages RAG architecture to provide answers to questions related to the Budget of Uttarakhand, India. Currently, It can answer all the questions related to the budget speech given on the floor of Vidhansabha of Uttarakhand in 2024.

**Document used for RAG**: https://budget.uk.gov.in/files/english_translate_23-24_bhashan.pdf

---
## Tools used:
1. langchain
2.  google PaLM
3.  FAISS
4.  Streamlit


## Updated v2
- In the updated version **all-MiniLM-L6-v2** model is used to create the embeddings and **pinecone** is used as a vector database.

**Instructions**: Add Pinecone and Google API keys in the .env file and add the pinecone index name in the utils.py



---


## Chatbot architecture
![Alt text](https://github.com/adhikarinarayan/BudgetBot/blob/main/files/model.png "Chatbot Architecture")

## Some examples of answers from Budgetbot
![Alt text](https://github.com/adhikarinarayan/BudgetBot/blob/main/tests/1.png "1")
![Alt text](https://github.com/adhikarinarayan/BudgetBot/blob/main/tests/2.png "2")
![Alt text](https://github.com/adhikarinarayan/BudgetBot/blob/main/tests/3.png "3")

## Future work
Although BudgetBotUK's responses are good, we can improve it further.
1. Instead of GooglePalm, we can use other LLMs like LLama2, Mistral 7B, etc.
2. We can add more documents related to budget to improve the semantic search results.
3. Instead of FAISS, other vector databases like Pinecone can be utilized for this task.
