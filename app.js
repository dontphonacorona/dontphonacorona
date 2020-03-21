
const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000

// serve public http frontend
app.use('/', express.static('public'));


app.listen(PORT, function () {
  console.log(`dontphonacorona running on port ${PORT}!`);
});