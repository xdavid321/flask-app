function validateRegistrationForm() {
	var fname = document.forms["RegistrationForm"].firstName.value.trim();
	var lname = document.forms["RegistrationForm"].lastName.value.trim();
	var designation = document.forms["RegistrationForm"].designation.value
			.trim();
	var number = document.forms["RegistrationForm"].contactNumber.value.trim();
	var empId = document.forms["RegistrationForm"].empId.value.trim();
	var seatNo = document.forms["RegistrationForm"].seatNumber.value.trim();
	var pcNumber = document.forms["RegistrationForm"].pcNumber.value.trim();
	var ipAddress = document.forms["RegistrationForm"].ipAddress.value.trim();
	var userId = document.forms["RegistrationForm"].userId.value.trim();
	var password = document.forms["RegistrationForm"].password.value.trim();

	var status = true;
	if (fname == "") {
		document.getElementById("firstNameError").innerText = " First name is required.";
		document.forms["RegistrationForm"].firstName.style.borderColor = "red";
		status = false;
	}
	if (lname == "") {
		document.getElementById("lastNameError").innerText = " Last name is required.";
		document.forms["RegistrationForm"].lastName.style.borderColor = "red";
		status = false;
	}
	if (designation == "") {
		document.getElementById("designationError").innerText = " Designation is required.";
		document.forms["RegistrationForm"].designation.style.borderColor = "red";

		status = false;
	}
	if (number == "") {
		document.getElementById("contactNumberError").innerText = " Contact Number is required.";
		document.forms["RegistrationForm"].contactNumber.style.borderColor = "red";
		status = false;
	} else if (isNaN(number)) {
		document.getElementById("contactNumberError").innerText = " Contact Number has to be a number";
		document.forms["RegistrationForm"].contactNumber.style.borderColor = "red";
		status = false;
	}
	if (empId == "") {
		document.getElementById("empIdError").innerText = " Employee ID is required.";
		document.forms["RegistrationForm"].empId.style.borderColor = "red";

		status = false;
	}
	if (seatNo == "") {
		document.getElementById("seatNumberError").innerText = " Seat Number is required.";
		document.forms["RegistrationForm"].seatNumber.style.borderColor = "red";
		status = false;
	}

	if (pcNumber == "") {
		document.getElementById("pcNumberError").innerText = " PC Number is required.";
		document.forms["RegistrationForm"].pcNumber.style.borderColor = "red";

		status = false;
	}
	if (ipAddress == "") {
		document.getElementById("ipAddressError").innerText = " IP Address is required.";
		document.forms["RegistrationForm"].ipAddress.style.borderColor = "red";

		status = false;
	}
	if (userId == "") {
		document.getElementById("userIdError").innerText = " User ID is required.";
		document.forms["RegistrationForm"].userId.style.borderColor = "red";

		status = false;
	}
	if (password == "") {
		document.getElementById("passwordError").innerText = " Password is required.";
		document.forms["RegistrationForm"].password.style.borderColor = "red";

		status = false;
	}
	if (status == true) {
		alert("Saved successfully");
	}
	return status;
}
