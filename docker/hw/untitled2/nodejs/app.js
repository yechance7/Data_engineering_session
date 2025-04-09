const express = require('express');
const mysql = require('mysql2/promise');
const app = express();
const port = 3000;

app.use(express.json());

const dbConfig = {
    host: process.env.MYSQL_HOST || 'localhost',
    user: process.env.MYSQL_USER || 'root',
    password: process.env.MYSQL_PASSWORD || 'password',
    database: process.env.MYSQL_DATABASE || 'mydb',
};

async function initializeDatabase() {
    const connection = await mysql.createConnection(dbConfig);

    await connection.execute(`
    CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL
    );
  `);
    connection.end();
    console.log('Users table ensured.');
}

initializeDatabase();

app.use(express.json());

app.post('/users', async (req, res) => {
    try {
        const {name, email} = req.body;
        const connection = await mysql.createConnection(dbConfig);
        const [result] = await connection.execute('INSERT INTO users (name, email) VALUES (?, ?)', [name, email]);
        res.status(201).json({id: result.insertId, name, email});
    } catch (err) {
        console.error('Error inserting user:', err);
        res.status(500).send('Server Error');
    }
});

app.get('/users', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM users');
        res.json(rows);
    } catch (err) {
        console.error('Error fetching users:', err);
        res.status(500).send('Server Error');
    }
});

app.listen(port, () => {
    console.log(`App running on http://localhost:${port}`);
});
