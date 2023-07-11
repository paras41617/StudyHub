function toggleInputField() {
    var materialType = document.getElementById("id_material_type");
    var urlInput = document.getElementById("url-input");
    var fileInput = document.getElementById("file-input");

    if (materialType.value === "url") {
        urlInput.style.display = "block";
        fileInput.style.display = "none";
    } else if (materialType.value === "file") {
        urlInput.style.display = "none";
        fileInput.style.display = "block";
    }
}

function toggleCategoryInput() {
    var categorySelect = document.getElementById("id_category");
    var newCategoryInput = document.getElementById("id_new_category");

    if (categorySelect.value === "new") {
        newCategoryInput.style.display = "block";
        newCategoryInput.setAttribute("required", "required");
    } else {
        newCategoryInput.style.display = "none";
        newCategoryInput.removeAttribute("required");
    }
}

function toggleGradeInput() {
    var gradeSelect = document.getElementById("id_grade");
    var newGradeInput = document.getElementById("id_new_grade");

    if (gradeSelect.value === "new") {
        newGradeInput.style.display = "block";
        newGradeInput.setAttribute("required", "required");
    } else {
        newGradeInput.style.display = "none";
        newGradeInput.removeAttribute("required");
    }
}
