# RULES 
"""
 - STORE ALL DATA IN DICTIONARES
 - USUNG AS LESS PACKAGES AS POSSIBLE 
"""

from multiprocessing import Pool
from requests_html import HTMLSession

# IF NEED SELENIUM SELENIUM
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# WRITE FUNC TO LOG IN WITH SELENIUM AND JUST REQUESTS


def Log_in(session):
	# log ins to some site, returns loge in session
	get = session.get('')
	post = session.post('')

	return session



def get_cetegories(link:str, session=HTMLSession()):
	# Collects category dicts to list and ruturns in
	r = session.get(link)

	categories = []
	# Here might be some box and all following lines needs to be higher
	for category in r.html.find('categories_class_name,should_end_with_tag_a'):
		if category.text == 'Exactly needed category':
			cat_id = 100		# any number
		elif category.text == 'Another exactly needed category':
			cat_id = 101
		else:	# others categories thats just useless and don't need to be saved
			continue
		"""
		else:
			_id = 99	# some trash category
		"""
		categories.append(
			{
				'name': category.text,
				'url': category['href'],	# if error than category.attrs['href']
				'_id': cat_id
			}
		)	

	return categories

def get_product_list(cat:dict, session=HTMLSession()):
	# Collects all catogory products and returns list of dicts
	
	"""
	here might be some kind of getting through pagesfor this usualy all needed is just:
	# var to count pages
	page = -1
	# loop to 
	while True:
		if '404' in r.html.find('body')[0].text
			break
	"""
	products = []
	r = session.get(cat['url'])
	for prod in r.html.find('Products_class_name.should_end_with_tag_a'):
		products.append(
			{
				'url': prod['href'],	# if error than prod.attrs['href']
				'category_id': cat['_id']
			}
		)
	pass

def collect_prod_data(prod:dict, session=HTMLSession()):
	# Collects product data
	r = session.get(prod['url'])

	prod['name'] = r.html.find('span.or_div.class_came')
	prod['description'] = r.html.find('span.or_div.class_came')
	prod['price'] = r.html.find('span.or_div.class_came')

	"""
	Here you can make some changes in data, transtale, delete commas ect.
	"""
	prod.pop('some_data_that_can_lead_to_some_issue')
	return prod

"""
HEre is main for multyflow work
"""

if __name__ == '__name__':
	session = HTMLSession()
	"""
	here you set up storages
	"""
	cats = get_cetegories('link/to/main/page/of_site')
	for cat in cats:
		prods = get_product_list(cats, session)

		results = Pool(collect_prod_data, prods)

		"""
		HERE YOUR WRITING FUNCTION
		"""

		


	