let product = document.querySelectorAll('img');
let cart = document.querySelector('.cart');
let clrButton = document.querySelector('button');
let priceBlock = document.querySelector('#p-price');
let idProduct, price = 0;

clrButton.addEventListener('click', event =>{
    cart.innerHTML = '';
    price = 0;
    priceBlock.textContent = `Price: ${price}`;
});
product.forEach(el => el.addEventListener('drag', event =>{
    idProduct = event.target.id;
}));
cart.addEventListener('dragenter', (event) =>{
   cart.style.background = 'red';
});
cart.addEventListener('dragleave', (event) =>{
    cart.style.background = 'cornsilk';
});
cart.addEventListener('dragover', (event)=> {
    event.preventDefault();
}); 
cart.addEventListener('drop', (event) =>{
    price += Number(document.getElementById(idProduct).alt);
    priceBlock.textContent = `Price: ${price}`;
    cart.innerHTML += event.dataTransfer.getData('text/html')
    cart.style.background = 'cornsilk';
});
