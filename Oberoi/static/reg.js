document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    displayConfirmation();
});

function displayConfirmation() {
 
    const form = document.getElementById('registrationForm');
    form.innerHTML = '<div class="confirmation-message">Thank you for your submission. We will review your application and verify it shortly.</div>';
}