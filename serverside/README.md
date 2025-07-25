# Backend Traffic Monitor

## Setup
```bash
npm install
```

Add middleware and route in your main server file:
```js
const ipTracker = require('./middleware/ipTracker');
app.use(ipTracker);
app.use('/api/analytics', require('./routes/analytics'));
```

## View Traffic Logs
GET /api/analytics