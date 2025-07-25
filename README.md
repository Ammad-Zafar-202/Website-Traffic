# 🌐 Website Traffic Analytics for CleanTech Directory

This project implements a complete **website traffic monitoring solution** for the CleanTech Directory platform. It consists of:

1. ✅ **Server-Side Traffic Monitoring (Backend)** – to be integrated into the Node.js backend of the live platform.
2. 🚀 **Pilot Streamlit Dashboard (Python)** – to rapidly test and visualize traffic tracking functionality.

---

## 📁 Project Structure

```
/
├── backend_traffic_monitor/     # Node.js traffic tracking middleware and API
└── analytics_pilot_streamlit/  # Python-based mock traffic analytics dashboard
```

---

## ✅ 1. Server-Side Traffic Monitor (`backend_traffic_monitor/`)

This module provides real-time tracking of website visitors using their IP addresses. It performs the following:

### 🔍 Features:
- Logs IP address of visitors
- Estimates **geographic location** using `geoip-lite`
- Simulates **demographic age estimates**
- Stores logs in memory (can be extended to DB)
- Exposes `/api/analytics` endpoint to retrieve logged data

### 🧩 How It Works:
- Uses Express.js middleware to intercept requests
- Captures and logs relevant visitor data
- Appends log to a global variable `global.trafficLogs`
- Makes data available via a GET endpoint

### 🔧 Setup Instructions:
1. Navigate to the backend directory:
   ```bash
   cd backend_traffic_monitor
   npm install
   ```

2. In your main backend server file:
   ```js
   const ipTracker = require('./middleware/ipTracker');
   app.use(ipTracker);
   app.use('/api/analytics', require('./routes/analytics'));
   ```

3. Restart your server and access:
   ```
   GET http://localhost:5000/api/analytics
   ```

---

## 🚀 2. Pilot Test Dashboard (`analytics_pilot_streamlit/`)

This standalone Python dashboard simulates IP visitor data and displays live insights for demonstration purposes.

### 📊 What It Does:
- Simulates visitor IPs
- Calls public IP geolocation API (`ip-api`)
- Estimates age range randomly for demo
- Renders charts using **Streamlit**

### 🧪 Pilot Use Case:
> This pilot demonstrates a **feasibility test** for full-scale implementation. It is useful for:
> - Stakeholder presentation
> - Live prototype demo
> - Testing chart features before backend integration

### 🔧 Setup Instructions:
1. Navigate to the pilot directory:
   ```bash
   cd analytics_pilot_streamlit
   pip install -r requirements.txt
   ```

2. Run the pilot dashboard:
   ```bash
   streamlit run pilot.py
   ```

3. Your browser will launch a local dashboard like:
   ```
   http://localhost:8501
   ```

---

## 🔒 Notes
- Backend module can be extended to store logs in a database (MongoDB, PostgreSQL).
- Geo estimation accuracy depends on IP data and may require compliance review for production use.
- Age estimates in pilot are simulated; integrate real auth or analytics data for accuracy.

---

## 💡 Future Improvements
- Add browser fingerprinting or cookie-based session tracking
- Connect backend logs to a Mongo/Postgres DB
- Enhance dashboard with time-series analytics (by hour/day/month)
- Integrate with Gemini-based chat assistant for personalized engagement

---

## 🤝 Contribution & License

This is part of the **CleanTech Directory Platform**. For collaboration or integration assistance, contact the development team.