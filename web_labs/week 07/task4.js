const summer = (a, b, c) => a + b + c;
console.log(summer.apply(null, [2, 2, 2]));
console.log(summer(...[2, 2, 2]));