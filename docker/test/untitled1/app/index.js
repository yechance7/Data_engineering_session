const express = require('express');
const redis = require('redis');
const app = express();
const port = 3000;

const client = redis.createClient({
    host: 'redis',
    port: 6379
});

client.on('error', (err) => {
    console.log('Redis error:', err);
});

app.get('/counter', (req, res) => {
    client.get('counter', (err, counter) => {
        if (err) {
            res.status(500).send('Error reading counter from Redis');
            return;
        }
        res.send(`Counter value is ${counter}`);
    });
});

app.post('/counter/increment', (req, res) => {
    client.incr('counter', (err, counter) => {
        if (err) {
            res.status(500).send('Error incrementing counter in Redis');
            return;
        }
        res.send(`Counter incremented to ${counter}`);
    });
});

app.listen(port, () => {
    console.log(`App running on http://localhost:${port}`);
});
