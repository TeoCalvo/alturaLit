import streamlit as st
import pandas as pd
import os

st.write(""" 
# Vamos checar sua altura?

Uma brincadeira na comunidade do Téo Me Why para identificar a altura da galera!

Dê uma conferida no nosso repositório no github: [github.com/teocalvo/alturalit](https://github.com/teocalvo/alturalit)

Insira suas informações para checarmos...
""")

model = pd.read_pickle("models/model_tree.pkl")

features = model['features']

fields = { f: [st.radio( f, ("Nunca", "As vezes", "Sempre") )] for f in features[:-3] }
fields[ features[-3] ] = [st.radio( features[-3],
                                  ("Máxima, mais alta",
                                   "Mediana",
                                   "Mínima, mais baixa"))]

fields[ features[-2] ] = [st.radio( features[-2],
                                  ("Sim",
                                  "Não") )]

fields[features[-1]] = [st.slider("Qual o tamanho do seu calçado?",
                                  25, 46, 35)]

data = pd.DataFrame(fields)

altura = model["model"].predict(data[features])[0]
st.text(f"Estimamos que a sua altura é: {altura:.2f}")

st.write("""
## Quer contribuir?

Fique a vontade para contribuir adicionando seus dados neste [formulário](https://forms.gle/eoszvqSKWUGerHTu8).
""")
