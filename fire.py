from firebase import firebase
firebase = firebase.FirebaseApplication('https://auxilium-android.firebaseio.com/', None)
result = firebase.get('/reports', None)
print(result)
