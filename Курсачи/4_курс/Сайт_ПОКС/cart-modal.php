<div class="modal-body">
    <?php if (!empty($_SESSION['cart'])): ?>
        <table class="table">
            <thead>
            <tr>
                <th scope="col">Картинка</th>
                <th scope="col">Название</th>
                <th scope="col">Цена</th>
            </tr>
            </thead>
            <tbody>
            <?php foreach ($_SESSION['cart'] as $id=>$item): ?>
                <tr>
                    <td><a href="#"><img class="cart_img" src="<?= $item['img']?>" alt="<?= $item['name'] ?>"></a></td>
                    <td><a href="#"><?= $item['name'] ?></a></td>
                    <td><?= $item['price'] ?></td>
                </tr>
            <?php endforeach; ?>
            <tr>
                <td colspan="4" align="right">Товаров: <span id="modal-cart-qty">
                        <?= $_SESSION['count'] ?>
                    </span> <br> Сумма: <?= $_SESSION['cart.sum'] ?></td>
            </tr>
            </tbody>
        </table>
    <?php else: ?>
        <p>Корзина пуста</p>
    <?php endif; ?>
</div>
<div class="modal-footer">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
    <?php if (!empty($_SESSION['cart'])): ?>
        <button type="submit" class="btn btn-primary">Оформить заказ</button>
        <button type="button" class="btn btn-danger" id="clear-cart">Очистить корзину</button>
    <?php endif;?>
</div>