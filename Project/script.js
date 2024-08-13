const mysql = require('mysql2');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'nst'
});

// Connect to the database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err.stack);
    return;
  }
  console.log('Connected to the database.');
});

// Create a table
const createTableQuery = `CREATE TABLE IF NOT EXISTS bio (
  Name VARCHAR(255),
  Age INT
)`;
connection.query(createTableQuery, (err, results, fields) => {
  if (err) {
    console.error('Error creating table:', err.stack);
    return;
  }
  console.log('Table created or already exists.');
});

// Insert data into the table
const insertQuery = 'INSERT INTO bio (Name, Age) VALUES ?';
const values = [
  ['anu', 12],
  ['Arun', 43],
  ['Durai', 34]
];
connection.query(insertQuery, [values], (err, results, fields) => {
  if (err) {
    console.error('Error inserting data:', err.stack);
    return;
  }
  console.log('Data inserted.');
});

// Select data from the table
const selectQuery = 'SELECT * FROM bio';
connection.query(selectQuery, (err, results, fields) => {
  if (err) {
    console.error('Error selecting data:', err.stack);
    return;
  }
  console.log('Selected data:', results);
});

// Update data in the table
const updateQuery = "UPDATE bio SET Name='AJAY' WHERE Age=43";
connection.query(updateQuery, (err, results, fields) => {
  if (err) {
    console.error('Error updating data:', err.stack);
    return;
  }
  console.log('Data updated.');
});

// Delete data from the table
const deleteQuery = 'DELETE FROM bio WHERE Age=12';
connection.query(deleteQuery, (err, results, fields) => {
  if (err) {
    console.error('Error deleting data:', err.stack);
    return;
  }
  console.log('Data deleted.');
});

// Close the connection
connection.end((err) => {
  if (err) {
    console.error('Error ending the connection:', err.stack);
    return;
  }
  console.log('Connection closed.');
});
