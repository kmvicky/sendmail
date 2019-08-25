import time
from django.urls import reverse
from sendzip.taskapp.tasks import send_mail
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotFound



class HomePage(TemplateView):

	def get(self, request, *args, **kwrgs):

		self.template_name = 'zipfile/zipfile.html'
		
		try:
			context = {
				'action': reverse('zipfile:homepage')
			}

			return self.render_to_response(context)

		except Exception as e:
			raise e


	def post(self, request, *args, **kwrgs):

		self.template_name = 'zipfile/zipfile.html'
		
		try:
			
			data = request.POST.dict()

			urls = data.get('urls', None)

			email = data.get('email', None)

			if not email and not urls:
				return HttpResponseNotFound('Email and urls are mandatory')

			urls = urls.split(',')

			params = {
				'urls': urls,
				'email': email
			}
			
			send_mail.delay(**params)

			return JsonResponse(context)
		
		except Exception as e:
			return HttpResponseNotFound(str(e))