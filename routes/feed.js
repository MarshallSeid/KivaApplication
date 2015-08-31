var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
	getNewestLoans(20, function(err, response, data){ 
		//console.log("RESPONSE: " + response);
		//console.log("DATA: " + data);
	  if (response.statusCode != 200) {
	 		console.log("ERROR RETURNED");
	 		return;
 		}
  var obj = JSON.parse( data );
  var loanNum = [];
  var loans = obj["loans"];
  var names = [];
  var countries = [];
  var countryCodes = [];

  //Other uses we have: Sector (Agriculture, Business), Activity (Tailoring)
  for(i = 0; i < loans.length; i++) {
  		  names.push(i);
          names.push(loans[i]["name"]);    
          countries.push(loans[i]["location"]["country"]);
          countryCodes.push(loans[i]["location"]["country_code"]);

  }
  console.log("NAMES: " + names);	
  console.log("COUNTRIES: " + countries);
  res.render('feed', { title: 'Kiva Impact Feed', body: names, country: countries,
  					   cc: countryCodes})
})});

function getNewestLoans(numOfResults, callback) {

	request.get('http://api.kivaws.org/v1/loans/newest.json?per_page=' + numOfResults, callback);
	//Callback that uses getlenderinfo
	//Do more stuff with what I got from the getlenderinfo 

}


module.exports = router;

//Gender Impact (Dependenent on Gender and what the HDI ratings is )
//Environment Impact (Dependent on Sector?)

/* sector(list of strings)
A list of business sectors for which to filter results.
One of: Agriculture, Arts, Clothing, Construction, Education, Entertainment,
		Food, Health, Housing, Manufacturing, Personal Use, Retail, Services, Transportation, Wholesale

Themes(list of strings)
A list of themes for which to filter results.
One of: Green, Higher Education, Arab Youth, Kiva City LA, Islamic Finance, Youth, Start-Up, Water and Sanitation, Vulnerable Groups, Fair Trade, 
Rural Exclusion, Mobile Technology, Underfunded Areas, Conflict Zones, Job Creation, SME, Growing Businesses, Kiva City Detroit, Health, Disaster recovery, 
Flexible Credit Study, Innovative Loans
*/
