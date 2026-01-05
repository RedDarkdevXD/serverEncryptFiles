#!/bin/bash
function install_dependencies(){
    dependencies=(python3 python3-streamlit python3-cryptograpy)
    if [ "$(id -u)" = "0" ]; then
        for i in "${dependencies[@]}"; do
            apt-get install $i -y
        done
    else
        echo 'Need root for install dependencies with this script'
    fi
}
function make_drectorys(){
    folders=("credentialsFiles" "userFiles" "userFiles/Documents" "userFiles/Pictures" "userFiles/Videos" "userFiles/Music")
    for i in "${folders[@]}"; do
        mkdir $i
        echo 'Folders created'
    done
}
function make_password(){
    echo 'Now create a password for acces in the GUI. If you want it be "password" then only press enter'
    read password
    if [ -z "${password}" ]; then
        printf 'password' > credentialsFiles/cred.txt
    else
        printf "%s" $password > credentialsFiles/cred.txt
    fi
}
function generate_key(){
    echo 'Only press enter if you dont have dependencies installed'
    echo 'Want create a key. Can do this more later from GUI(y or n)'
    read yorn
    if [ $yorn = 'y' ]; then
        python3.12 <<EOF
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("credentialsFiles/main_key.key", "wb") as file:
    file.write(key)
EOF
        echo 'Key created'
    else
        echo 'Key doesnt created'
    fi
}
echo 'Created by reddark'
echo 'This script was tested in Linux Mint system. Its recomended install dependencies manually'
read
sleep 1
install_dependencies
sleep 1
make_drectorys
sleep 1
make_password
sleep 1
generate_key
echo 'Now execute "streamlit run streamlit_app.py" in the app directory for start frond end'
