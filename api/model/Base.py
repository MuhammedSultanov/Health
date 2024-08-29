#!/usr/bin/python3

"""Importing libraries for configuring datetime and Firebase"""
import uuid
from datetime import datetime
from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self, collection_name):
        """Method to update updated_at timestamp and save the instance to Firestore"""
        self.updated_at = datetime.now()
        
        doc_ref = db.collection(collection_name).document(self.id)
        doc_ref.set({
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })