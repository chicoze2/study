const express = require('express');
const routes = require('./routes');
require('express-async-errors');

const app = express();

app.use(express.json())
app.use(routes)

//error handler (no async methods)
app.use((err, request, response, next) => {
  console.log('####  Error handler received ############################')
  console.log(err)
  response.sendStatus(500)
})

app.listen(3000, () => { console.log('🔥 Server running'); });

