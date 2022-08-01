<?php
 include 'connect.php';
 echo "Заказ";
 session_start();
 print_r($_SESSION['cart']);
 foreach ($_SESSION['cart'] as $item) {
     $item_name = $item['name'];
     mysqli_query($connect,"DELETE FROM `catalog` WHERE name = '$item_name' ");
 }

unset($_SESSION['cart']);
unset($_SESSION['cart.sum']);
unset($_SESSION['count']);
 echo "<script>alert('Заказ оформлен!');
 location.href='https://localhost/Site_Chernikov/index.php';</script>"
?>