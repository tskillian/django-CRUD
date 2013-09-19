
from django.shortcuts import render
from django.http import HttpResponseRedirect

from manage_users.models import Users, UserForm

def index(request):
	first_names = []
	last_names = []
	emails = []
	for i in Users.objects.all():
		first_names.append(i.user_first_name)
		last_names.append(i.user_last_name)
		emails.append(i.email_address)

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			users_obj = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	return render(request, 'home.html', {
		'form': form, 'first_names': first_names
		})




