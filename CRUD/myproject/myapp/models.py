from django.db import models

# Create your models here.
from mongodb import database

user = database['user']
notes = database['notes']