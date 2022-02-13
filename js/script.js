function validateRegistrationForm() {

	var firstname = document.forms["RegistrationForm"].firstName.value.trim();
	var lastname = document.forms["RegistrationForm"].lastName.value.trim();
	var emailId = document.forms["RegistrationForm"].emailId.value.trim();
	var empId = document.forms["RegistrationForm"].empId.value.trim();
	var password = document.forms["RegistrationForm"].passWord.value.trim();
	var contactNumber = document.forms["RegistrationForm"].contactNumber.value
			.trim();
	var passCode = document.forms["RegistrationForm"].passCode.value.trim();
	var expertiseArea = document.forms["RegistrationForm"].expertiseArea.value
			.trim();

	var status = true;

	if (firstname == "") {
		document.getElementById("firstNameError").innerText = " First name is required.";
		document.forms["RegistrationForm"].firstName.style.borderColor = "red";
		status = false;
	}
	if (lastname == "") {
		document.getElementById("lastNameError").innerText = " Last name is required.";
		document.forms["RegistrationForm"].lastName.style.borderColor = "red";
		status = false;
	}
	if (emailId == "") {
		document.getElementById("emailIdError").innerText = " EmailId is required.";
		document.forms["RegistrationForm"].emailId.style.borderColor = "red";

		status = false;
	}
	if (empId == "") {
		document.getElementById("EmployeeIdError").innerText = " Employee ID is required.";
		document.forms["RegistrationForm"].empId.style.borderColor = "red";

		status = false;
	}
	if (password == "") {
		document.getElementById("passwordError").innerText = " Password is required.";
		document.forms["RegistrationForm"].passWord.style.borderColor = "red";

		status = false;
	}
	if (contactNumber == "") {
		document.getElementById("contactNumberError").innerText = " Contact Number is required.";
		document.forms["RegistrationForm"].contactNumber.style.borderColor = "red";
		status = false;
	} else if (isNaN(contactNumber)) {
		document.getElementById("contactNumberError").innerText = " Contact Number has to be a number";
		document.forms["RegistrationForm"].contactNumber.style.borderColor = "red";
		status = false;
	}
	if (passCode == "") {
		document.getElementById("passcodeError").innerText = " Passcode is required.";
		document.forms["RegistrationForm"].passCode.style.borderColor = "red";
		status = false;
	}

	if (expertiseArea == "") {
		document.getElementById("expertiseAreaError").innerText = "Expertise Area is required.";
		document.forms["RegistrationForm"].expertiseArea.style.borderColor = "red";

		status = false;
	}

	if (status == true) {
		alert("Saved successfully");
	}
	return status;
}
