# BudgetBotUK
BudgetBotUK is an LLM-powered chatbot that leverages RAG architecture to provide answers to questions related to Budget of Uttarakhand. Currently, It can answer all the questions related to the budget speech given on the floor of Vidhansabha of Uttarakhand in 2024.

**Document used for RAG**: https://budget.uk.gov.in/files/english_translate_23-24_bhashan.pdf


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
