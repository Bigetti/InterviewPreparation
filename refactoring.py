import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PostWork:

    def __init__(self, smtp, imap, login, password, subject, recipients, message, header=None):
        self.smtp = smtp
        self.imap = imap
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header


    def send_message(self):

        #send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())
        ms.quit()
        #send end


    def receive_message(self):
        #recieve
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        #end recieve



if __name__ == '__main__':

    smtp_server = "smtp.gmail.com"
    imap_server = "imap.gmail.com"
    email_login = 'login@gmail.com'
    email_password = 'qwerty'
    email_subject = 'Subject'
    email_recipients = ['vasya@email.com', 'petya@email.com']
    email_message = 'Message'

    postwork = PostWork(smtp_server, imap_server, email_login, email_password, email_subject, email_recipients, email_message)

        # Отправка сообщения
    postwork.send_message()

        # Получение сообщения
    postwork.receive_message()