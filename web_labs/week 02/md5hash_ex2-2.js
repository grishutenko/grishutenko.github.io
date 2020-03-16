const crypto = require('crypto');
const lock = 'hiden word fghvbn';
let hash = crypto.createHash('md5').update(lock).digest('hex');
console.log(hash);