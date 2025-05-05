import socket, asyncio
import streamlit as st
from client import client
import server

# async def main():
    # st.write("# Chat")
    # cliente = client(ip='localhost', port=8080)
    # lc, rc = st.columns(2)
    # msg = st.text_input(label="Mensagem:",key="msg")
    # if msg:
    #     cliente.connect()
    #     cliente.send(msg=msg)
    #     cliente.close()
    # st.write(msg)

async def clientea():
    cliente = client(ip='localhost', port=8080)
    msg = input("Msg: ")
    if not msg.empty():
        cliente.connect()
        cliente.send(msg=msg)
        cliente.close()
    else:
        print("Mensagem vazia")

asyncio.run(server.server())
asyncio.run(clientea())