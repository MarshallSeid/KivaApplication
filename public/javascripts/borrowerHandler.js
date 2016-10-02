$( document ).ready(function() {
var submit = document.getElementById("submit");
submit.onclick = function(){
	var amount = document.getElementById("amount").value;
	var tags = document.getElementById("tags").value;
	
	console.log("Amount: " + amount);
}
});

