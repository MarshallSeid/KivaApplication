var express = require('express');
var router = express.Router();

/* GET Impact Calculator. */
router.get('/', function(req, res, next) {
	res.render('calculator', { title: 'Kiva Impact Calculator' });
	
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
