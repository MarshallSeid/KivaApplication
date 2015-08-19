var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home', { title: 'Kiva Impact Home Page' });
});

module.exports = router;
