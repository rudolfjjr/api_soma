# -*- coding: utf-8 -*-
# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Sum App", layout="centered")
st.title("Exemplo: Streamlit + FastAPI — Soma de 2 números")

st.markdown("Digite dois números e clique em **Somar**. O Streamlit fará uma chamada HTTP para a API FastAPI.")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Valor A", value=1.0, step=1.0, format="%.6f")
with col2:
    b = st.number_input("Valor B", value=2.0, step=1.0, format="%.6f")

api_url = st.text_input("URL da API", value="http://127.0.0.1:8000/add")
if st.button("Somar"):
    try:
        payload = {"a": float(a), "b": float(b)}
        # chamada POST JSON
        r = requests.post(api_url, json=payload, timeout=10.0)
        r.raise_for_status()
        data = r.json()
        st.success(f"Resultado: {data['result']}")
        st.json(data)
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na chamada à API: {e}")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")