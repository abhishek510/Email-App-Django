# Email-App-Django
Email sending application in django using Sendgrid api and logging through ELK stack  

Launch with $python manage.py runserver and go to localhost:8000, the application supports csv upload of format  
<pre>
to                  | cc                         | bcc  
--------------------|----------------------------|-----------------  
example@example.com | example1@example.com       |example2@example.com  
example4@example.com| example5@example.com       |example6@example.com  
</pre>

Create an account on https://sendgrid.com/ and create an API key and set it to an environmental variable 
export SENDGRID_API_KEY='your key here'  
A cronjob that runs every 30 minutes will send the admin(can be found at EmailSender/cron.py) an email with the mail statistics of the day.  

setup dependencies using:  
$pip install requirements.txt  

To setup ELK stack install docker and docker compose and use the repository : https://github.com/deviantony/docker-elk  
$ git clone https://github.com/deviantony/docker-elk  
$ cd docker-elk  
$ sudo docker-compose up -d  
(all 3 container should be up now)  

follow the link to configure django logs to go to logstash:  
https://www.codementor.io/@samueljames/using-django-with-elasticsearch-logstash-and-kibana-elk-stack-9l4fwx138  

