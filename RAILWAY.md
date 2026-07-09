# Railway Deployment Guide - VPN Store Bot

## 📋 Prerequisites

Before deploying to Railway, ensure you have:

1. **GitHub Account** - Repository connected
2. **Railway Account** - https://railway.app
3. **Telegram Bot Tokens** - From @BotFather
4. **PostgreSQL Database** - (Railway will provide)

## 🚀 Deployment Steps

### Step 1: Connect GitHub Repository

1. Go to https://railway.app/dashboard
2. Click "New Project" → "Deploy from GitHub"
3. Select `llpouyagamell-lang/vpn-telegram-bot`
4. Click "Deploy"

### Step 2: Add PostgreSQL Database

1. In Railway Dashboard → "New" → "Database" → "PostgreSQL"
2. Railway automatically sets `DATABASE_URL`
3. No manual configuration needed!

### Step 3: Configure Environment Variables

1. Go to Project → Settings → Variables
2. Add the following:

```env
# Required
USER_BOT_TOKEN=YOUR_USER_BOT_TOKEN_FROM_BOTFATHER
ADMIN_BOT_TOKEN=YOUR_ADMIN_BOT_TOKEN_FROM_BOTFATHER
ENVIRONMENT=production
LOG_LEVEL=INFO

# Optional (defaults provided)
STORAGE_TYPE=local
ENABLE_CACHE=true
CACHE_TTL_SECONDS=300
ENABLE_TRANSACTIONS=true
```

### Step 4: Deploy

1. Railway automatically deploys when you push to GitHub
2. Monitor logs in Railway Dashboard
3. Wait for "Running" status

## 🔍 Verify Deployment

### Check Logs
```bash
# In Railway Dashboard → Logs tab
# Look for:
# "✅ Build completed successfully!"
# "Starting VPN Store Bot on Railway..."
# "Database ready ✓"
# "Both bots are running..."
```

### Test Bot
```bash
# Send message to user bot
/start

# Send message to admin bot
/start
```

## 📊 Project Structure for Railway

```
vpn-telegram-bot/
├── main.py                 # Entry point (Railway runs this)
├── railway.json           # Railway config
├── railway.toml          # Alternative config
├── Procfile              # Process definition
├── runtime.txt           # Python version
├── requirements.txt      # Dependencies
├── build.sh             # Build script
├── start.sh             # Startup script
├── .env.example         # Environment template
├── .env.railway         # Railway-specific env vars
└── ... (rest of project)
```

## ⚙️ Configuration Files Explained

### `railway.json` & `railway.toml`
- Tells Railway how to build and run the app
- Specifies Python 3.12
- Sets command: `python3 -m main`

### `Procfile`
- Alternative format for process definition
- Also specifies: `python3 -m main`

### `runtime.txt`
- Python version: 3.12

### `build.sh`
- Runs during build phase
- Installs dependencies
- Creates necessary directories

### `start.sh`
- Runs after build (optional, configured in Railway)
- Initializes database
- Starts the application

## 🔑 Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `USER_BOT_TOKEN` | ✅ Yes | - | Telegram user bot token |
| `ADMIN_BOT_TOKEN` | ✅ Yes | - | Telegram admin bot token |
| `DATABASE_URL` | ✅ Yes | auto | PostgreSQL connection (set by Railway) |
| `ENVIRONMENT` | ❌ No | production | App environment |
| `LOG_LEVEL` | ❌ No | INFO | Logging level |
| `STORAGE_TYPE` | ❌ No | local | File storage backend |
| `ENABLE_CACHE` | ❌ No | true | Enable caching |
| `CACHE_TTL_SECONDS` | ❌ No | 300 | Cache TTL in seconds |
| `ENABLE_TRANSACTIONS` | ❌ No | true | Enable database transactions |

## 🐛 Troubleshooting

### "No start command detected"
**Solution:** Ensure `railway.json` or `Procfile` exists in root directory

### "DATABASE_URL not set"
**Solution:** Add PostgreSQL plugin from Railway dashboard

### "ModuleNotFoundError: No module named 'main'"
**Solution:** Verify `main.py` exists in project root

### "Bot not responding"
**Solution:** 
1. Check tokens in Environment Variables
2. Verify bots in @BotFather
3. Check logs for errors

### "Database connection failed"
**Solution:**
1. Verify DATABASE_URL is correct
2. Wait for PostgreSQL to initialize (2-3 minutes)
3. Check Railway PostgreSQL logs

## 📈 Scaling Tips

### For Multiple Bots
- Current setup runs both bots in one service
- To separate: Create two services, each with different command
  - Service 1: `python3 user_bot.py`
  - Service 2: `python3 admin_bot.py`

### For High Traffic
- Use Railway's PostgreSQL (better than SQLite)
- Enable caching: `ENABLE_CACHE=true`
- Monitor logs and scale resources as needed

### For Data Storage
- Local storage in `/data/uploads` (ephemeral)
- For persistent storage: Use Railway Volumes
- For larger scale: Integrate S3/MinIO

## 🔐 Security Best Practices

1. **Never commit `.env` file**
   - .gitignore already excludes it ✓

2. **Use Environment Variables**
   - All tokens in Railway dashboard ✓
   - Never hardcode secrets ✓

3. **Enable HTTPS**
   - Railway automatically provides HTTPS ✓

4. **Monitor Logs**
   - Check for unauthorized access
   - Monitor error rates

## 📝 Post-Deployment Checklist

- [ ] Bots responding to `/start`
- [ ] Database connected and initialized
- [ ] Logs showing "Both bots are running"
- [ ] No errors in Railway dashboard
- [ ] Environment variables all set
- [ ] PostgreSQL plugin added

## 🆘 Getting Help

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- GitHub Issues: https://github.com/llpouyagamell-lang/vpn-telegram-bot/issues

---

**Railway Deployment Complete! 🎉**
