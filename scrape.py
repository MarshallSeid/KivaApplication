import requests, json

per_page = "500"
num_pages = 12

loan_amount = 0
num_loans = 0

for i in range(1,num_pages+1):
	r = requests.get("http://api.kivaws.org/v1/loans/newest.json?per_page="+per_page+"&page=" + str(i))
	parsed = json.loads(r.content)
	num_loans = parsed["paging"]["total"]
	for loan in parsed["loans"]:
		loan_amount += loan["loan_amount"]

print loan_amount / num_loans
