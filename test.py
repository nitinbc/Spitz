# import re
# def check_id(mail_id):
# 	emailRegex = re.compile(r'''(
# 		[a-zA-Z0-9._%+-]+
# 		@
# 		[a-zA-Z0-9.-]+
# 		(\.[a-zA-Z]{2,4})
# 		)''', re.VERBOSE)
	
# 	# print(var)
# 	return not (emailRegex.search(mail_id) == None) 


import os, json
from io import StringIO
from scraper.shine_scrape import search_shine
from email_gmail.build_template import build
from email_gmail.getVerifyCreds import get_email_id, check_id
from match_tools.re_tool import ratings_list
from email_gmail.send_mail import send_mail

num=str(len(os.listdir('downloads'))-2)
file_path = 'downloads/shine_'+num+'.json'
resume_file = 'Files/Resume.pdf'
template_path = 'email_gmail/template.json'

my_mail_list =[]
for i in range(20):
	mail_id = get_email_id(i, file_path).split()[0]
	if check_id(mail_id):
		my_mail_list.append(mail_id)
# print(my_mail_list)
# # for ids in range(2,len(my_mail_list)):
# # 	print(my_mail_list[ids])
# for mail_id in my_mail_list:
# 	if not mail_id=='shraddhak@pskindia.com' and not mail_id=='imdevisingh@gmail.com':
# 		print(mail_id)

print(file_path)
ratings = ratings_list(file_path)
print(ratings)
print(my_mail_list)
# sent_to = ['riyav@headhuntershr.com', 'hetsi@brconsultancy.in','amruta@pskindia.com', 'hetsi@brconsultancy.in',
# 			'forjobcv@gmail.com', 'welcomehr2@gmail.com', 'talent@iallp.in', 'websoljobs@gmail.com',
# 			'narayan.shapuram@anantha.co.in', 'forjobcv@gmail.com', 'hetsi@brconsultancy.in','monica.honeybeezconsultancy@gmail.com',
# 			'shinejobs@thinkvidya.com','tejal.shah@mcx.com', 'atul.kumar@globaledgesoft.com', 'arun.d@exploitinfo.com',
# 			'hr@axnesstech.com', 'info@newparameter.com', 'lizelle.desouza@wisseninfotech.com', 'info@newparameter.com',
# 			'forjobcv@gmail.com', 'rayinfochn@brraysoft.com','tejakumar@patent-art.com', 'hr@binstech.in', 'deepti@peshr.com',
# 			'info@newparameter.com', 'hetsi@brconsultancy.in', 'kalpana80us@gmail.com', 'arun.d@exploitinfo.com','msowmya@magazinemanager.com',
# 			'shital.j@growelsoftech.com']

# print(len(sent_to))
# sent_to_set = set(sent_to)
# sent_to_list = list(sent_to_set)
# print(len(sent_to_list))
# with open('sent_to.json', 'a+') as f:
# 	io = StringIO()
# 	json.dump(sent_to_list, io, sort_keys=True, indent=4, separators=(',', ': '))
# 	f.write(io.getvalue())
# f.close()