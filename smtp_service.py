#!/usr/bin/python
import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.charset import Charset, BASE64
from email.mime.nonmultipart import MIMENonMultipart
from email import charset
from email import Encoders

class Mailer:
    def __init__(self):
        self.sender = config.smtp_ini['sender']
        self.receipant = config.smtp_ini['receipant']
        self.server = config.smtp_ini['server']
        self.port = config.smtp_ini['port']
        self.tls = config.smtp_ini['tls']
        self.login = config.smtp_ini['login']
        self.subject = config.smtp_ini['subject']
        self.password = config.password['pw']
        charset.add_charset('utf-8', charset.SHORTEST, charset.QP)
    def send_report(self, date, short_description, additional_description, title, _filename):
        full_email = MIMEMultipart('mixed')
        full_email['Subject'] = date + " " + self.subject
        full_email['From'] = self.sender
        full_email['To'] = self.receipant
        email_addresses = self.receipant.split(',')
        # CSV FILE 
        attachment = MIMENonMultipart('html', 'csv', charset='utf-8')
        attachment.add_header('Content-Disposition', 'attachment', filename=_filename)
        attachment.set_payload(open(_filename, "rb").read())
        full_email.attach(attachment)
        # HTML TABLE
        body = MIMEMultipart('alternative')
        body.attach(MIMEText((short_description + additional_description).encode('utf-8'),
                             'html', _charset='utf-8'))
        body.attach(MIMEText(("""\
                                <html>
                                  <head></head>
                                  <body>
                                    <div style="text-align:center">
                                        <strong>
                                            <h1><font color="red">""" + title + """</font></h1>
                                            <h4>""" + short_description + additional_description + """</h4>
                                        </strong>
                                    </div>
                                  </body>
                                </html>
                                """).encode('utf-8'),
                             'html', _charset='utf-8'))
        full_email.attach(body)        
        s = smtplib.SMTP(self.server, self.port)
        if self.tls == 'yes':
            s.starttls()
        if not self.login == '':
            s.login(self.login, self.password)
        try:
            s.sendmail(self.sender, email_addresses, full_email.as_string())
            s.quit()
        except SMTPException as e:
            print "ERROR %d: %s" % (e.args[0], e.args[1])
