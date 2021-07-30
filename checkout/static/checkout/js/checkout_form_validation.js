// On clicking the submit button, grab all form's required fields
// and for each of them check if is not valid. 
// If not valid add "invalid-field" class and if it doesnt already
// have the error message span element, add it.
// Else if valid and has the error message span element, remove invalid
// class and span element.
document.getElementById('submit-button').addEventListener('click', () => {
    let requiredField = document.querySelectorAll('[required]');
    requiredField.forEach((field) => {
        if(!field.validity.valid) {
            field.classList.add('invalid-field');
            if(!document.getElementById(`remove_${field.name}`)) {
                field.insertAdjacentHTML("afterEnd", `<span id="remove_${field.name}" class='text-danger invalid-text'>${field.title}</span>`);
            }
        } else if(field.validity.valid && document.getElementById(`remove_${field.name}`)) {
            field.classList.remove('invalid-field');
            document.getElementById(`remove_${field.name}`).remove()
        }
    });
    // On clicking submit button also add a "change" event to listen to
    // validation.
    form.addEventListener('change', () => {
        let requiredField = document.querySelectorAll('[required]');
        requiredField.forEach((field) => {
            if(!field.validity.valid) {
                field.classList.add('invalid-field');
                if(!document.getElementById(`remove_${field.name}`)) {
                    field.insertAdjacentHTML("afterEnd", `<span id="remove_${field.name}" class='text-danger invalid-text'>${field.title}</span>`);
                }
            } else if(field.validity.valid && document.getElementById(`remove_${field.name}`)) {
                field.classList.remove('invalid-field');
                document.getElementById(`remove_${field.name}`).remove()
            }
        })
    });
});