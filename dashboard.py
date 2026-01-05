#import libraries
import encryptFunctions as fn
import streamlit as st
from streamlit import write
import otherFunctions as ofn
st.header("Main dashboard")
write("For generate a key push this button")
if st.button("Generate key"):
    status = fn.generate_key()
write("For encrypt folders in userfiles folder push this button(The folders must be specified in the JSON list):")
if st.button("Encrypt folders"):
    status = fn.encrypt_folders()
    write(status)
write("For decrypt folders in userfiles folder push this button(The folders must be specified in the JSON list):")
if st.button("Decrypt folders"):
    status = fn.decrypt_folders()
    write(status)
write("For check status folders push this button")
if st.button("Check status"):
    ofn.check_status_folders()