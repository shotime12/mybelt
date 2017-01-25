from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt

# Create your models here.
class UserManager(models.Manager):
	def register(self, request):
		#get the values from the form
		is_valid = True

		if len(request.POST['first_name']) == 0:
			messages.error(request, 'First Name is required')
			is_valid = False

		if len(request.POST['last_name']) == 0:
			messages.error(request, 'Last Name is required')
			is_valid = False

		if len(request.POST['email']) == 0:
			messages.error(request, "E-mail is required")
			is_valid = False

		email_match = User.objects.filter(email=request.POST['email'])
		

		if len(email_match) > 0:
			messages.error(request, "That email is already in use")
			is_valid = False

		if len(request.POST['password']) == 0:
			messages.error(request, 'Password is required')
			is_valid = False

		if request.POST['password'] != request.POST['password2']:
			messages.error(request, "Passwords don't match")
			is_valid = False

		if not is_valid:
			return False
		#validate the form
		#make sure email is not already in use

		#hash the password
		hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
		print hashed
		new_user = User(
			first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			email = request.POST['email'],
			password = hashed,
			)
		new_user.save()
		print new_user.id

		request.session['logged_in_user'] = new_user.id
		return True
		#put in the database
	def login(self, request):
		is_valid =True

		users = User.objects.filter(email=request.POST['email'])

		if len(users)==0:
			messages.error(request, "That user does not exist");
			return False
		user = users[0]
		#print user.password
		encrypt_pass = bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8'))
		if encrypt_pass != user.password:
			messages.error(request, "incorrect password")
			return False
		
		request.session['logged_in_user'] = user.id
		
		return True

class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length =100)
	password = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()
