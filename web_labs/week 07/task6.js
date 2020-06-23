const sum = (...numbers) => numbers.reduce((x, y) => x+y);

console.log(`Sum: ${sum(5, 7, 2, 1)}`)
console.log(`Sum: ${sum(7, 5, 3)}`)
console.log(`Sum: ${sum(3, 4)}`)