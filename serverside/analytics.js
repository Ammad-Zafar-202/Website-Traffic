const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json(global.trafficLogs || []);
});

module.exports = router;