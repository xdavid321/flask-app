function validateRemedyCreationForm(){
	var category= document.forms["RemedyCreationForm"].category.value;
	var problemStatement = document.forms["RemedyCreationForm"].problemStatement.value;
	
	var status = true;
	
	if (category == "--") {
		alert("Please select one Category");
		status = false;
	}
	if (problemStatement=="") {
		alert("Problem Statement is required");
		status = false;
	}
	return status;
}