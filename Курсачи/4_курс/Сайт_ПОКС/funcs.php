<?php
    function debug(array $data): void {
        echo "<pre>".print_r($data,1)."</pre>";
    }

    function get_products(): array {
        global $res;
        for ($set = array (); $row = $res->fetch_assoc(); $set[] = $row);
        return $set;

    }
    function get_acoutic(): array {
        global $res_acoustic;
        for ($set = array (); $row = $res_acoustic->fetch_assoc(); $set[] = $row);
        return $set;

    }
    function get_bass(): array {
        global $res_bass;
        for ($set = array (); $row = $res_bass->fetch_assoc(); $set[] = $row);
        return $set;

    }

    function get_all(): array {
        global $res_all;
        for ($set = array (); $row = $res_all->fetch_assoc(); $set[] = $row);
        return $set;
    }

    function get_product(string $id) : array
    {
        global $connect;
        $stmt = mysqli_query($connect,"SELECT * FROM `catalog` WHERE `id` LIKE '$id'");
        $stmt = mysqli_fetch_assoc($stmt);
        return $stmt;
    }

    function add_to_cart($product): void
    {
        if (isset($_SESSION['cart'][$product['id']])) {
            return;
        } else {
            $_SESSION['cart'][$product['id']] = [
              'name' => $product['name'],
              'price' => $product['price'],
              'img' => $product['img'],
            ];
        }
        $_SESSION['cart.sum'] = !empty($_SESSION['cart.sum']) ? $_SESSION['cart.sum'] + $product['price'] : $product['price'];
        $_SESSION['count'] = count($_SESSION['cart']);
    }
?>