<?php
    require_once '../connect.php';
    session_start();
    //
    $login = $_POST['login_reg'];
    $pass = $_POST['pass-reg'];
    $pass_c = $_POST['pass-regconf'];
    if ($pass === $pass_c) {
        if (!empty($login) and (!empty($pass))) {
            $resq = mysqli_query($connect,"SELECT `login` FROM `users`");
            $resq = mysqli_fetch_all($resq);
            foreach ($resq as $item) {
                if ($login == $item[0]) {
                    $_SESSION['message'] = "Такой пользователь уже существует";
                    header('Location: ../register.php');
                    die();
                }
            }
            mysqli_query($connect,"INSERT INTO `users`(`login`, `password`) VALUES ('$login','$pass')");
            $_SESSION['message'] = "Успешная регистрация";
            header('Location: ../register.php');
        } else {
            $_SESSION['message'] = "Заполните все поля";
            header('Location: ../register.php');
        }
    } else {
        $_SESSION['message'] = "Пароли не совпадают";
        header('Location: ../register.php');
    }