import re, os, json


dev = [
		'Python', 'Django', 'HTML', 'CSS', 'Javascript', 'JS', 'backend', 'frontend',
		'Github', 'full-stack', 'full stack', 'gunicorn', 'nginx', 'postgresql', 'AWS',
		'digital ocean', 'scripting', 'startup'
		]

cv = [ 
		'Image', 'processing', 'DIP', 'CV', 'computer', 'vision', 'recognition',
		'machine', 'learning','segmentation', 'feature', 'extraction', 'python', 'scikit', 
		'sci-kit', 'matlab'
		]

def _get_rate(job_dict, file_path):
	# num=str(len(os.listdir('../downloads'))-1)
	# print(num)
	with open(file_path, 'r') as f:
		job_list = json.load(f)
	f.close()

	rate_dev = 0
	rate_cv = 0
	exp = job_dict['discription']
	for skill in dev:
		if skill in exp:
			rate_dev += 1
	for skill in cv :
		if skill in exp :
			rate_cv += 1
	# return {'rate_dev': rate_dev, 'rate_cv': rate_cv}
	return (rate_dev, rate_cv)

def ratings_list(file_path):
	# num=str(len(os.listdir('../downloads'))-1)
	# print(num)
	with open(file_path, 'r') as f:
		job_list = json.load(f)
	f.close()

	ratings =[]
	for listing in job_list:
		ratings.append(_get_rate(listing, file_path)) 
	return ratings

# print(ratings_list())

