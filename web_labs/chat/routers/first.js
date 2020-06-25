const {Router} = require('express');
const mydb = require('../mydb');
const router = Router();

router.get('/', async (req, res) => {
    const db = await mydb.find({});
    res.render('index', {
        title:'main page',
        db
    })
});
router.post('/write', async  (req, res) =>{
    const post = new mydb({
        username:'user1',
        coments: req.body.coment

    });
    await post.save(); 
    res.redirect('/');
});

module.exports = router;
