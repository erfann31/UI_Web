function showColumn(columnId) {
  var columns = document.querySelectorAll(".contexts");
  columns.forEach(function (column) {
    column.style.display = "none";
  });

  var selectedColumn = document.getElementById(columnId);
  if (selectedColumn) {
    selectedColumn.style.display = "flex";
  }

  var buttons = document.querySelectorAll(".nav-button");
  buttons.forEach(function (button) {
    button.classList.remove("active");
  });

  var clickedButton = document.getElementById("button-" + columnId);
  if (clickedButton) {
    clickedButton.classList.add("active");
  }
}

