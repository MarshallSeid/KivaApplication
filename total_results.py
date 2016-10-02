import time
import json
from requests import get
from json import loads
from math import ceil

per_page = 500
num_pages = 0
loan_avg = 0

data = { 
	"funded": {
		"countries": {},
		"tag": {},
		"gender": {
			"male": 0.0,
			"female": 0.0
		},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	},
	"expired": {
		"countries": {},
		"tag": {},
		"gender": {
			"male": 0.0,
			"female": 0.0
		},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	},
	"total": {
		"countries": {},
		"tag_funded": {},
		"gender_funded": {
			"male": 0.0,
			"female": 0.0
		},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	}
}

req = get("http://api.kivaws.org/v1/loans/search.json?per_page=1").content
parsed = loads(req)
num_loans = parsed["paging"]["total"]
num_pages = int(ceil(num_loans / per_page))

# for loop for each page
for i in range(1, 20):
	req = get("http://api.kivaws.org/v1/loans/search.json?per_page="+str(per_page)+"&page=" + str(i)).content
	parsed = loads(req)
	# for loop for each loan
	for loan in parsed["loans"]:
		# Increment Countries
		if data[loan["status"]]["countries"][loan[country_code]] == 0:
			data[loan["status"]]["countries"][loan[country_code]] = 1;
		else: 
			data[loan["status"]]["countries"][loan[country_code]] += 1;
		# Increment Gender	
		data[loan["status"]]["gender_funded"][loan[gender]] += 1;
		data["total"]["gender_funded"][loan[gender]] += 1;
		# Increment tag funded
		if data[loan["status"]]["sector"][loan["sector"]] == 0:
			data[loan["status"]]["sector"][loan["sector"]] = 1;
		else: 
			data[loan["status"]]["sector"][loan["sector"]] += 1;

		data[loan["status"]]["num_loans"] += 1

		# for tag in loan["tags"]:
		# 	tag_name = tag["name"] 
		# 	if tag_name in loans[loan["status"]]["tag"]:
		# 		loans[loan["status"]]["tag"][tag_name] += 1
		# 	else:
		# 		loans[loan["status"]]["tag"][tag_name] = 1
		# 	if tag_name in totals:
		# 		totals[tag_name] += 1
		# 	else: 
		# 		totals[tag_name] = 1.0

with open('data.txt', 'w') as outfile:
	json.dump(data, outfile)

# for name in data["funded"]["tag"]:
# 	if data["funded"]["tag"][name] > 10:
# 		data["funded"]["tag"][name] = (data["funded"]["tag"][name] / data[totals][name]) * 100
# 		print ("Tag: " + name + " - " + str(loans["funded"]["tag"][name]))

# for status in loans:
# 	num_loans = loans[status]["num_loans"]
# 	loans[status]["loan_avg"] /= num_loans
# 	print ("loan average amount for " + status + ": " + str(loans[status]["loan_avg"]))
# 	print ("desc average length for " + status + ": " + str(loans[status]["desc_avg"]))
# 	print ("use average length for " + status + ": " + str(loans[status]["use_avg"]))
# 	print ("tag average length for " + status + ": " + str(loans[status]["tags_avg"]))
