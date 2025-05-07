import streamlit as st

st.markdown("<h1 style='text-align: center; font-size: 64px;'>Chat</h1>", unsafe_allow_html=True)
st.divider()
lc, rc = st.columns(2)
with lc:
    st.write("## Client")
    nickname = st.text_input("Nickname:", placeholder="Insira seu nickname...")
    if nickname:   
        with open("client.txt", "a") as f:
            f.write(f"Nickname:{nickname}")
        
    def clear_text():
        st.session_state.widget = ""
        status = "Enviado"
    msg = st.text_input('Mensagem', placeholder="Insira sua mensagem....",key='widget', on_change=clear_text)
    
    if msg:
         st.write("Enviado")
        
with rc:
    st.write("## Server")
    st.write(f"Nickname: {nickname}")
