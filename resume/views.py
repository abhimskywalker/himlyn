from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'resume/index.html')

def signup_page(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == "POST":
		password = request.POST["passwd"]    
        email = request.POST["email"]

        user_create = User.objects.create_user(username=email, email=email, password=password)
        user_create.is_active = True
        user_create.save()
        return HttpResponseRedirect('/signup-done/')