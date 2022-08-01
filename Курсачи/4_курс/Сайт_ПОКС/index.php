<?php
    error_reporting(-1);
    session_start();
    require_once 'connect.php';
    require_once 'funcs.php';
    $products= get_products();
    $acoutic_g = get_acoutic();
    $bass_g = get_bass();
    $g_all = get_all();
    debug($_SESSION);
    //$_SESSION['login'] = 'karasik';
    //$_SESSION['pass'] = "123";
    //unset($_SESSION['login']);
    //unset($_SESSION['user']);
    //session_destroy();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Музыкальный магазин</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <link href="style.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/smoothscroll/1.4.10/SmoothScroll.min.js" integrity="sha256-huW7yWl7tNfP7lGk46XE+Sp0nCotjzYodhVKlwaNeco=" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    
<script>
SmoothScroll({
    // Время скролла 400 = 0.4 секунды
    animationTime    : 400,
    // Размер шага в пикселях 
    stepSize         : 75,

    // Дополнительные настройки:
    
    // Ускорение 
    accelerationDelta : 30,  
    // Максимальное ускорение
    accelerationMax   : 2,   

    // Поддержка клавиатуры
    keyboardSupport   : true,  
    // Шаг скролла стрелками на клавиатуре в пикселях
    arrowScroll       : 50,

    // Pulse (less tweakable)
    // ratio of "tail" to "acceleration"
    pulseAlgorithm   : true,
    pulseScale       : 4,
    pulseNormalize   : 1,

    // Поддержка тачпада
    touchpadSupport   : true,
})
</script>
<script>
    $(".link").click(function() { // ID откуда кливаем
        $('html, body').animate({
            scrollTop: $(".formwrap").offset().top  // класс объекта к которому приезжаем
        }, 10); // Скорость прокрутки
    });
</script>
    <header id="header" class="header">
        <div class="container">
            <div class="nav">
                <img class="icon" src="img/icon.svg" alt="Фон">
                <div class="burger">
                    <span></span>
                </div>
                <ul class="menu">
                    <li>
                        <a href="#catalog" class="link">Каталог</a>
                    </li>
                    <li>
                        <a href=".about-us" class="link">Партнёры</a>
                    </li>
                    <li>
                        <a href=".footer-line" class="link">Контакты</a>
                    </li>
                    <?php if (!isset($_SESSION['user'])): ?>
                    <li>
                        <button class="btn btn-secondary btn-lg" data-toggle="modal" data-target="#login">Войти</button>
                    </li>
                    <?php endif?>
                    <li>
                        <button type="button" id="get-cart" class="btn btn-primary" data-toggle="modal" data-target="#cart-modal">
                            Корзина <span class="badge badge-light mini-cart-qty"><?= $_SESSION['count'] ?? 0 ?></span>
                        </button>
                    </li>
                    <?php if (isset($_SESSION['user'])):?>
                    <li>
                        <button type="button" class="btn btn-light">Здравствуйте,<?= $_SESSION['user']['login'] ?></button>
                    </li>
                    <li>
                        <button type="button" id="logout" class="btn btn-danger">Выход</button>
                    </li>
                    <?php endif?>
                    <?php if ( isset($_SESSION['user']) and $_SESSION['user']['admin'] == 1) : ?>
                    <li>
                        <button type="button" id="admin-btn" class="btn btn-secondary" data-toggle="modal" data-target="#admin">Админ-панель</button>
                    </li>
                    <?php endif?>
                </ul>
            </div>
            <div id="description" class="description">
                <h1>Продаём гитары
                    <br>высочайшего качества!</h1>
                <h2>У нас закупаются самые<br> лучшие музыканты<br>
                    современности</h2>
            </div>
        </div>
    </header>

    <section id="about" class="about">
        <div class="container">
            <h2>Почему именно мы</h2>
            <div class="why" id="why">
                <div class="why-item">
                    <img class="man" src="img/for_section.png">
                </div>

                <div class="why-box">
                    <div>1.    Частые скидки</div>
                    <div>2.    Высокое качество обслуживания</div>
                    <div>3.    Более 50 филиалов по всей стране</div>
                </div>
            </div>
            <div class="about-us" id="about-us">
                <h2>Наши партнёры</h2>
                <div class="partners" id="partners">
                    <div class="fender-logo">
                        <img src="img/fender.png" onclick="Fender()">
                    </div>
                    <div class="gibsonlogo">
                        <img class="mid_p" src="img/gibson.png" onclick="Gibson()">
                    </div>
                    <div class="cort-logo">
                        <img src="img/cort.png" onclick="Cort()">
                    </div>
                    <div class="yamaha-logo">
                        <img src="img/yamaha.svg" onclick="Yamaha()">
                    </div>
                    <div class="martinez-logo">
                        <img class="mid_p" onclick="Martinez()" src="img/martinez.svg">
                    </div>
                    <div class="ibanez-logo">
                        <img  onclick="Ibanez()" src="img/Ibanez.svg">
                    </div>
                </div>
            </div>
            <div class="catalog" id="catalog">
                <h2>Каталог товаров</h2>
            </div>
            <div class="catalog-header">
                <h3>Электрогитары</h3>

            </div>
            <div id="goods">
                <div class="products-container">
                    <?php if (!empty($products)): ?>
                    <?php foreach ($products as $product): ?>
                    <li class="products-element">
                        <span class = "products-element__name"><?= $product['name']; ?></span>
                        <img class = "products-element__image" src="<?= $product['img'];?>">
                        <span class = "products-element__price"><?= $product['price']; ?> руб
                <a class = "pb" href="?cart=add&id=<?= $product[0] ?>" data-id="<?php echo $product['id']?>">
                    Купить
                </a>
                            <?php endforeach; ?>
                            <?php endif; ?>
                </div>

            </div>
            <div class="catalog-header">
                <h3>Акустические гитары</h3>
            </div>
            <div class="goods-acoustic" id="goods-acoustic">
                <div class="products-container">
                    <?php if (!empty($acoutic_g)): ?>
                    <?php foreach ($acoutic_g as $acoustic): ?>
                    <li class="products-element">
                        <span class = "products-element__name"><?= $acoustic['name']; ?></span>
                        <img class = "products-element__image" src="<?= $acoustic['img'];?>">
                        <span class = "products-element__price"><?= $acoustic['price']; ?> руб
                <a class = "pb" href="?cart=add&id=<?= $acoustic[0] ?>" data-id="<?php echo $acoustic['id']?>">
                    Купить
                </a>
                            <?php endforeach; ?>
                            <?php else:
                                echo "<p>Товаров нет в наличии</p>";

                            ?>
                            <?php endif; ?>
                </div>
            </div>
            <div class="catalog-header">
                <h3>Бас-гитары</h3>
            </div>
            <div class="goods-bass" id="goods-bass">
                <div class="products-container">
                    <?php if (!empty($bass_g)): ?>
                    <?php foreach ($bass_g as $bass): ?>
                    <li class="products-element">
                        <span class = "products-element__name"><?= $bass['name']; ?></span>
                        <img class = "products-element__image" src="<?= $bass['img'];?>">
                        <span class = "products-element__price"><?= $bass['price']; ?> руб
                <a class = "pb" href="?cart=add&id=<?= $bass[0] ?>" data-id="<?php echo $bass['id']?>">
                    Купить
                </a>
                            <?php endforeach; ?>
                            <?php else:
                                echo "<p>Товаров нет в наличии</p>";

                                ?>
                            <?php endif; ?>
                </div>
            </div>
            <div class="reviews">
                <h3>Отзывы</h3>
            </div>
            </div>
        </div>
    </section>
    <footer>
        <div class="container">
            <div class="footer-line">
                <div class="footer-item">
                    <img class="icon" src="img/icon.svg" alt="Фон">
                    <h3>© 2009-2022 Музычерников ™ - музыкальные инструменты, интернет магазин</h3>
                </div>
            </div>
        <div class="contact-links">
            <div class="tel">8(952) 980 8089</div>
        <div class="images">
            <img class="vk-img" tooltip="Наш ВК" src= "img/vk.png" onclick="Vk()">
            <img class="inst-img" src= "img/tg.png" onclick="Telega()">
        </div>
        </div>
        <div class="desc">
            Наш адрес
        </div>
        <div class="map">
            <script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A08b31a1e22ec46349c2eb6fbb805a69db98ed1c9fd6c47f83ea8b8637a14bd59&amp;width=500&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>
        </div>
        </div>
    </footer>
    <div class="modal fade cart-modal" id="cart-modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Корзина</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form action="test.php" method="post">
                    <div class="modal-cart-content">

                    </div>
                </form>

            </div>
        </div>
    </div>
    <div class="modal fade" id="login">
        <div class="modal-dialog modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Логин-панель</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form id="formlog">
                    <div class="form-group">
                        <label class="label" for="formGroupExampleInput">Логин</label>
                        <input type="text" class="form-control" id="formGroupExampleInput" name="login_in" placeholder="Введите логин">
                    </div>
                    <div class="form-group">
                        <label class="label" for="formGroupExampleInput2">Пароль</label>
                        <input type="password" class="form-control" name="pass_in" id="formGroupExampleInput2" placeholder="Введите пароль">
                    </div>
                    <button type="submit" id="signinbut" class="btn btn-primary">Вход</button>
                    <p class="toreg">
                        Ещё не зарегистрированы?- <a class="linktolog" href="register.php">сделайте это</a>
                    </p>
                </form>
            </div>
        </div>
    </div>

    <div class="modal fade cart-modal" id="admin" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Админ-панель</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form class="admin_form" action="admin.php" id="admin_form" method="post">
                    <div class="form-group">
                        <label class="label" for="formGroupExampleInput">Изменение цены</label>
                        <input type="text" class="form-control" id="formGroupExampleInput" name="admin_price" placeholder="Введите Цену">
                        <select class = 'admin_good' name="guitar">
                        <option value="">Выберите товар</option>
                        <?php foreach ($g_all as $item) :?>
                        <option value="<?= $item['name'] ?>"><?= $item['name'] ?> </option>
                        <?php endforeach ?>
                        </select>
                        <button type="submit" id="price_but" class="btn btn-primary">Ввод</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script type="text/javascript" src="script.js"></script>
    <!-- UItoTop plugin -->
<script src="/js/jquery.ui.totop.js" type="text/javascript"></script>
<script src="/js/easing.js" type="text/javascript"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"></script>
<!-- Starting the plugin -->
<script type="text/javascript">
$(document).ready(function() {
/*
var defaults = {
containerID: 'toTop', // fading element id
containerHoverID: 'toTopHover', // fading element hover id
scrollSpeed: 1200,
easingType: 'linear'
};
*/
 
$().UItoTop({ easingType: 'easeOutQuart' });
 
});
</script>
</body>
</html>