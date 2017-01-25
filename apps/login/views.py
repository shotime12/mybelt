from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
	context = {
	"users": User.objects.all()
	}

	return render(request, 'login/index.html', context)


def register(request):
	#get the values from the form
	#print(request.POST['first_name'])
	did_register = User.objects.register(request)

	if did_register:
		#User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'] )
		#print request.POST['first_name']
		return redirect('/dashboard')
	else:
		return redirect('/login')

	
	print request.POST['first_name']

	return redirect('/login')

def login(request):
	did_login = User.objects.login(request)
	#print did_login
	if did_login:
		#print "works"
		return redirect('/dashboard')
	else:
		return redirect('/login')
