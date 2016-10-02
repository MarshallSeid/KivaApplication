import time
import json
from requests import get
from json import loads
from math import ceil

per_page = 500
num_pages = 0

data = { 
	"funded": {
		"total_funds": 0.0,
		"countries": {},
		"activity": {},
		"tag": {},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	},
	"fundraising": {
		"total_funds": 0.0,
		"countries": {},
		"activity": {},
		"tag": {},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	},
	"expired": {
		"total_funds": 0.0,
		"countries": {},
		"activity": {},
		"tag": {},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	},
	"total": {
		"total_funds": 0.0,
		"countries": {},
		"activity": {},
		"tag_funded": {},
		"sector": {},
		"themes": {},
		"num_loans": 0.0
	}
}

averages = {
	"sectors": {
		"Agriculture": {
		 	"avg_funded": 0.0,
			 "num_loans": 0.0,
			 "total_funds": 0.0},
		"Arts": {
			 "avg_funded": 0.0,
			 "num_loans": 0.0,
			 "total_funds": 0.0}, 
		"Clothing": {
			"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		"Construction": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		"Education": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Entertainment": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Food": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Health": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Housing": {
			"avg_funded": 0.0,	
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Manufacturing": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Personal Use": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Retail": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Services": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Transportation": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}, 
		 "Wholesale": {
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}
	},
	"activities": {

	},
	"themes": {		
		"Green":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Higher Education":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Arab Youth":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Kiva City LA":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Islamic Finance":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Youth":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Start-Up":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Water and Sanitation":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Vulnerable Groups":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Fair Trade":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Rural Exclusion":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Mobile Technology":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Underfunded Areas":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Conflict Zones":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Job Creation":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "SME":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Growing Businesses":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Kiva City Detroit":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Health":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Disaster recovery":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Flexible Credit Study":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Innovative Loans":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "IPA Study":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0},
		 "Refugees/Displaced":{
		 	"avg_funded": 0.0,
			"num_loans": 0.0,
			"total_funds": 0.0}
		}  
	}

req = get("http://api.kivaws.org/v1/loans/search.json?status=funded&per_page=1").content
parsed = loads(req)
num_loans = parsed["paging"]["total"]
num_pages = int(ceil(num_loans / per_page))

# for loop for each page
for i in range(1, num_pages):
	req = get("http://api.kivaws.org/v1/loans/search.json?status=funded&per_page="+str(per_page)+"&page=" + str(i)).content
	parsed = loads(req)
	# for loop for each loan
	for loan in parsed["loans"]:
		status = loan["status"]
		# Increment Countries
		country  = loan["location"]["country"]
		loan_amt = loan["funded_amount"]
		if country not in data[loan["status"]]["countries"]:
			data[status]["countries"][country] = 1
		else: 
			data[status]["countries"][country] += 1

		# Update sector fields 
		sector = loan["sector"]
		if sector not in data[status]["sector"]:
			data[status]["sector"][sector] = 1
			averages["sectors"][sector]["num_loans"] = 1
		else: 
			data[status]["sector"][sector] += 1
			averages["sectors"][sector]["num_loans"] += 1
		# Find averages of sector  
		averages["sectors"][sector]["total_funds"] += loan_amt
		averages["sectors"][sector]["avg_funded"] = averages["sectors"][sector]["total_funds"] / averages["sectors"][sector]["num_loans"]

		# Increment theme field
		if "themes" in loan:
			for theme in loan["themes"]:
				if theme not in data[loan["status"]]["themes"]:
					data[status]["themes"][theme] = 1
					averages["themes"][theme]["num_loans"] = 1

				else: 
					data[status]["themes"][theme] += 1
					averages["themes"][theme]["num_loans"] += 1
				averages["themes"][theme]["total_funds"] += loan_amt
				averages["themes"][theme]["avg_funded"] = averages["themes"][theme]["total_funds"] / averages["themes"][theme]["num_loans"]
		
		# Increment activity field
		activity = loan["activity"]
		if activity not in data[status]["activity"]:
			data[status]["activity"][activity] = 1
			averages["activities"][activity] = {
			"avg_funded": loan_amt, "num_loans": 1, "total_funds": loan_amt
			}
		else: 
			data[status]["activity"][loan["activity"]] += 1
			averages["activities"][activity]["total_funds"] += loan_amt
			averages["activities"][activity]["num_loans"] += 1
			averages["activities"][activity]["avg_funded"] = averages["activities"][activity]["total_funds"] / averages["activities"][activity]["num_loans"]

# Update the Funded Campaigns/Total Campaigns
with open('data.txt', 'w') as outfile:
	json.dump(data, outfile)
with open('averages.txt', 'w') as outfile:
	json.dump(averages, outfile)