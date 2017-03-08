import os, json, re


def get_email_id(key_arg, file_path):

	# num=str(len(os.listdir('../downloads'))-1)
	with open(file_path, 'r') as f:
		job_list = json.load(f)
	f.close()


	email_id="contact not found"
	dict_job = job_list[key_arg]
	experience = dict_job['experience'].split(" ")
	if int(experience[0]) in (0,1, 2) :
		for item in dict_job['contact_details']:
			if 'Email:' in item:
				email_id=item[7:]	
	else:
		email_id = "Experiance not matched"
	return email_id

	
def check_id(mail_id):
	emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+
		@
		[a-zA-Z0-9.-]+
		(\.[a-zA-Z]{2,4})
		)''', re.VERBOSE)
	return not (emailRegex.search(mail_id) == None) 





