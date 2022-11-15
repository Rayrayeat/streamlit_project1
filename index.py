import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import pandas as pd

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

records_ref = db.collection('records')
query = records_ref.limit_to_last(20)
docs = query.get()

datalist = [doc.to_dict() for doc in docs]
dict_data = pd.DataFrame(datalist)

st.title("光線和距離及時監控")
st.table(dict_data)



def downloadData():
    print("下載資料")