import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def send_mail(recepient_id, template, resume_file):
	EMAIL = ''
	PASSWORD = ''
	msg = MIMEMultipart()
	msg['From']= EMAIL
	msg['To']=recepient_id
	msg['Subject'] = "Regarding: An Opening for Developer position"
	body= template
	msg.attach(MIMEText(body, 'plain'))

	filename= "Resume.pdf"
	attachment= open(resume_file, "rb")


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
	print('Sending mail to: {}'.format(recepient_id))
	smtpObj.sendmail(EMAIL, recepient_id, text)
	smtpObj.quit()

# send_mail('', 'template')