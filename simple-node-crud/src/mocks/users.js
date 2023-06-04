const { v4 } = require('uuid')

const contacts = [
  {
    id: v4(),
    name: 'Chico',
    email: 'chicoze2@hotmail.com',
    phone: '123123123',
    category_id: v4()

  },
  {
    id: v4(),
    name: 'Mario',
    email: 'mariojorgecrz@hotmail.com',
    phone: '965965965',
    category_id: v4()

  },

];

module.exports = contacts