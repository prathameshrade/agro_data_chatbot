import streamlit as st
import requests
st.title("ARGO Float Data Explorer")
query = st.text_input("Ask a question about ARGO data:")
if st.button("Submit") and query:
    response = requests.post("http://localhost:8000/query", json={"query": query})
    if response.status_code == 200:
        st.write(response.json()["response"])
st.write("Map, profile plots, and data tables would be here")
