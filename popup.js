document.addEventListener("DOMContentLoaded", function(){ //once html has been fully rendered
	//alert("the content has been loaded"); //alert 

	document.getElementById("button1").addEventListener("click", function(){ //button id clicked, alert
		// alert("button clicked");
		// var body = document.getElementsByTagName("body")[0].style.fontSize = "10px" //all elements of <body> as an array
		// window.open('https://www.four.lol/', '_blank'); //opens window
	});

	
	var count = 0;
	document.getElementById("buttonFunc").addEventListener("click", function(){ //button id clicked, alert

		count += 1;
		var counter = document.getElementById('clicks').innerHTML = count;
		// console.log("1"); //fails to work
	});
	
});