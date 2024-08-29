import firebase_admin
from firebase_admin import db, credentials
import json

# Initialize Firebase app with service account
cred_obj = credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': "https://newhealth-f6c05-default-rtdb.firebaseio.com/"  # Replace with your actual database URL
})

