from django.shortcuts import render
from django.http import HttpResponse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import pandas as pd
import re
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')


def remove_invalids(emailid_str):
    emailid_list = emailid_str.split(',')
    valid_email = []
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    for emailid in emailid_list:
        if(re.search(regex,emailid)):
            valid_email.append(emailid) 
    return valid_email



def parse_input(request):
    if request.method == 'POST':
        recipients_str = (request.POST['r_ids'])
        subject = (request.POST['subject'])
        body = (request.POST['body'])
        cc_str = (request.POST['cc'])
        bcc_str = (request.POST['bcc'])

        recipients_list = remove_invalids(recipients_str)
        cc_list = remove_invalids(cc_str)
        bcc_list = remove_invalids(bcc_str)
        result = send_mail(recipients_list, cc_list, bcc_list, subject, body)
        return HttpResponse(result)



def send_mail(recipients_list, cc_list, bcc_list, subject, body):
    if len(recipients_list) == 0:
        return 'All recipients were invalid'
    
    mail = Mail()
    mail.from_email = Email("test@domain.com", "Abhishek")
    mail.subject = subject

    personalization = Personalization()
    for recipient in recipients_list:
        personalization.add_to(Email(recipient))
    for recipient in cc_list:
        personalization.add_cc(Email(recipient))
    for recipient in bcc_list:
        personalization.add_bcc(Email(recipient))
    mail.add_personalization(personalization)
    mail.add_content(Content("text/plain", body))

    try:
        sendgrid_client = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sendgrid_client.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        return 'Error. Please check your mailing list and try again'

    return 'E-mails sent'


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        subject = request.POST['subject']
        body = request.POST['body']
        df = pd.read_csv(file)
        recipients_list = df.['to']
        cc_list = df.['cc']
        bcc_list = df.['bcc']

        recipients_list = remove_invalids(recipients_str)
        cc_list = remove_invalids(cc_str)
        bcc_list = remove_invalids(bcc_str)
        result = send_mail(recipients_list, cc_list, bcc_list, subject, body)
        return HttpResponse(result)
        