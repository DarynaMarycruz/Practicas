import os
import pandas as pd
from pandasai import Agent
import streamlit as st

os.environ["PANDASAI_API_KEY"] = "$2a$10$R/j.oBm1k1A/ND0uQS8uKegnoHshq1EffC5SYPTZtNA8bcPrDLj7m"


st.title("Probando Streamlit")
upload_file=st.file_uploader("Upload a CSV file for analysis", type=['csv'])
if upload_file is not None:
    df = pd.read_csv(upload_file, delimiter=';')
    st.write(df.head(3))

    prompt = st.text_area("Escribe tu consulta")
    if st.button("Responder"):
        if prompt:
            st.write("Estamos generando su respuesta por favor esperar")
            agent = Agent(df)
            st.write(agent.chat(prompt))
     
        else:
            st.warning("Por favor introduza su pregunta")
# Sample DataFrame


# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
# Link referencia https://www.youtube.com/watch?v=oSC2U2iuMRg&list=PL-2EBeDYMIbTw2NtO8DCubf4U7q52l6il&index=3


