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
		"num_loans": 0.0,
		"tag":{}
	},
	"funded": {
		"loan_avg": 0.0,
		"use_avg": 0.0,
		"desc_avg": 0.0,
		"tags_avg": 0.0,
		"num_loans": 0.0,
		"tag":{}
	},
	"expired": {
		"loan_avg": 0.0,
		"use_avg": 0.0,
		"desc_avg": 0.0,
		"tags_avg": 0.0,
		"num_loans": 0.0,
		"tag":{}
	},

}
	# Number of funded over total with that tag
totals = {}
# get one loan to calculate num_loans and num_pages
req = get("http://api.kivaws.org/v1/loans/search.json?per_page=1").content
parsed = loads(req)
num_loans = parsed["paging"]["total"]
num_pages = int(ceil(num_loans / per_page))

# for loop for each page
for i in range(1, 100):
	req = get("http://api.kivaws.org/v1/loans/search.json?per_page="+str(per_page)+"&page=" + str(i)).content
	parsed = loads(req)
	# for loop for each loan
	for loan in parsed["loans"]:
		loans[loan["status"]]["loan_avg"] += loan["loan_amount"]
		loans[loan["status"]]["desc_avg"] += len(loan["description"]["languages"])
		loans[loan["status"]]["tags_avg"] += len(loan["tags"])
		loans[loan["status"]]["use_avg"] += len(loan["use"])
		loans[loan["status"]]["num_loans"] += 1

		for tag in loan["tags"]:
			tag_name = tag["name"] 
			if tag_name in loans[loan["status"]]["tag"]:
				loans[loan["status"]]["tag"][tag_name] += 1
			else:
				loans[loan["status"]]["tag"][tag_name] = 1
			if tag_name in totals:
				totals[tag_name] += 1
			else: 
				totals[tag_name] = 1.0
#tags_sort = [ (v,k) for k,v in loans["funded"]["tag"][name].iteritems() ]
#tags_sort.sort(reverse=True)
for name in loans["funded"]["tag"]:
	if loans["funded"]["tag"][name] > 10:
		loans["funded"]["tag"][name] = (loans["funded"]["tag"][name] / totals[name]) * 100
		print ("Tag: " + name + " - " + str(loans["funded"]["tag"][name]))

#tags_sort = [ (v,k) for k,v in loans["funded"]["tag"][name].iteritems() ]
#tags_sort.sort(reverse=True)
#for v,k in tags_sort:
#	print "%s: %d" % (k,v)
for status in loans:
	num_loans = loans[status]["num_loans"]
	loans[status]["loan_avg"] /= num_loans
	loans[status]["desc_avg"] /= num_loans
	loans[status]["tags_avg"] /= num_loans
	loans[status]["use_avg"] /= num_loans
	#
#	for v,k in tags_sort:
##		print "%s: %d" % (k,v)
	#for tag in loans[status]["tag"]:
	#	print ("# of " + tag + " for " + status + ": " + str(loans[status][tag]))
	print ("loan average amount for " + status + ": " + str(loans[status]["loan_avg"]))
	print ("desc average length for " + status + ": " + str(loans[status]["desc_avg"]))
	print ("use average length for " + status + ": " + str(loans[status]["use_avg"]))
	print ("tag average length for " + status + ": " + str(loans[status]["tags_avg"]))
