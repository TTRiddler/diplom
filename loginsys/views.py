from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def login(request):
	args = {}
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if username and password:
			if user is not None:
				auth.login(request, user)
				return redirect('/')
			else:
				args['login_error'] = "Неправильно введен логин/пароль"
				return render(request, 'loginsys/login.html', args)
		else:
			args['login_error'] = "Введите логин/пароль"
			return render(request, 'loginsys/login.html', args)
	else:
		return render(request, 'loginsys/login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            if form.cleaned_data.get('teachers_key') == "ZQUsqDot":
            	user.profile.teachers_key = True
            else:
            	user.profile.teachers_key = False
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'loginsys/signup.html', {'form': form})