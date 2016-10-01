var express = require('express');
var router = express.Router();
var request = require('request');

/* GET Impact Calculator. */
router.get('/', function(req, res, next) {
	// getNewestLoans(20, function(err, response, data){
	// 	//console.log("RESPONSE: " + response);
	// 	//console.log("DATA: " + data);
	// 	if (response.statusCode != 200) {
	// 		console.log("ERROR RETURNED");
	// 		return;
	// 	}
	// 	var obj = JSON.parse(data);
	res.render('map', { title: 'Map', body: "Map temporary body"});	
	// })
});

/*
router.get('/lender', function(req, res, next) {
	var id = req.query.id;
	request('http://api.kivaws.org/v1/loans/' + id + '.json', function (error, response, body) {
  	if (!error && response.statusCode == 200) {
    	console.log(body) // Show the HTML for the Google homepage.
 		 }
   	})
});
*/
module.exports = router;
