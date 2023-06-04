const { Router } = require('express')
const router = Router()

// import controllers
const contactController = require('./app/controllers/contactController')
const categoryController = require('./app/controllers/categoryController')

// import middlewares

// router.get('/contacts', contactController.index);
router.get(  '/contacts',  contactController.index);
router.get('/contacts/:id', contactController.show);
router.delete('/contacts/:id', contactController.delete);
router.post('/contacts/', contactController.store);
router.put('/contacts/:id', contactController.update);

router.get('/categories', categoryController.index);
router.get('/categories/:id', categoryController.show);
router.post('/categories', categoryController.store);
router.delete('/categories/:id', categoryController.delete);
router.put('/categories/:id', categoryController.update);

module.exports = router;