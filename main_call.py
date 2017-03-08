import os, json
from scraper.shine_scrape import search_shine
from email_gmail.build_template import build
from email_gmail.getVerifyCreds import get_email_id, check_id
from match_tools.re_tool import ratings_list
from email_gmail.send_mail import send_mail
from io import StringIO

# num=str(len(os.listdir('downloads'))-1)
# file_path = 'downloads/shine_'+num+'.json'
# resume_file = 'Files/Resume.pdf'
template_path = 'email_gmail/template.json'

# search_shine('https://www.shine.com/job-search/python-django-jobs-in-mumbai-pune-hyderabad-9', file_path=file_path)

num=str(len(os.listdir('downloads'))-2)
file_path = 'downloads/shine_'+num+'.json'
# list_of =[]
print(file_path)

# with open('sent_to.json', 'r') as f:
# 	sent_to_list = json.load(f)
# f.close()

ratings = ratings_list(file_path)
for index, rate in enumerate(ratings):
	if rate[0]+rate[1]>=4:
		mail_id = get_email_id(index, file_path).split()[0]
		flag=False
		# if mail_id in sent_to_list:
		# 	flag = False
		if (not flag) and check_id(mail_id):
			template = build(ratings[index], template_path)
			# send_mail(mail_id, template, resume_file)
			# sent_to_list.append(mail_id)
			print(mail_id)
			print(template)
	
# print(file_path)

# with open('sent_to.json', 'w+') as f:
# 	io = StringIO()
# 	json.dump(sent_to_list, io, sort_keys=True, indent=4, separators=(',', ': '))
# 	f.write(io.getvalue())
# f.close()







		

