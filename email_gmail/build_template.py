import os, json




# template = temp_dict['subject'] + temp_dict['subject_Dev'] + temp_dict['body_head'] + temp_dict['first_para'] + temp_dict['body_Dev']+ temp_dict['second_para']+ temp_dict['body_CV']+ temp_dict['body_pre_cnclu_Dev']+ temp_dict['body_cnclu']+ temp_dict['portfolio_reference']+ temp_dict['regards']
# print(template)

def build(rates, template_path):
	with open(template_path, 'r') as template:
		temp_dict = json.load(template)
	template.close()
	if rates[0]+rates[1] >= 4:
		if rates[0]>2 and rates[1]<2:
			template = temp_dict['subject_Dev'] +"\n" +temp_dict['body_head'] + temp_dict['first_para'] + temp_dict['body_Dev']+ temp_dict['second_para']+ temp_dict['body_CV']+ temp_dict['body_pre_cnclu_Dev']+ temp_dict['body_cnclu']+ temp_dict['portfolio_reference']+ temp_dict['regards']
		elif rates[0]>=2 and rates[1]>=2:	
			template = temp_dict['subject_Dev'] + temp_dict['subject_CV']+ "\n" +temp_dict['body_head'] + temp_dict['first_para'] + temp_dict['body_Dev']+ temp_dict['second_para']+ temp_dict['body_CV']+ temp_dict['body_pre_cnclu_Dev']+ temp_dict['body_cnclu']+ temp_dict['portfolio_reference']+ temp_dict['regards']
		elif rates[0]<2 and rates[1]>2:
			template = temp_dict['subject_CV']+ "\n" +temp_dict['body_head'] + temp_dict['first_para'] + temp_dict['body_CV'] + temp_dict['second_para']+ temp_dict['body_Dev'] + temp_dict['body_pre_cnclu_CV']+ temp_dict['body_cnclu']+ temp_dict['portfolio_reference']+ temp_dict['regards']
	else:
		template = "Not a good match"

	return template

