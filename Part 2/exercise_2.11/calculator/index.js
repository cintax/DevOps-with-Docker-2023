const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// Set up middleware to handle form data
app.use(bodyParser.urlencoded({ extended: false }));

// Serve static files from the public directory
app.use(express.static('public'));

// Handle POST requests to the /calculate endpoint
app.post('/calculate', (req, res) => {
  const num1 = parseFloat(req.body.num1);
  const num2 = parseFloat(req.body.num2);
  const sum = num1 + num2;
  const difference = num1 - num2;
  const product = num1 * num2;
  const quotient = num1 / num2;
  res.send(`
    <html>
      <head>
        <title>Calculator Results</title>
        <link rel="stylesheet" type="text/css" href="style.css">
      </head>
      <body>
        <h1>Calculator Results</h1>
        <p>Num 1: ${num1}</p>
        <p>Num 2: ${num2}</p>
        <p>Sum: ${sum}</p>
        <p>Difference: ${difference}</p>
        <p>Product: ${product}</p>
        <p>Quotient: ${quotient}</p>
        <a href="/">Back</a>
      </body>
    </html>
  `);
});

// Start the server
app.listen(3000, () => {
  console.log('Server is listening on port 3000');
});

