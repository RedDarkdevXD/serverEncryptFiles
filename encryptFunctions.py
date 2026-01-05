#import librarys
from cryptography.fernet import Fernet
import zipfile
import shutil
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
def generate_key():
    try:
        existsFilesList = []
        for i in folders:
            if os.path.exists(f"userFiles/{i}.zip.encrypted"):
                existsFilesList.append(f"{i}.zip.encrypted", )
        save_log(existsFilesList)
        if not existsFilesList:
            if os.path.exists("credentialsFiles/main_key.key"):
                os.remove("credentialsFiles/main_key.key")
                save_log("Last key deleted")
            key = Fernet.generate_key()
            save_log("Key generate")
            with open("credentialsFiles/main_key.key", "wb") as file:
                file.write(key)
            save_log("Key saved")
            write("File with key created succesfull")
        else:
            write("There files encrypted with before key")
            save_log("There files encrypted with before key")
    except Exception as e:
       save_log(e)
def encrypt_folders():
    # Check exist folders and files
    for i in folders:
        userFoldersStatus = os.path.exists(f"userFiles/{i}")
        folderFilesStatus = os.path.exists(f"userFiles/{i}/dontdelete.svrcr")
        if not userFoldersStatus:
            save_log(f"{i} folder dont exist")
            os.mkdir(f"userFiles/{i}")
            with open(f"userFiles/{i}/dontdelete.svrcrf", "w") as dontrm:
                dontrm.write("Dont delete this file or the directory dont decrypt correct")
            save_log(f"{i} folder created with dontdelete file")
        elif not folderFilesStatus:
            with open(f"userFiles/{i}/dontdelete.svrcrf", "w") as dontrm:
                dontrm.write("Dont delete this file or the directory dont decrypt correct")
            save_log(f"{i}/dontdelete.svrcrf file created")
    # Load key
    try:
        with open("credentialsFiles/main_key.key", "rb") as filekey:
            key = filekey.read()
        f = Fernet(key)
        save_log("Llave cargada")
    except Exception as e:
        save_log(e)
    # Comprim folders
    for i in folders:
        try:
            shutil.make_archive(
                f"userFiles/{i}",
                "zip",
                root_dir=f"userFiles/{i}",
                base_dir="."
                )
            save_log(f"{i}.zip file created")
        except Exception as e:
            save_log(e)
    # Read zip, encrypt, save encripted file 
    for i in folders:
        try:
            with open(f"userFiles/{i}.zip", "rb") as file:
                data = file.read()
            encrypted_data = f.encrypt(data)
            with open(f"userFiles/{i}.zip.encrypted", "wb") as file:
                file.write(encrypted_data)
            save_log(f"{i} folder encrypted successfull")
        except Exception as e:
            save_log(e)
    # Delete original directorys and zip files
    for i in folders:
        if os.path.exists(f"userFiles/{i}.zip.encrypted"):
            shutil.rmtree(f"userFiles/{i}")
            save_log(f"{i} folder deleted")
            os.remove(f"userFiles/{i}.zip")
            save_log(f"{i}.zip file deleted")
    save_log("Archivos encriptados")
    return "The folders are encrypted"
def decrypt_folders():
    # Load key
    with open("credentialsFiles/main_key.key", "rb") as file:
        key = file.read()
    f = Fernet(key)
    save_log("Key loaded")
    # Decrypt .encrypted files
    for i in folders:
        encFileStatus = os.path.exists(f"userFiles/{i}.zip.encrypted")
        if encFileStatus:
            with open(f"userFiles/{i}.zip.encrypted", "rb")as fileenc:
                dataenc = fileenc.read()
                datadec = f.decrypt(dataenc)
                save_log(f"{i}.zip.encrypted file opened and decrypted")
        with open(f"userFiles/{i}.zip", "wb")as filedec:
            filedec.write(datadec)
            save_log(f"{i}.zip saved")
    # Unzip files
    for i in folders:
        with zipfile.ZipFile(f"userFiles/{i}.zip", "r") as filezip:
            filezip.extractall(f"userFiles/{i}")
            save_log(f"{i}.zip unziped")
    # Delete files
    for i in folders:
        if os.path.exists(f"userFiles/{i}") and not "." in i:
            os.remove(f"userFiles/{i}.zip.encrypted")
            save_log(f"{i}.zip.encrypted file deleted")
            os.remove(f"userFiles/{i}.zip")
            save_log(f"{i}.zip file deleted")
        else:
            save_log(f"userFiles/{i} dont exist. file associated not deleted")
            write(f"Folder {i} dont found")
    save_log("Files decrypted succesfull")
    return "The folders are decrypted"    
