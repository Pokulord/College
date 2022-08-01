async function load_elec() {
    const response= await fetch('./empdata.json');
    const names = await response.text();
    console.log('Тут');
    console.log(names);
    return names;
}
var res_el=load_elec();

var CATALOG_ELEC =[
    {
        id: "el1",
        name: "IBANEZ GRX70QA-TRB",
        img: "img/guitars/IBANEZ GRX70QA-TRB.jpg",
        price: 23000,
    },
    {
        id: "el2",
        name: "GIBSON 2019 LES PAUL TRIBUTE SATIN",
        img: "img/guitars/GIBSON 2019 LES PAUL TRIBUTE SATIN.png",
        price: 10000,
    },
    {
        id: "el3",
        name: "FENDER American Performer Stratocaster HSS RW",
        img: "img/guitars/FENDER American Performer Stratocaster HSS RW.jpg",
        price: 159000,
    },
    {
        id: "el4",
        name: "YAMAHA PACIFICA 311H",
        img: "img/guitars/YAMAHA PACIFICA 311H.jpg",
        price: 44000,
    },
    {
        id: "el5",
        name: "IBANEZ GRX40-MGN",
        img: "img/guitars/IBANEZ GRX40-MGN.jpeg",
        price: 15000,
    },
    {
        id: "el3",
        name: "GIBSON 2019 LES PAUL TRIBUTE SATIN",
        img: "img/guitars/GIBSON 2019 LES PAUL TRIBUTE SATIN.png",
        price: 100000,
    },

];


const CATALOG_ACOUSTIC = [
    {
        id: "id1",
        name: "YAMAHA F310" ,
        img: "img/guitars/YAMAHA F310.jpg" ,
        price: 12000 ,
    },
    {
        id: "id2",
        name: "EPIPHONE J-200 EC Studio" ,
        img: "img/guitars/EPIPHONE J-200 EC Studio.jpg" ,
        price: 50000 ,
    },
    {
        id: "id3",
        name: "FENDER CD-60S" ,
        img: "img/guitars/FENDER CD-60S.jpg" ,
        price: 26000 ,
    }
]

const CATALOG_BASS = [
    {
        id: "idb1",
        name: "FENDER SQUIER Affinity 2021",
        img: "img/guitars/FENDER SQUIER Affinity 2021.jpeg",
        price: 33000
    },
    {
        id: "idb2",
        name: "YAMAHA TRBX304",
        img: "img/guitars/YAMAHA TRBX304.jpg",
        price: 33000
    },
    {
        id: "idb3",
        name: "IBANEZ GIO GSR206B-WNF",
        img: "img/guitars/IBANEZ GIO GSR206B-WNF.jpg",
        price: 40000
    },
]