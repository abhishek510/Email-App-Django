from django.shortcuts import render
from django.http import HttpResponse
import re


# Create your views here.

def home(request):
    return render(request, 'home.html')


def convert_str_to_list(string1):
    result_list = string1.split(',')
    return result_list


def remove_invalids(emailid_list):
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

        recipients_list = convert_str_to_list(recipients_str)
        cc_list = convert_str_to_list(cc_str)
        bcc_list = convert_str_to_list(bcc_str)

        recipients_list = remove_invalids(recipients_list)
        cc_list = remove_invalids(cc_list)
        bcc_list = remove_invalids(bcc_list)

        if len(recipients_list) == 0:
            return HttpResponse('<h1>All recipients were invalid</h1>')
        
