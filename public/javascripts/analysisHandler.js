$( document ).ready(function() {
var submit = document.getElementById("submit");
console.log("ready to submit");
submit.onclick = function(){
	var amount = document.getElementById("loan_amt").value;
	var selected_option = $('#sector option:selected');
	var sector = document.getElementById("sector");
	var s = sector.options[sector.selectedIndex].text;
	var themes = document.getElementById("theme").checked;

	console.log("HI MARSHALL");
	console.log("Amount:" + amount);
	console.log("Sector:" + s);
	console.log("Theme:" + themes);


}
});

