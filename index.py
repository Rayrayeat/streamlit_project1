import streamlit as st

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account.
app = None
db = None
if db is None :
    print("建立firestore實體")
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    if app is None:
        app = firebase_admin.initialize_app(cred)
    db = firestore.client()


st.title("光線和距離及時監控")



def downloadData():
    print("下載資料")