let inputBlock = document.querySelectorAll("input");
let colorArea = document.querySelector('div');
let button = document.querySelector('button');
let value1, value2, value3;

colorArea.style.height = '10rem';
colorArea.style.width = '20rem';
colorArea.style.backgroundColor = 'rgb(000, 000, 000)';

inputBlock[0].addEventListener('input', e => {
    value1 = inputBlock[0].value;
    value2 = inputBlock[1].value;
    value3 = inputBlock[2].value;
    colorArea.style.backgroundColor = `rgb(${value1},${value2},${value3})`;
    });

inputBlock[1].addEventListener('input', e => {
    value1 = inputBlock[0].value;
    value2 = inputBlock[1].value;
    value3 = inputBlock[2].value;
    colorArea.style.backgroundColor = `rgb(${value1},${value2},${value3})`;
    });

inputBlock[2].addEventListener('input', e => {
    value1 = inputBlock[0].value;
    value2 = inputBlock[1].value;
    value3 = inputBlock[2].value;
    colorArea.style.backgroundColor = `rgb(${value1},${value2},${value3})`;
    });
