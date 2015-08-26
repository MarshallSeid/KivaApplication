var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
	getNewestLoans(20, function(err, response, data){
		console.log("RESPONSE: " + response);
		console.log("DATA: " + data);
	  if (response.statusCode != 200) {
	 		console.log("ERROR RETURNED");
	 		return;
 		}
  res.render('feed', { title: 'Kiva Impact Feed', body: response})
})});


function getNewestLoans(numOfResults, callback) {

	request.get('http://api.kivaws.org/v1/loans/newest.json?per_page=' + numOfResults, callback);
	//Callback that uses getlenderinfo
	//Do more stuff with what I got from the getlenderinfo 

}

module.exports = router;

