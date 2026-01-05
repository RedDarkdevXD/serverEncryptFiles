import streamlit as st
from streamlit import write
import json
import os
with open("config.json", "r", encoding="utf-8") as jsonconf:
    datajson = json.load(jsonconf)
st.header("Server log file")
write("For clean log file push this button(this remove all log)")
if datajson["candellog"]:
    if st.button("Delete log"):
        os.remove("logFile.log")
else:
    write("candellog is false then you cannot delete log file")
if os.path.exists("logFIle.log"):
    with open("logFIle.log", "r") as logFile:
        if datajson["candowlog"]:
            st.download_button("Download logfile", logFile.read(), "logFile.log")
        st.code(logFile.read())
