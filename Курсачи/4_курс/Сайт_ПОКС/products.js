//Формируем класс товаров 

class Products {

    constructor() {
        this.classNameActive = 'products-element__btn_active';
        this.labelAdd = 'В корзину';
        this.labelRemove = 'В корзине';
    }

    handle(elem,id) {
       const {pushProduct,products} =  localStorageUtil.putProducts(id);

       if (pushProduct) {
           elem.classList.add(this.classNameActive);
           elem.innerHTML = this.labelRemove;
       } else {
            elem.classList.remove(this.classNameActive);
            elem.innerHTML = this.labelAdd;
       }
    }
    render() {
        const productStore =  localStorageUtil.getProducts();
        let htmlCatalog = '';

        CATALOG_ELEC.forEach(({id,name,price,img}) => {
            let activeClass = '';
            let activeText = '';
            // Проверка на то, есть ли этот id в списке
            if (productStore.indexOf(id) === -1) {
                activeText = this.labelAdd;
            //если есть
            } else {
                activeClass = " " + this.classNameActive;
                activeText= this.labelRemove;
            }
            htmlCatalog += `
            <li class="products-element">
                <span class = "products-element__name">${name}</span>
                <img class = "products-element__image" src="${img}">
                <span class = "products-element__price">${price} руб
                <button class = "products-element__btn${activeClass}" onclick="productsPage.handle(this,'${id}')">
                    ${activeText}
                </button>
                </span>
            </li>
            `;
        });

        const html = `
            <ul class="products-container">
                ${htmlCatalog}
            </ul>
        `;
        document.getElementById("goods").innerHTML = html;

        htmlCatalog = '';

        CATALOG_ACOUSTIC.forEach(({id,name,price,img}) => {
            let activeClass = '';
            let activeText = '';
            if (productStore.indexOf(id) === -1) {
                activeText = this.labelAdd;
            } else {
                activeClass = " " + this.classNameActive;
                activeText= this.labelRemove;
            }
            htmlCatalog += `
            <li class="products-element">
                <span class = "products-element__name">${name}</span>
                <img class = "products-element__image" src="${img}">
                <span class = "products-element__price">${price} руб
                <button class = "products-element__btn${activeClass}" onclick="productsPage.handle(this,'${id}')">
                ${activeText}</button>
                </span>
            </li>
            `;
        });

         const htmla = `
            <ul class="products-container">
                ${htmlCatalog}
            </ul>
        `;
        document.getElementById("goods-acoustic").innerHTML = htmla;

        htmlCatalog = '';

        CATALOG_BASS.forEach(({id,name,price,img}) => {
            let activeClass = '';
            let activeText = '';
            if (productStore.indexOf(id) === -1) {
                activeText = this.labelAdd;
            }
            else {
                activeClass = " " + this.classNameActive;
                activeText = this.labelRemove;
            }
            htmlCatalog += `
            <li class="products-element">
                <span class = "products-element__name">${name}</span>
                <img class = "products-element__image" src="${img}">
                <span class = "products-element__price">${price} руб
                <button class = "products-element__btn${activeClass}" onclick= "productsPage.handle(this,'${id}')">
                ${activeText}</button>
                </span>
            </li>
            `;
        });

        const htmlb = `
        <ul class="products-container">
            ${htmlCatalog}
        </ul>
    `;

    document.getElementById('goods-bass').innerHTML = htmlb;
    }

}

const productsPage = new Products();
productsPage.render();