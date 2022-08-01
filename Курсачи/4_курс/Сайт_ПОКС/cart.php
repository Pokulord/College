<?php

error_reporting(-1);
session_start();
require_once 'connect.php';
require_once 'funcs.php';


if (isset($_GET['cart'])) {
    switch ($_GET['cart']) {
        case 'add':
            $id = isset($_GET['id']) ?$_GET['id'] : 0 ;
            $product = get_product($id);

            if (!$product) {
                echo json_encode(['code'=>'err','answer'=>"err"]);
            }
            add_to_cart($product);
            ob_start();
            require 'cart-modal.php';
            $cart = ob_get_clean();
            echo json_encode(['code'=>'okay','answer'=>$cart]);
            break;
        case 'show':
            require 'cart-modal.php';
            break;
        case 'clear':
            if (!empty($_SESSION['cart'])) {
                unset($_SESSION['cart']);
                unset($_SESSION['cart.sum']);
                unset($_SESSION['count']);
            }
            require 'cart-modal.php';
            break;
    }
}
