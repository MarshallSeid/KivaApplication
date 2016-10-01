from requests import get
from json import loads
from math import ceil

per_page = 500
num_pages = 0
loan_sum = 0

countries = {}

# get one loan to calculate num_loans and num_pages
req = get("http://api.kivaws.org/v1/loans/newest.json?per_page=1").content
parsed = loads(req)
num_loans = parsed["paging"]["total"]
num_pages = int(ceil(num_loans / per_page))

# for loop for each page
for i in range(1,num_pages+1):
	req = get("http://api.kivaws.org/v1/loans/newest.json?per_page="+str(per_page)+"&page=" + str(i)).content
	parsed = loads(req)
	# for loop for each loan
	for loan in parsed["loans"]:
		country_code = str(loan["location"]["country_code"])
		country_name = str(loan["location"]["country"])
		if country_name in countries:
			countries[country_name]["loan_sum"] += loan["loan_amount"]
			countries[country_name]["num_loans"] += 1
		else:
			countries[country_name] = {}
			countries[country_name]["country_code"] = country_code
			countries[country_name]["loan_sum"] = loan["loan_amount"]
			countries[country_name]["num_loans"] = 1

		#num_desc_lan = len(loan["description"]["languages"])

#print countries
for country in countries:
	print (country + ": " + str(countries[country]["loan_sum"] / countries[country]["num_loans"]))