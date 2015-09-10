var express = require('express');
var router = express.Router();
var request = require('request');
var numberOfResults = 5;

/* GET home page. */
router.get('/', function(req, res, next) {
  getNewestLoans(numberOfResults, function(err, response, data){ 
     if (response.statusCode != 200) {
        console.log("Error in getting the most recent loans");
        return;
     } console.log("Status code of getNewestLoans: " + response.statusCode);
    var fetchedData = JSON.parse( data );
    var loans = fetchedData["loans"];

    var loanNum = [];
    var names = [];
    var countries = []; //var countryCodes = [];

    for(i = 0; i < loans.length; i++) {
          names.push(loans[i]["name"]);  
          countryName = loans[i]["location"]["country"];
          countries.push(countryName); //countryCodes.push(loans[i]["location"]["country_code"]);
     }
     
    if (countries.length == 0) {
        console.log("CountryNames is blank (getHDIindex) ");
        return;
    } 
    
    var humanIndex = [];
    var asyncCalls = 0;
    for (i = 0; i < countries.length; i++) {
       getHDIindex(countries[i], function(err, hdiData){
           if (err) {
               console.log("Error in getting HDI Index: " + err);
               return;
           }
           humanIndex.push(hdiData);
           asyncCalls = asyncCalls + 1;
       }); 
     } 
        
    var timeout = setInterval( function() { 
        /* This code (should) wait until the array has filled up before returning*/
        console.log("Asynch Calls: " + asyncCalls);
        if(/*checkIfFinished()*/asyncCalls == countries.length) { 
            clearInterval(timeout); 
            res.render('feed', { title: 'Kiva Impact Feed', body: names, country: countries,
              hdi: humanIndex});
        } 
    }, 100 );
  });
});

/* Modularize your code as much as possible. Make each method do a simple, specialized task */
function getHDIindex(countryName, callback) {
  
  var hdiIndices = [];
  console.log("Country Name for loop: " + countryName);
    request.get('http://data.undp.org/resource/myer-egms.json?country=' + countryName, function(err, response, data) {
      if (response.statusCode != 200) {
        console.log("Error in getting country information from HDI: " + response.statusCode);
        return callback("ERROR", null);
      }
      var hdiObj = JSON.parse(data);
      console.log("Data from getHDI Index" + data);
      
      if (hdiObj[0]) {
          hdiIndices.push(hdiObj[0]["hdi_rank"]);
          console.log("Country: " + countryName + ", HDI Index Rank: " + hdiObj[0]["hdi_rank"]);
        }
      if (hdiIndices.length == 0 ) {
          console.log("HdiIndices is blank");
          return callback(null, hdiIndices/*Do you instead want to return an error here?*/);
      }
      else 
      { 
         return callback(null, hdiIndices); 
      }
   });
}
                          

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