#import libraries
import encryptFunctions as fn
import streamlit as st
from streamlit import write
import json
# Definir variables generales
banner = """
..######..########.########..##.....##.########.########..########.##....##..######..########..##....##.########..########.########.####.##.......########
.##....##.##.......##.....##.##.....##.##.......##.....##.##.......###...##.##....##.##.....##..##..##..##.....##....##....##........##..##.......##......
.##.......##.......##.....##.##.....##.##.......##.....##.##.......####..##.##.......##.....##...####...##.....##....##....##........##..##.......##......
..######..######...########..##.....##.######...########..######...##.##.##.##.......########.....##....########.....##....######....##..##.......######..
.......##.##.......##...##....##...##..##.......##...##...##.......##..####.##.......##...##......##....##...........##....##........##..##.......##......
.##....##.##.......##....##....##.##...##.......##....##..##.......##...###.##....##.##....##.....##....##...........##....##........##..##.......##......
..######..########.##.....##....###....########.##.....##.########.##....##..######..##.....##....##....##...........##....##.......####.########.########
"""
with open("config.json", "r", encoding="utf-8") as jsonconf:
    datajson = json.load(jsonconf)
def bannerfn(show: True = bool):
    print(banner)
    print("Please dont close this terminal meanwhile is encrypt or decrypt a file")
    print("Created by reddark")
bannerfn(datajson["showbanner"])
# Cargar estilo desde css
if datajson["activecss"]:
    with open("styles/cstreamlystyle.css", "r") as stylecss:
        st.markdown(f"<style>{stylecss.read()}</style>", unsafe_allow_html=True)
# Definir estado de login
st.title("Security files server")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# Funcion de login
def login():
    credentialsStatus = False
    #user = st.text_input("user") # Añadir en otro momento
    password= st.text_input("password", type="password")
    if st.button("login"):
        # Abre el archivo cred.txt y compara su contenido con la entrada de texto
        with open("credentialsFiles/cred.txt", "r") as creds:
            content = creds.read()
            if content == password:
                credentialsStatus = True
        # Comprueba la variable credentialsStatus
        if credentialsStatus:
            st.session_state.logged_in = True
            st.rerun()
        else:
            write("cant logged in")
# Funcion de deslogueo
def logout():
    if st.button("logout"):
        st.session_state.logged_in = False
#comprobacion de estado de login
if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [st.Page(logout, title="logout")],
            "Main pages": [st.Page("dashboard.py", title="Main dashboard", default=True), st.Page("logFile.py", title="Server log")]
        }
    )
else:
    pg = st.navigation([st.Page(login, title="login", icon=":material/login:")])
pg.run()
