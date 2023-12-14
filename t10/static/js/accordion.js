document.addEventListener("DOMContentLoaded", function () {
    const accordions = document.querySelectorAll(".accordion");
  
    accordions.forEach((accordion) => {
      const header = accordion.querySelector(".accordion-header");
      const content = accordion.querySelector(".accordion-content");
  
      header.addEventListener("click", () => {
        content.style.maxHeight = content.style.maxHeight
          ? null
          : content.scrollHeight + "px";
        header.classList.toggle("active");
      });
    });
  });