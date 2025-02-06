document.addEventListener("DOMContentLoaded", function() {
    console.log("Page loaded successfully!");

    document.querySelectorAll(".category-card").forEach(card => {
        card.addEventListener("mouseover", () => {
            card.classList.add("hovered");
        });
        card.addEventListener("mouseout", () => {
            card.classList.remove("hovered");
        });
    });
});
