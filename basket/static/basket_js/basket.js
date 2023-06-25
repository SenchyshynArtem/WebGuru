$(document).ready(function () {
  $(".close").click(function () {
    $(".modal-overlay").fadeOut();
  });

  $("#comment-form").submit((e) => {
    e.preventDefault();
    $.ajax({
      type: "POST",
      url: $("#comment-form").attr("action"),
      data: $("#comment-form").serializeArray(),
      success: () => {
        window.location.href = $("#show_basket").val();
      },
    });
  });
});

let finalBasketPrice = document.querySelector(".final-price");
finalBasketPrice = parseInt(finalBasketPrice.innerText);

$(".product-box").on("click", function () {
  let paramPrice = parseInt($(this).parent().find(".parameterPrice").html());
  let parameterPk = $(this).val();
  let productPk = $(this).parent().find(".productPk").val();
  let check = 1;
  if ($(this).is(":checked")) {
    $(this).addClass("check");
    $(this).removeClass("uncheck");
    finalBasketPrice = finalBasketPrice + paramPrice;
    console.log(finalBasketPrice);
    $(".final-price").html(finalBasketPrice);
    check = "uncheck";
  } else {
    $(this).addClass("uncheck");
    $(this).removeClass("check");
    finalBasketPrice = finalBasketPrice - paramPrice;
    console.log(finalBasketPrice);
    $(".final-price").html(finalBasketPrice);
    check = "check";
  }

  const csrf = $("main").find("input[name=csrfmiddlewaretoken]");
  $.ajax({
    type: "POST",
    url: $("#show_basket").val(),
    data: {
      csrfmiddlewaretoken: csrf.val(),
      check: check,
      parameterPk: parameterPk,
      productPk: productPk,
    },
    success: function () {},
  });
});

$(document).ready(function () {
  $(".delete_from_basket").click(function (e) {
    // let checkedPrice1 = document.querySelectorAll('.check');
    const csrf = $("main").find("input[name=csrfmiddlewaretoken]");
    const pk_product = $(this).val();

    //
    // let product = $(this).find(`.product_price_${pk_product}`).find('.check');
    // let product = document.querySelectorAll(`.product_price_${pk_product} .check`);
    let product_price = $(this).find(".product_price").html();
    let checkedPrice = document.querySelectorAll(`.check`);
    product_price = parseInt(product_price);

    let fullProductPrice = 0;

    for (var i = 0; i < checkedPrice.length; ++i) {
      var price = checkedPrice[i];
      price = price.innerHTML;
      price = parseInt(price);
      fullProductPrice = fullProductPrice + price;
    }

    fullProductPrice = fullProductPrice + product_price;

    $.ajax({
      type: "POST",
      url: $("#url_delete_from_basket").val(),
      data: { csrfmiddlewaretoken: csrf.val(), pk_product: pk_product },
      success: function (response) {
        $(".final-price").html(response.full_price);
        $(".tag span").html(+$(".tag span").html() - 1);
        const product_elem = document.querySelector(
          `#product_in_basket_${pk_product}`
        );
        product_elem.remove();
        if (document.querySelector(".del_products") == null) {
          window.location.href = $("#show_basket").val();
        }
      },
    });
  });
});

$(".show_form").click(function () {
  $(".form").css("display", "flex");
});

$(".times p").click(function () {
  $(".form").css("display", "none");
});

$(".times-sign").click(function () {
  $(".modal-overlay").css("display", "none");
});
