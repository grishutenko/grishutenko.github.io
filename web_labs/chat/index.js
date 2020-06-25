const express = require('express');
const mongoose = require('mongoose');
const exphbs = require('express-handlebars'); 
const firstRouter = require('./routers/first');
const modelmydb = require('./mydb');

const PORT = process.env.PORT || 3000;
const app = express();
const hbs = exphbs.create(
    {defaultLayout:'main',
    extname: 'hbs'
}); 

app.engine('hbs', hbs.engine);
app.set('view engine', 'hbs');
app.set('views', 'views');

app.use(express.urlencoded({extended: true}));
app.use(firstRouter);

async function start(){
    try{
        await mongoose.connect(
            'mongodb+srv://pavel:pavel@cluster0-thkfi.mongodb.net/mydb', 
        {
            useNewUrlParser: true,
            useFindAndModify: false,
            useUnifiedTopology: true
        });
        app.listen(PORT, () => console.log('alrady works.'));
    } catch(e){
        console.log(e);
    }
}

start()
