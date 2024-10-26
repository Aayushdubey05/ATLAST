// Optional JavaScript for additional validation or interactivity
document.getElementById('user-form').addEventListener('submit', function(event) {
    const age = document.getElementById('age').value;
    const phoneNo = document.getElementById('phoneNo').value;

    if (age <= 0) {
        alert('Age must be a positive number.');
        event.preventDefault();
    }

    // Validate phone number (basic example: 10 digits)
    if (!/^\d{10}$/.test(phoneNo)) {
        alert('Phone number must be 10 digits.');
        event.preventDefault();
    }
});
