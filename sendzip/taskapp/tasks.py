import os
import json
import logging
from zipfile import ZipFile

from sendzip.taskapp.celery import app
from datetime import datetime, timedelta
from django.template.context import Context
from django.core.mail import EmailMultiAlternatives

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen

		
import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders


@app.task()
def create_zip(urls):

	directory = 'downloadedfiles'

	if not os.path.exists(directory):
		os.makedirs(directory)

	file_paths = list()

	for idx, url in enumerate(urls):
		html = urlopen(url).read()
		
		with open('downloadedfiles/{}.html'.format(str(idx+1)), 'wb') as out_file:
			out_file.write(html)


	try:
		# Gel all the files in the directory
		for root, directories, files in os.walk(directory):
			for file in files:
				file_path = os.path.join(root, file)
				file_paths.append(file_path)
		
		# Create zip file
		with ZipFile('files.zip','w') as output_file:
			for file in file_paths:
				output_file.write(file)
	except Exception as e:
		print(e)


@app.task()
def send_mail(**kwargs):

	try:
		urls = kwargs.get('urls')
		sender_email = 'kmvicky1994@gmail.com'
		receiver_email = kwargs.get('email')
		password = '8058756021++'

		message = MIMEMultipart("alternative")
		message["Subject"] = "multipart test"
		message["From"] = sender_email
		message["To"] = receiver_email

		# Create the plain-text and HTML version of your message
		text = '''Hello, Please find the attached zip file'''

		# Turn these into plain/html MIMEText objects
		part1 = MIMEText(text, "plain")

		create_zip.delay(urls)

		part2 = MIMEBase('application', 'octet-stream')
		part2.set_payload(open('files.zip', 'rb').read())
		encoders.encode_base64(part2)
		part2.add_header('Content-Disposition', 'attachment; filename=files.zip')

		message.attach(part1)
		message.attach(part2)

		# Create secure connection with server and send email
		# context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
				server.login(sender_email, password)
				server.sendmail(
						sender_email, receiver_email, message.as_string()
				)


		directory = 'downloadedfiles'

		# Remove all the files in the directory
		for root, directories, files in os.walk(directory):
			for file in files:
				file_path = os.path.join(root, file)
				os.remove(file_path)

	except Exception as e:
		print(e)

	

