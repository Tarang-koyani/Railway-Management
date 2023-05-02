// // console.log("hello world!");

// /////validation for booking -form
// var bookingForm = document.getElementById("booking-form");

// const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
// const phoneRegex = /^\d{10}$/;
// bookingForm.addEventListener("submit", (e) => {
// 	// Prevent form submission
// 	// event.preventDefault();
// 	var nameField = document.getElementById("name");
// 	var classField = document.getElementById("class");
// 	var emailField = document.getElementById("email");
// 	var phoneField = document.getElementById("phone");
// 	var fromField = document.getElementById("from");
// 	var toField = document.getElementById("to");
// 	var dateField = document.getElementById("date");
// 	// Validate fields
// 	if (
// 		nameField.value === "" ||
// 		emailField.value === "" ||
// 		phoneField.value === "" ||
// 		fromField.value === "" ||
// 		toField.value === "" ||
// 		dateField.value === "" ||
// 		classField.value === ""
// 	) {
// 		alert("Please fill in all fields.");
// 		return;
// 	}

// 	// Validate email format
// 	if (!emailRegex.test(emailField.value)) {
// 		alert("Please enter a valid email address.");
// 		return;
// 	}

// 	// Validate phone number format
// 	if (!phoneRegex.test(phoneField.value)) {
// 		alert("Please enter a valid phone number.");
// 		return;
// 	}

// 	// Submit form if all validation passes
// 	bookingForm.submit();
// });

// // validation for registration form
// const register_form = document.getElementById("register-form");

// register_form.addEventListener("submit", (e) => {
// 	const reg_name = document.getElementById("name").value;
// 	const email = document.getElementById("email").value;
// 	const password = document.getElementById("password").value;
// 	const confirmPassword = document.getElementById("confirmpassword").value;
// 	const phone = document.getElementById("phone").value;
// 	const address = document.getElementById("address").value;

// 	if (reg_name === "") {
// 		alert("Name must be filled out");
// 		return;
// 	}

// 	if (email === "") {
// 		alert("Email must be filled out");
// 		return;
// 	}

// 	if (password === "") {
// 		alert("Password must be filled out");

// 		return;
// 	}
// 	if (!emailRegex.test(emailField.value)) {
// 		alert("Please enter a valid email address.");
// 		return;
// 	}
// 	if (password !== confirmPassword) {
// 		alert("Passwords do not match");
// 		return;
// 	}

// 	if (phone === "") {
// 		alert("Phone number must be filled out");

// 		return;
// 	}
// 	if (!phoneRegex.test(phoneField.value)) {
// 		alert("Please enter a valid phone number.");
// 		return;
// 	}
// 	if (address === "") {
// 		alert("Address must be filled out");
// 		return;
// 	}

// 	register_form.submit();
// });
// console.log("hello world");
$(function () {
	var dtToday = new Date();

	var month = dtToday.getMonth() + 1;
	var day = dtToday.getDate();
	var year = dtToday.getFullYear();
	if (month < 10) month = "0" + month.toString();
	if (day < 10) day = "0" + day.toString();
	var maxDate = year + "-" + month + "-" + day;
	$("#inputdate").attr("min", maxDate);
});
