$(document).ready(function () {
  $(".times-sign").click(function () {
    $(".feedback-modal-overlay").hide();
  });

  $(".feedback-button").click(function () {
    $(".feedback-modal-overlay").css("display", "flex");
  });

  $(".open-feedback").click(function () {
    $(".feedback-modal-overlay").css("display", "flex");
  });

  $(".close").click(function () {
    $(".modal-overlay").fadeOut();
  });

  $("#feedback-form").submit((e) => {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: $("#feedback-form").attr("action"),
      data: $("#feedback-form").serializeArray(),
      success: () => {
        $(".modal-overlay").css("display", "flex");
        $(".modal-overlay").fadeIn();
        $("#feedback-form p input, #feedback-form p textarea").val("");
        $(".feedback-modal-overlay").css("display", "none");
      },
    });
  });
});
