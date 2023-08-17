from django.shortcuts import render, redirect
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import os

config = {
  apiKey: "AIzaSyCjUOfSfmBdwXeAtIQ1BG9WWIKfR2OT7Bs",
  authDomain: "fir-django-690e1.firebaseapp.com",
  projectId: "fir-django-690e1",
  storageBucket: "fir-django-690e1.appspot.com",
  messagingSenderId: "673967078390",
  appId: "1:673967078390:web:46e5138b40122201c0e5d7"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_save = default_storage.save(file.name, file)
        storage.child("files/" + file.name).put("media/" + file.name)
        delete = default_storage.delete(file.name)
        messages.success(request, "File upload in Firebase Storage successful")
        return redirect('main')
    else:
        return render(request, 'main.html')
