<?php
session_start();
unset($_SESSION['user']);

$response = [
    "status" => true
];
echo  json_encode($response);