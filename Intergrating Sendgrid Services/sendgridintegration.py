Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
... from sendgrid import SendGridAPIClient
... from sendgrid.helpers.mail import Mail
... 
... message = Mail(
...     from_email='adhilahamed492@gmail.com',
...     to_emails='abikeshak@gmail.com',
...     subject='Sending with Twilio SendGrid is Fun',
...     html_content='<strong>and easy to do anywhere, even with Python</strong>')
... try:
...     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
...     response = sg.send(message)
...     print(response.status_code)
...     print(response.body)
...     print(response.headers)
... except Exception as e:
