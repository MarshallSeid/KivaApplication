var express = require('express');
var router = express.Router();
var request = require('request');

/* GET Map. */
router.get('/', function(req, res, next) {
	res.render('map', { title: 'Map', body: "Map temporary body"});	
});

module.exports = router;
