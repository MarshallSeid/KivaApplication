$( document ).ready(function() {
var lenderButt = document.getElementById("lenderButton");
lenderButt.onclick = function(){
	var lenderId = document.getElementById("formValueId").value;
    console.log("It worked");
    console.log("Id: " + lenderId);
    request('http://api.kivaws.org/v1/loans/' +  lenderId  + '.json', function (error, response, body) {
		if (!error && response.statusCode == 200) {
    		console.log(body) // Show the HTML for the Google homepage.
 		 }
    });
}});

