$(document).ready(function() {
    $('.burger').click(function(event) {
        $('.burger,.menu').toggleClass('active');
    });
    $('.link').click(function(event) {
        $('.burger,.menu').removeClass('active');
    });
});

let menuLinks = document.querySelectorAll('.link');

for (let menuLink of menuLinks) {
    menuLink.addEventListener('click', (e) => {
        e.preventDefault();
        let scrollToElem = menuLink.getAttribute('href');
        let coordinates = document.querySelector(scrollToElem).offsetTop;
        window.scrollTo({
            top: coordinates,
            behavior: 'smooth'
        });
    })
}

//Добавление в корзину

$(function (){

    function showCart(cart) {
        $('#cart-modal .modal-cart-content').html(cart);
        $('#cart-modal').modal();
        let cartQty = $('#modal-cart-qty').text() ? $('#modal-cart-qty').text() : 0;
        $('.mini-cart-qty').text(cartQty);
    }

    $('.pb').on('click',function (e){
        e.preventDefault();
        console.log("click");
        let id = $(this).data('id');
        console.log(id);

        $.ajax({
            url: 'cart.php',
            type: 'GET',
            data: {cart:'add',id:id},
            dataType: 'json',
            success: function (res) {
                console.log(res);
                alert ('OK');
                showCart(res.answer);
            },
            error: function () {
               alert ('Error');
            }
        });
    });

    $('#get-cart').on('click',function (e){
        e.preventDefault();
        console.log("click");

        $.ajax({
            url: 'cart.php',
            type: 'GET',
            data: {cart:'show'},
            success: function (res) {
                showCart(res);
            },
            error: function () {
                alert ('Error');
            }
        });
    });

    $('#cart-modal .modal-cart-content').on('click', '#clear-cart',function (){
        $.ajax({
            url: 'cart.php',
            type: 'GET',
            data: {cart:'clear'},
            success: function (res) {
                console.log(res);
                alert ('OK');
                showCart(res);
            },
            error: function () {
                alert ('Error');
            }
        });
    });
    $('#formlog').submit(function(e){
        e.preventDefault();
        let login = $('input[name="login_in"]').val(),
            pass = $('input[name="pass_in"]').val();

        $.ajax({
            url: 'vendor/signin.php',
            type: 'POST',
            dataType: 'json',
            data: {
                login_in: login,
                pass_in:pass
            },
            success (data) {
                if (data.status != true) {
                    alert("Неверные логин или пароль");
                }
                else {
                    document.location.href = 'index.php';
                }
            }
        });

    });

    $('#admin_form').submit(function(e) {
        e.preventDefault();
        let price = $('input[name="admin_price"]').val(),
            guitar= $('select[name="guitar"]').val();

        $.ajax({
            url: 'admin.php',
            type: 'POST',
            dataType: 'json',
            data: {
                admin_price: price,
                guitar: guitar
            },
            success(data) {
                if (data.status != true) {
                    alert('Введите данные корректно');
                }
                else {
                    alert('OK');
                }
            }
        });
    });

    $('.menu').on('click','#logout',function (e) {
        e.preventDefault();
        $.ajax({
            url: 'logout.php',
            type: 'POST',
            dataType: 'json',
            data: {
                act: 'logout'
            },
            success(data){
                if (data.status == true) {
                    document.location.href = 'index.php';
                }
            }
        });

    }) ;
});

//Ссылки на сайты партнёров
function Fender () {
    window.open("https://fender.ru/");
}

function Gibson () {
    window.open("https://www.gibson.com/en-US/");
}

function Cort () {
    window.open("https://www.cortguitars.com/");
}

function Yamaha () {
    window.open("https://ru.yamaha.com/index.html");
}

function Martinez () {
    window.open("http://www.martinezguitars.eu/");
}

function Ibanez () {
    window.open("https://www.ibanez.com/eu/");
}

function Vk () {
    window.open ('https://vk.com/id300791559');
}

function Telega() {
    window.open('https://t.me/Pokulord');
}
