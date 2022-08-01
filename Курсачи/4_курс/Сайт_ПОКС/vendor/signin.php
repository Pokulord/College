<?php
    require_once '../connect.php';
    session_start();
    $login_in = $_POST['login_in'];
    $pass_in = $_POST['pass_in'];

    $check = mysqli_query($connect,"SELECT * FROM `users` WHERE `login`='$login_in' and `password` = '$pass_in'");
    if (mysqli_num_rows($check) > 0) {

        $user = mysqli_fetch_assoc($check);

        $_SESSION['user'] = [
            "login" => $user['login'],
            "pass" => $user['password'],
            "admin" => $user['admin']
        ];

        $response = [
            "status" => true
        ];
        echo  json_encode($response);
    } else {
        $response = [
            "status" => false
        ];
        echo  json_encode($response);
    }

    ?>