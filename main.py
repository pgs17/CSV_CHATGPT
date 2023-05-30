import streamlit as st
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
from dotenv import load_dotenv
import os
# creating GUI 
def main():

    # to make sure env variables are read 
    load_dotenv()

    st.set_page_config(page_title="CSV CHATGPT")
    st.header("CHATGPT FOR CSV")

    user_csv=st.file_uploader("Upload The CSV file",type=['CSV'])

# action when user has entered his csv
    if user_csv is not None:
          question=st.text_input("Ask Question About YOur CSV FILE")
       
         
        
          llm=OpenAI(temperature=0.7)
          agent=create_csv_agent(llm,user_csv,verbose=True)

       


    #    now agent is used to answer the question 
          if question is not None and question!="":
              
            response=agent.run(question)
            st.write(response)
   

if __name__=="__main__":
    main()    