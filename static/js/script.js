//profiles

var student_profiles = document.getElementById("student_profiles");
var add_more_fields = document.getElementById("add_field");
var remove_fields = document.getElementById("remove_field");


add_more_fields.onclick = function() {
  var new_field = document.createElement('input');
  new_field.setAttribute('type', 'url');
  new_field.setAttribute('name', 'stu_profiles');
  new_field.setAttribute('class', 'form-control col-sm-8 col-md-4');
  new_field.setAttribute('placeholder', 'another_field');
  student_profiles.appendChild(new_field);
}

remove_fields.onclick = function() {
  var input_tags = student_profiles.getElementsByTagName("input");
  
  if (input_tags.length > 1){
    student_profiles.removeChild(input_tags[(input_tags.length) - 1]);
  }
}

//certificates
var student_certificates = document.getElementById("student_certificates");
var add_field_certificate = document.getElementById("add_field_certificate");
var remove_field_certificate = document.getElementById("remove_field_certificate");


add_field_certificate.onclick = function() {
  var new_field = document.createElement('input');
  new_field.setAttribute('type', 'url');
  new_field.setAttribute('name', 'stu_certificates');
  new_field.setAttribute('class', 'form-control col-sm-8 col-md-4');
  new_field.setAttribute('placeholder', 'another_field');
  student_certificates.appendChild(new_field);
}

remove_field_certificate.onclick = function() {
  var input_tags = student_certificates.getElementsByTagName("input");
  
  if (input_tags.length > 1){
    student_certificates.removeChild(input_tags[(input_tags.length) - 1]);
  }
}


//project links
var student_projectslinks = document.getElementById("student_projectslinks");
var add_field_project = document.getElementById("add_field_project");
var remove_field_project = document.getElementById("remove_field_project");


add_field_project.onclick = function() {
  var new_field = document.createElement('input');
  new_field.setAttribute('type', 'url');
  new_field.setAttribute('name', 'stu_projectslinks');
  new_field.setAttribute('class', 'form-control col-sm-8 col-md-4');
  new_field.setAttribute('placeholder', 'another_field');
  student_projectslinks.appendChild(new_field);
}

remove_field_project.onclick = function() {
  var input_tags = student_projectslinks.getElementsByTagName("input");
  
  if (input_tags.length > 1){
    student_projectslinks.removeChild(input_tags[(input_tags.length) - 1]);
  }
}