var express = require('express');
var router = express.Router();
var request = require('request');

/* GET Map. */
router.get('/', function(req, res, next) {
	console.log("gonna render");
	res.render('analysis', { title: 'Analysis', body: "Map temporary body"});	
});

module.exports = router;
