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
num=str(len(os.listdir('../downloads'))-1)
with open('../downloads/'+'shine_'+num+'.json', 'r') as f:
	job_list = json.load(f)
f.close()


def get_experiance(job_dict):
	exp = job_dict['experiance']
	