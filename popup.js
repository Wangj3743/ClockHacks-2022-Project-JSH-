// import { webdriver } from 'selenium';
// import { By } from 'selenium/webdriver/common/by';
// import { WebDriverWait } from 'selenium/webdriver/support/ui';
// import { expected_conditions as EC } from 'selenium/webdriver/support';
// import * as time from 'time';

document.addEventListener("DOMContentLoaded", function(){ //html fully rendered

	document.getElementById("submit").addEventListener("click", function(){
		document.getElementById("vis").style.display="none";
		document.getElementById("vis").style.visibility="hidden";
		document.getElementById("invis").style.display="block";
		document.getElementById("invis").style.visibility="visible";
		
	});

	document.getElementById("fancy_Button").addEventListener("click", function(){
		var driver, id_box, login_button, pass_box;
		driver = new webdriver.Chrome();
		driver.get("https://secure.devpost.com/users/login?ref=top-nav-login%27");
		id_box = driver.find_element(By.ID, "user_email");
		id_box.send_keys("PLACEHOLDER USERNAME");
		pass_box = driver.find_element(By.ID, "user_password");
		pass_box.send_keys("PLACEHOLDER PASSWORD");
		login_button = driver.find_element(By.ID, "submit-form");
		login_button.click();
	});
});