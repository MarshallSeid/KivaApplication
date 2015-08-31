var express = require('express');
var router = express.Router();
var request = require('request');
var numberOfResults = 5;
/* GET home page. */
router.get('/', function(req, res, next) {
	getNewestLoans(numberOfResults, function(err, response, data){ 
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
  var humanIndex = [];


  //Other uses we have: Sector (Agriculture, Business), Activity (Tailoring)
  for(i = 0; i < loans.length; i++) {
  		   names.push(i);
          names.push(loans[i]["name"]);  
          countryName = loans[i]["location"]["country"];
          countries.push(countryName);
          countryCodes.push(loans[i]["location"]["country_code"]);
   var returnIndex = getHDIindex(countryName, function(err, response, hdiData){
            var hdiObj = JSON.parse(hdiData);
            var hdiRank = hdiObj[0]["hdi_rank"];
            humanIndex.push(hdiRank);
            console.log("HDI Ranks in function call: " + humanIndex);
            return humanIndex;
          });
      console.log("RETURN INDEX: " + returnIndex);
      console.log("HDI Ranks in for loop: " + humanIndex);
   }
   console.log("NAMES: " + names);  
   console.log("COUNTRIES: " + countries);
   console.log("HDI Ranks: " + humanIndex);
  res.render('feed', { title: 'Kiva Impact Feed', body: names, country: countries,
               cc: countryCodes, hdi: humanIndex});
  });
});

function getNewestLoans(numOfResults, callback) {

	request.get('http://api.kivaws.org/v1/loans/newest.json?per_page=' + numOfResults, callback);
	//Callback that uses getlenderinfo
	//Do more stuff with what I got from the getlenderinfo 

}

function getHDIindex(countryName, callback) {
  console.log("COUNTRY NAME FROM HDI: " + countryName);
  request.get('http://data.undp.org/resource/myer-egms.json?country=' + countryName, callback);
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
