from requests import get
from json import loads
from math import ceil

per_page = 500
num_pages = 0
loan_avg = 0

loans = {
	"fundraising": {
		"loan_avg": 0.0,
		"use_avg": 0.0,
		"desc_avg": 0.0,
		"tags_avg": 0.0,
		"num_loans": 0.0
	},
	"funded": {
		"loan_avg": 0.0,
		"use_avg": 0.0,
		"desc_avg": 0.0,
		"tags_avg": 0.0,
		"num_loans": 0.0
	},
	"expired": {
		"loan_avg": 0.0,
		"use_avg": 0.0,
		"desc_avg": 0.0,
		"tags_avg": 0.0,
		"num_loans": 0.0
	}	
}

# get one loan to calculate num_loans and num_pages
req = get("http://api.kivaws.org/v1/loans/search.json?country_code=US&per_page=1").content
parsed = loads(req)
num_loans = parsed["paging"]["total"]
num_pages = int(ceil(num_loans / per_page))

# for loop for each page
for i in range(1,num_pages+1):
	req = get("http://api.kivaws.org/v1/loans/search.json?country_code=US&per_page="+str(per_page)+"&page=" + str(i)).content
	parsed = loads(req)
	# for loop for each loan
	for loan in parsed["loans"]:
		loans[loan["status"]]["loan_avg"] += loan["loan_amount"]
		loans[loan["status"]]["desc_avg"] += len(loan["description"]["languages"])
		loans[loan["status"]]["tags_avg"] += len(loan["tags"])
		loans[loan["status"]]["use_avg"] += len(loan["use"])
		loans[loan["status"]]["num_loans"] += 1

for status in loans:
	num_loans = loans[status]["num_loans"]
	loans[status]["loan_avg"] /= num_loans
	loans[status]["desc_avg"] /= num_loans
	loans[status]["tags_avg"] /= num_loans
	loans[status]["use_avg"] /= num_loans
	print ("loan average length for " + status + ": " + str(loans[status]["loan_avg"]))
	print ("desc average length for " + status + ": " + str(loans[status]["desc_avg"]))
	print ("use average length for " + status + ": " + str(loans[status]["use_avg"]))
	print ("tag average length for " + status + ": " + str(loans[status]["tags_avg"]))
