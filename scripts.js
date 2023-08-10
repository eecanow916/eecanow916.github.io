// Add event listener to handle navigation to the profile creation page
document.addEventListener("DOMContentLoaded", function () {
    const createProfileLink = document.querySelector("#create-profile a");
    createProfileLink.addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "create-profile.html"; // Navigate to the profile creation page
    });
});
