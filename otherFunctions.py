#import libsrarys
import os
import json
from streamlit import write
with open("config.json", "r", encoding="utf-8") as jsonconf:
    datajson = json.load(jsonconf)
folders = datajson["folders"]
def save_log(msg):
    if datajson["savelog"]:
        with open("logFIle.log", "a") as logFile:
            logFile.write(f"{msg}\n")
def check_status_folders():
    with open("credentialsFiles/main_key.key", "rb") as keyFile:
        write(f"actual key: {keyFile.read()}")
        save_log(f"actual key: {keyFile.read()}")
    for i in folders:
        try:
            if os.path.exists(f"userFiles/{i}"):
                save_log(f"{i} folder exist and is not encrypted")
                write(f"{i} folder exist and is not encrypted")
        except Exception as e:
            save_log(e)
    for i in folders:
        try:
            if os.path.exists(f"userFiles/{i}.zip"):
                save_log(f"{i}.zip file exist, its compressed but its not encrypted")
                write(f"{i}.zip file exist, its compressed but its not encrypted")
        except Exception as e:
            save_log(e)
    for i in folders:
        try:
            if os.path.exists(f"userFiles/{i}.zip.encrypted"):
                save_log(f"{i}.zip.encrypted file exist and its encrypted")
                write(f"{i}.zip.encrypted file exist and its encrypted")
        except Exception as e:
            save_log(e)
