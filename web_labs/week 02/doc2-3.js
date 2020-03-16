/**@const {string} */ const hiWord = 'Hello';
/**
 * Возврвщает приветствие
 * принимает строку или ничто, в случае ничто возвращает безымянное приветствие
 */
function sayHello(name = 'Nameless'){
    return '${hiWord}, ${name}!';
}
console.log(sayHello());
console.log(sayHello());