from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .signup import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def register(request):
	if request.method=='POST':
		user = UserRegisterForm(request.POST)
		if user.is_valid():
			username = user.cleaned_data.get('username')
			mail=user.cleaned_data.get('email')
			if email_verify(mail):
                                user.save()
                                messages.success(request, f'Account has been created for {username}! Please login to continue')
			else:
                                messages.warning(request,f'Your account couldn\'t be created.....Only Somaiya students are allowed')
                                return redirect('user-register') 
			return redirect('project-home')
	else:
		user = UserRegisterForm()
	return render(request,'users/register.html',{'form':user})


def email_verify(email):
	domains = 'somaiya.edu'
	email_domain = email.split('@')[1]
	if email_domain == domains:

		return True
	return False

@login_required
def profile(request):
	##return render(request,'users/profile.html')
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,request.FILES,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account has been updated!')
			return redirect('user-profile')

	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)

	context={
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request,'users/profile.html',context)
