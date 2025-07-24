
# 🚀 Website Traffic – Deployment Instructions

## 🌐 Frontend Deployment (Vercel)
1. Go to: https://vercel.com
2. Click "New Project" → Select this GitHub repo
3. Set Project Root: frontend
4. Add ENV: REACT_APP_API_URL=https://your-backend-url.up.railway.app
5. Deploy!

## ⚙ Backend Deployment (Railway)
1. Go to: https://railway.app
2. New Project → Connect GitHub
3. Set Root: backend
4. Add `.env`: PORT=3001
5. Enable auto-deploy

## ✅ GitHub Secrets
Go to GitHub → Settings → Secrets → New Secret:
- RAILWAY_TOKEN = your token

## 📁 Project Structure
- frontend/ — React app with dashboard
- backend/ — Node API storing visits
- .github/ — GitHub Actions for CI/CD

Visit your deployed frontend and test analytics logs & export! 🎉
