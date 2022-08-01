<?php
$connect = mysqli_connect('localhost','root','','shop');


if (!$connect) {
    die ("Error");
}
$res = mysqli_query($connect,"SELECT `id`,`name`,`img`,`price` from `catalog` WHERE `category` = 'elec'");
$res_acoustic = mysqli_query($connect,"SELECT `id`,`name`,`img`,`price` from `catalog` WHERE `category` = 'acoustic'");
$res_bass = mysqli_query($connect,"SELECT `id`,`name`,`img`,`price` from `catalog` WHERE `category` = 'bass'");
$res_all = mysqli_query($connect,"SELECT * from `catalog`");
?>