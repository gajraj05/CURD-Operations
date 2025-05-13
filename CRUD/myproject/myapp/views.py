from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from bson.objectid import ObjectId

def index(request):
    if request.method == 'POST':
        data = {
        'username' : request.POST.get('username'),
        'password' : request.POST.get('password'),
        }

        user.insert_one(data)
        return redirect('/details/')
        
    return render(request, 'index.html')


def details(request):
    if request.method == 'POST':
        note = {
            'name' : request.POST.get('name'),
            'phone' : request.POST.get('phone'),
            'address' : request.POST.get('address'),
            'city' : request.POST.get('city'),
            'state' : request.POST.get('state'),
            'country' : request.POST.get('country'),
        }
        notes.insert_one(note)
        return redirect('/details/')
    
    # Create a list and add 'id' field
    all_notes = []
    for note in notes.find():
        note['id'] = str(note['_id']) 
        all_notes.append(note)

    return render(request, 'details.html', context={
        'notes': all_notes
    })


def update_note(request, id):
    if request.method == 'POST':
        updated_data = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'address': request.POST.get('address'),
            'city': request.POST.get('city'),
            'state': request.POST.get('state'),
            'country': request.POST.get('country'),
        }
        notes.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
        return redirect('/details/')
    
    note = notes.find_one({'_id': ObjectId(id)})
    return render(request, 'update.html', {'note': note})


def delete_note(request, id):
    notes.delete_one({'_id': ObjectId(id)})
    return redirect('/details/')
