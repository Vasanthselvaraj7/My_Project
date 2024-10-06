// JavaScript to show the dropdown message and hide it after a few seconds
document.addEventListener("DOMContentLoaded", function() {
    const statusMessage = document.getElementById("statusMessage");

    if (statusMessage) {
        // Add the show class to trigger the dropdown
        statusMessage.classList.add("show");

        // Remove the show class after 3 seconds to hide the message
        setTimeout(() => {
            statusMessage.classList.remove("show");
        }, 3000);
    }
});
