import sendzip.zipfile.views as views

from django.urls import include, path, re_path

app_name = 'zipfile'

urlpatterns = [
	
	path('', 
		views.HomePage.as_view(),
		 name='homepage'),
]