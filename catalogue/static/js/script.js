// Создание переменной finalPrice, которая содержит в себе путь к классу finalPrice
let finalPrice = document.querySelector('.finalPrice');
finalPrice = parseInt(finalPrice.innerText);
// Находим все элементы класса product-box по действию click
$(".product-box").on("click", function() {
    // Создание переменной parameterPrice, которая содержит в себе путь к классу parameterPrice и превращающее значение этого класса в числовое
    let parameterPrice = parseInt($(this).parent().find('.parameterPrice').html());
    let checkBox = 'none';
    // Если checbox - checked, то...
    if ($(this).is(":checked")) {
        let checkBox = "CHECK"
        // К элементу добавляется класс check и удаляется класс uncheck
        $(this).addClass("check")
        $(this).removeClass("uncheck")
        // Перезаписывание переменной finalPrice. Теперь она содержит сумму значений переменных finalPrice и parameterPrice
        finalPrice = finalPrice + parameterPrice
        console.log(finalPrice)
        // Замена числовых значений в классе finalPrice
        $('.finalPrice').html(finalPrice)
        // console.log(parseFloat(finalPriceElem.innerText))
    }
    // Иначе...
    else { 
        let checkBox = "UNCHECK"
        // К элементу добавляется класс uncheck и удаляется класс check
        $(this).addClass("uncheck")
        $(this).removeClass("check")
        // Перезаписывание переменной finalPrice. Теперь она содержит разность значений переменных finalPrice и parameterPrice
        finalPrice = finalPrice - parameterPrice
        console.log(finalPrice)
        // Замена числовых значений в классе finalPrice
        $('.finalPrice').html(finalPrice)
        // console.log(parseFloat(finalPriceElem.innerText))
    }
})


$("#basket_form").submit(function(e) {
    // Зупиняємо стандартну подію - відправку форми
    e.preventDefault(); 
    $.ajax({
        // Вказуємо метод запиту POST
        type: "POST", 
        // URL-адресу для відправки запиту беремо з елементу з класом 'url'
        url: $('.url').val(), 
        // Дані для відправки беремо з форми методом serialize()
        data: $(this).serialize(), 
        success: function() {   
            $('.modal-overlay-basket').css('display', 'flex');
            $('.tag span').html( +$('.tag span').html() + 1)
        }
    });
});

$('.times_div').click(function() {
    $('.modal-overlay-basket').css('display', 'none'); // Приховуємо модальне вікно
});