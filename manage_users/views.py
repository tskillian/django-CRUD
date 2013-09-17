from django.http import HttpResponse
from django.template import RequestContext, loader

from manage_users.models import Users


def index(request):
	#return render(request, 'home.html')

	users_list = Users.objects.order_by('-user_last_name')
	template = loader.get_template('home.html')
	context = RequestContext(request, {
		'users_list': users_list,
		})
	return HttpResponse(template.render(context))

