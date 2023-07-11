function toggleInputField() {
    var materialType = document.getElementById("id_material_type");  // Get the material type select element
    var urlInput = document.getElementById("url-input");  // Get the URL input container element
    var fileInput = document.getElementById("file-input");  // Get the file input container element

    if (materialType.value === "url") {
        urlInput.style.display = "block";  // Show the URL input container
        fileInput.style.display = "none";  // Hide the file input container
    } else if (materialType.value === "file") {
        urlInput.style.display = "none";  // Hide the URL input container
        fileInput.style.display = "block";  // Show the file input container
    }
}

function toggleCategoryInput() {
    var categorySelect = document.getElementById("id_category");  // Get the category select element
    var newCategoryInput = document.getElementById("id_new_category");  // Get the new category input element

    if (categorySelect.value === "new") {
        newCategoryInput.style.display = "block";  // Show the new category input element
        newCategoryInput.setAttribute("required", "required");  // Set the "required" attribute for form validation
    } else {
        newCategoryInput.style.display = "none";  // Hide the new category input element
        newCategoryInput.removeAttribute("required");  // Remove the "required" attribute
    }
}

function toggleGradeInput() {
    var gradeSelect = document.getElementById("id_grade");  // Get the grade select element
    var newGradeInput = document.getElementById("id_new_grade");  // Get the new grade input element

    if (gradeSelect.value === "new") {
        newGradeInput.style.display = "block";  // Show the new grade input element
        newGradeInput.setAttribute("required", "required");  // Set the "required" attribute for form validation
    } else {
        newGradeInput.style.display = "none";  // Hide the new grade input element
        newGradeInput.removeAttribute("required");  // Remove the "required" attribute
    }
}
