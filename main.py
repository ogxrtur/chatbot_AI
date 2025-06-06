import streamlit as st
from openai import OpenAI

modelo = OpenAI()
st.write("### ChatBot com IA")

# Inicializa a lista de mensagens no estado da sessão
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

#exibir historico

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)
    

# Campo de entrada do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

# Processa a mensagem se o usuário enviar
if mensagem_usuario:
    # Exibe a mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    
    # Salva no estado da sessão
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # Resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content
    

    # Exibe a resposta
    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)