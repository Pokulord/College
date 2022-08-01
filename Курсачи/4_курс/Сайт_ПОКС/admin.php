<?php
include_once 'connect.php' ;
$guitar = $_POST['guitar'];
$price = $_POST['admin_price'];

if (preg_match('/^\+?\d+$/', $price)) {
    if ($price>0){

        mysqli_query($connect,"UPDATE `catalog` SET `price`= '$price' WHERE `name` = '$guitar'");
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
} else {
    $response = [
        "status" => false
    ];
    echo  json_encode($response);
}



?>