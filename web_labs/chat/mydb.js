const {model} = require('mongoose');

const schema = {
    username:{
        type: String,
        required: true
    },
    coments:{
        type: String,
        required: true
    }
};

module.exports = model('mydb', schema); 
