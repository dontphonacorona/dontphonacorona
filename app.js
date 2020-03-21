
const express = require('express');
const app = express();
const api = require('./routes/api');

const PORT = process.env.PORT || 3000

// serve public http frontend
app.use('/', express.static('public', {extensions:['html']}));
// serve api routes
app.use('/api', api);



app.listen(PORT, function () {
  console.log(`dontphonacorona running on port ${PORT}!`);
});