#!/usr/bin/python3

from datetime import datetime
from model.Base import BaseModel
from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

class HealthRecord(BaseModel):
    def __init__(self, user_id, date=None, water_intake=None, sleep_duration=None, exercise_activities=None, custom_metrics=None):
        super().__init__()
        self.user_id = user_id
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.water_intake = water_intake
        self.sleep_duration = sleep_duration
        self.exercise_activities = exercise_activities
        self.custom_metrics = custom_metrics if custom_metrics else {}

    def to_dict(self):
        """Convert the HealthRecord object to a dictionary, including record-specific fields"""
        data = super().to_dict()
        data.update({
            'user_id': self.user_id,
            'date': self.date,
            'water_intake': self.water_intake,
            'sleep_duration': self.sleep_duration,
            'exercise_activities': self.exercise_activities,
            'custom_metrics': self.custom_metrics
        })
        return data

    def save_to_firestore(self):
        """Save the HealthRecord instance to Firestore"""
        record_ref = db.collection('health_records').document(self.user_id).collection('records').document(self.date)
        record_ref.set(self.to_dict())
