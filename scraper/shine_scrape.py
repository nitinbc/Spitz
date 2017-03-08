""" This script will scrape job particular data from shine.com.
All the collected data is saved in downloads folder for further 
processing."""

import requests, bs4, os, time, json
from io import StringIO

os.makedirs('../downloads', exist_ok=True)

def get_webpage_by_params(key_word, places):

	"""Takes 2 strings, each of them space seperated independently
	and returns page containing list of jobs and their links"""
	
	base_url_string = 'https://www.shine.com/job-search/'
	url_string = base_url_string + '-'.join(key_word.lower().split()) + '-jobs-in-' + '-'.join(places.lower().split())

	web_page = requests.get(url_string)
	
	try:
		web_page.raise_for_status()
	except Exception as exc:
		print ("Are key_word and Places, space seperated Strings?")
		print("There was a problem: %s" %exc)
	
	return web_page

def get_webpage_by_link(url):
	valid_link = "https://www.shine.com"
	if not valid_link in url:
		print("link is not valid")
		return
	else:
		web_page = requests.get(url)
		try:
			web_page.raise_for_status()
		except Exception as exc:
			print("There was a problem: %s" %exc)
		return web_page


def get_post_links(web_page):
	"""Takes in web_page. Extracts links to seperate job pages from 
	give page list"""
	soup_of_page = bs4.BeautifulSoup(web_page.text, "html.parser")
	job_list_element = soup_of_page.select('.cls_searchresult_a')
	links_to_page = []
	for i in job_list_element:
		links_to_page.append(i.get('href')) 
	return links_to_page

def get_job_detail(links_to_page, file_path):
	"""Goes to 'job-detail page' and downloads relevent info. Saves
	them to file in json  """
	
	url = 'https://www.shine.com'

	# target_folder = '../downloads/'
	# num = len(os.listdir('../downloads')) 
	list_to_json =[]
	# file_name = 'shine_'+str(num)+'.json'
	file_name = file_path
	count = 0
	for link in links_to_page:
		count += 1
		job_url = url + link
		post_page = requests.get(job_url)
		soup_of_post = bs4.BeautifulSoup(post_page.text, "html.parser")

		detail_dict ={}

		try:
			company_name = soup_of_post.findAll('span', {'itemprop':'hiringOrganization'})[0].getText()
		except:
			company_name = "Not Available or Hidden"

		
		posted_date = soup_of_post.select('.jobDate')[0].getText()
		experience = soup_of_post.findAll("span", {"itemprop":"experienceRequirements"})[0].getText()
		place = soup_of_post.select('.jd_location')[0].getText()
		discription = soup_of_post.select('pre')[0].getText()
		contact = soup_of_post.select('.cls_rect_detail_div li')
		contact_details = [contact[i].getText() for i in range(len(contact))]

		detail_dict = { "company_name":company_name,
						"posted_date": posted_date,
						"experience":experience,
						"place":place,
						"discription":discription,
						"contact_details":contact_details}

		list_to_json.append(detail_dict)
		print("Saving Job Details, json dump way")
		
		# To stop too many requests in too little time to server
		time.sleep(2)

		
	with open(file_name, "a+") as f:
		io = StringIO()
		json.dump(list_to_json, io, sort_keys=True, indent=4, separators=(',', ': '))
		f.write(io.getvalue())
	f.close()
	return "Successfully Saved to downloads ......"

def search_shine(*args, **kwargs):
	file_path = kwargs['file_path']
	if len(args)==2:
		web_page = get_webpage_by_params(args[0], args[1])
	elif len(args)==1:
		web_page = get_webpage_by_link(args[0])
	links = get_post_links(web_page)
	print(get_job_detail(links, file_path))

# main('computer vision machine learning', 'mumbai hyderabad pune')
