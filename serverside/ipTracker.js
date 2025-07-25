const geoip = require('geoip-lite');

module.exports = function ipTracker(req, res, next) {
  const ip = req.headers['x-forwarded-for']?.split(',')[0] || req.ip;
  const geo = geoip.lookup(ip) || {};
  const ageEstimate = ['18‑25','26‑35','36‑50','50+'][Math.floor(Math.random()*4)];
  const logEntry = {
    ip,
    country: geo.country || 'Unknown',
    region: geo.region || 'Unknown',
    city: geo.city || 'Unknown',
    ageEstimate,
    timestamp: new Date().toISOString()
  };
  console.log('Traffic Log:', logEntry);
  if (!global.trafficLogs) global.trafficLogs = [];
  global.trafficLogs.push(logEntry);
  next();
};