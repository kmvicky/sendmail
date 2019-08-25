from django.apps import AppConfig

class ZipfileConfig(AppConfig):

	name = 'sendzip.zipfile'
	verbose_name = 'zipfile'

	def ready(self):
		pass