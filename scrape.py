from requests import get
from json import loads
from math import ceil

per_page = 500
num_pages = 0
loan_avg = 0

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
			countries[country_name]["loan_avg"] += loan["loan_amount"]
			countries[country_name]["desc_avg"] += len(loan["description"]["languages"])
			countries[country_name]["tags_avg"] += len(loan["tags"])
			countries[country_name]["use_avg"] += len(loan["use"])
			countries[country_name]["num_loans"] += 1
		else:
			countries[country_name] = {}
			countries[country_name]["country_code"] = country_code
			countries[country_name]["desc_avg"] = len(loan["description"]["languages"])
			countries[country_name]["tags_avg"] = len(loan["tags"])
			countries[country_name]["use_avg"] = len(loan["use"])
			countries[country_name]["loan_avg"] = loan["loan_amount"]
			countries[country_name]["num_loans"] = 1

# for loop to avg all sums
for country in countries:
	num_loans = countries[country]["num_loans"]
	countries[country]["loan_avg"] /= float(num_loans)
	countries[country]["desc_avg"] /= float(num_loans)
	countries[country]["tags_avg"] /= float(num_loans)
	countries[country]["use_avg"] /= float(num_loans)


#print countries' loan avg
for country in countries:
	print ("loan average length for " + country + ": " + str(countries[country]["loan_avg"]))

#print countries' desc avg
for country in countries:
	print ("desc average length for " + country + ": " + str(countries[country]["desc_avg"]))

#print countries' use avg
for country in countries:
	print ("use average length for " + country + ": " + str(countries[country]["use_avg"]))

#print countries' tag avg
for country in countries:
	print ("tag average length for " + country + ": " + str(countries[country]["tags_avg"]))
