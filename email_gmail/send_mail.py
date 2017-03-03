import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

EMAIL = ''
PASSWORD = ''

def send_mail(recepient_id, template):

	msg = MIMEMultipart()
	msg['From']= EMAIL
	msg['To']=recepient_id
	msg['Subject'] = "Regarding: An Opening for Developer position"
	body="My message for now" + template
	msg.attach(MIMEText(body, 'plain'))

	filename= "Resume.pdf"
	attachment= open('../Files/Resume.pdf', "rb")


	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename =%s" %filename)
	msg.attach(part)

	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(EMAIL, PASSWORD)
	text = msg.as_string()
	smtpObj.sendmail(EMAIL, recepient_id, text)
	smtpObj.quit()

send_mail('', 'template')