import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': "https://console.firebase.google.com/project/healthcare-4bee0/database/healthcare-4bee0-default-rtdb/data/~2F"
	})