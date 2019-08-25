from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
from django.apps import AppConfig


if not settings.configured:
	# set the default Django settings module for the 'celery' program.
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')


app = Celery('sendzip')


class CeleryConfig(AppConfig):

	name = 'sendzip.taskapp'
	verbose_name = 'Celery Config'

	def ready(self):
		app.config_from_object('django.conf:settings', namespace='CELERY')
		app.autodiscover_tasks(['sendzip.taskapp'])


@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))  # pragma: no cover