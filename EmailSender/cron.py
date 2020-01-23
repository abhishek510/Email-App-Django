from emailservice.models import MailList
from emailservice.views import send_mail
import datetime

def notify_admin():
    today_date = datetime.date.today()
    today_datetime = datetime.datetime.combine(today_date, datetime.time())
    mails = MailList.objects.filter(time__gt = today_datetime)
    result = ""
    for mail in mails:
        result += "time = "+mail.time
        result += "subject = "+mail.email_subject
    
    message = send_mail(['abhishekdwi.05@gmail.com'], None, None, "Daily Usage", result)
