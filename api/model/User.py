#!/usr/bin/python3

from datetime import datetime
from model.Base import BaseModel
from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

class User(BaseModel):
    def __init__(self, email, password, first_name, last_name, is_admin=False):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin

    def to_dict(self):
        """Convert the User object to a dictionary, including user-specific fields"""
        data = super().to_dict()
        data.update({
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return data