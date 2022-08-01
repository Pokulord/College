<?php
 session_start();
?>
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
<div class="container">
    <form action="vendor/signup.php" method="post" class="form_reg">
        <div class="form-group">
            <label class="label" for="formGroupExampleInput">Логин</label>
            <input type="text" class="form-control" id="formGroupExampleInput" name="login_reg" placeholder="Введите логин">
        </div>
        <div class="form-group">
            <label class="label" for="formGroupExampleInput2">Пароль</label>
            <input type="password" class="form-control" id="formGroupExampleInput2" name="pass-reg" placeholder="Введите пароль">
            <label class="label" for="formGroupExampleInput2">Подтверждение</label>
            <input type="password" class="form-control" id="formGroupExampleInput3" name="pass-regconf" placeholder="Подтвердите пароль">
        </div>
        <button type="submit" id="signinbut" class="btn btn-primary">Регистрация</button>
        <p class="toreg">
            Уже зарегистрированы?- <a class="linktolog" href="index.php">авторизуйтесь</a>
        </p>
            <?php
                if ($_SESSION['message']) {
                    echo '<p class="msg">' . $_SESSION['message'] . '</p>';
                }
                    unset($_SESSION['message']);

            ?>
    </form>
</div>
