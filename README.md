# VPN Store Bot - Production Ready Telegram Bot

## 📋 نمای کلی پروژه

یک ربات تلگرام حرفه‌ای برای فروش اشتراک‌های VPN با معماری Clean Architecture، Repository Pattern، و Dependency Injection.

### ✨ ویژگی‌های اصلی

- **معماری تمیز و قابل نگهداری**: Clean Architecture + Repository Pattern + Service Layer
- **Async/Await کامل**: تمام عملیات بی‌همزمان
- **دیتابیس انعطاف‌پذیر**: SQLite (development) → PostgreSQL (production)
- **بدون Hard-Code**: تمام تنظیمات و قیمت‌ها از دیتابیس
- **فیلترهای پیشرفته**: >, <, LIKE, BETWEEN, IN, NULL checks
- **Soft Delete**: حفاظت از سابقه داده‌ها
- **Pagination**: تمام لیست‌ها صفحه‌بندی شده
- **Eager Loading**: جلوگیری از N+1 queries
- **Transaction Management**: تمام عملیات حساس درون Transaction
- **Role-Based Access**: سیستم ادمین با دسترسی‌های سطح‌بندی‌شده
- **Audit Logging**: ثبت تمام اقدامات حساس
- **Error Handling**: Exception handling جامع
- **Logging**: سیستم logging کامل با RotatingFileHandler

## 🏗️ ساختار پروژه

```
VPNStoreBot/
├── config/              # تنظیمات
│   ├── settings.py      # Pydantic BaseSettings (متغیرهای .env)
│   └── constants.py     # Enum‌ها و ثابت‌ها
│
├── database/            # لایه دیتابیس
│   ├── base.py          # DatabaseManager + AsyncEngine
│   ├── mixins.py        # TimestampMixin, SoftDeleteMixin, UUIDMixin
│   └── models/          # جداول دیتابیس
│       ├── all_models.py
│       └── __init__.py
│
├── repository/          # Repository Pattern (Generic Base + Specific)
│   ├── base.py          # BaseRepository (CRUD + Advanced Filtering)
│   ├── user_repository.py
│   ├── order_repository.py
│   ├── payment_repository.py
│   ├── discount_repository.py
│   ├── setting_repository.py
│   ├── audit_log_repository.py
│   └── __init__.py
│
├── services/            # Service Layer (Business Logic)
│   ├── order_service.py
│   ├── payment_service.py
│   ├── discount_service.py
│   ├── message_service.py
│   ├── setting_service.py
│   └── __init__.py
│
├── handlers/            # Telegram Handlers (فقط I/O)
│   ├── user/
│   │   ├── start.py
│   │   ├── shop.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── ...
│   ├── admin/
│   │   ├── start.py
│   │   ├── orders.py
│   │   ├── products.py
│   │   └── ...
│   └── errors.py
│
├── keyboards/           # Inline/Reply Keyboards
│   ├── user_keyboards.py
│   └── admin_keyboards.py
│
├── state/               # FSM States
│   ├── callback_manager.py  # مدیریت Callback Data (< 64 bytes)
│   └── user_state.py        # FSM State Groups
│
├── storage/             # File Storage (Interface + Providers)
│   ├── providers.py     # StorageProvider + LocalStorageProvider
│   └── __init__.py
│
├── cache/               # In-Memory Cache
│   ├── cache.py
│   └── __init__.py
│
├── utils/               # Utility Functions
│   ├── logger.py        # Logger Configuration
│   ├── validators.py    # Luhn Algorithm, Phone validation
│   ├── formatters.py    # Price, Date formatting
│   ├── exceptions.py    # Custom Exceptions
│   ├── decorators.py    # Logging decorators
│   ├── enums.py         # Enum utilities
│   └── __init__.py
│
├── user_bot.py          # User Bot Entry Point
├── admin_bot.py         # Admin Bot Entry Point
├── requirements.txt     # Dependencies
├── .env.example         # Environment Variables Template
├── .gitignore           # Git Ignore
└── README.md            # This file
```

## 🔧 نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.12+
- pip
- Git

### مراحل نصب

#### 1. Clone Repository

```bash
git clone https://github.com/llpouyagamell-lang/vpn-telegram-bot.git
cd vpn-telegram-bot
```

#### 2. Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\\Scripts\\activate     # Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment

```bash
cp .env.example .env
```

سپس `.env` را ویرایش کنید:

```env
# Tokens
USER_BOT_TOKEN=YOUR_USER_BOT_TOKEN
ADMIN_BOT_TOKEN=YOUR_ADMIN_BOT_TOKEN

# Database
DATABASE_URL=sqlite+aiosqlite:///./data/vpn_store.db
# یا PostgreSQL:
# DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/vpnbot

# Environment
ENVIRONMENT=development
LOG_LEVEL=INFO
```

#### 5. Initialize Database

```bash
python3 -c "import asyncio; from database.base import DatabaseManager; asyncio.run(DatabaseManager.init_db())"
```

#### 6. Run Bots

```bash
# Terminal 1 - User Bot
python3 user_bot.py

# Terminal 2 - Admin Bot
python3 admin_bot.py
```

## 📚 معماری و اصول

### Clean Architecture Layers

```
┌──────────────────────────────────────┐
│      Handler Layer (I/O Only)       │ ← فقط دریافت/ارسال پیام
├──────────────────────────────────────┤
│     Service Layer (Business Logic)  │ ← منطق تجاری
├──────────────────────────────────────┤
│    Repository Layer (Data Access)   │ ← Query و Exception
├──────────────────────────────────────┤
│     Database Layer (Entities)       │ ← جداول و روابط
└──────────────────────────────────────┘
```

### Repository Pattern

- **BaseRepository**: CRUD عمومی برای تمام مدل‌ها
- **Specific Repositories**: منطق تخصصی هر مدل
- **No Hard-Coded Queries**: تمام queries درون Repository
- **Type-Safe**: کامل Type Hints

### Dependency Injection

```python
# Service دریافت Repository از طریق Constructor
class OrderService:
    def __init__(self, order_repo: OrderRepository, payment_repo: PaymentRepository):
        self.order_repo = order_repo
        self.payment_repo = payment_repo

# Handler دریافت Service
async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_service = OrderService(order_repo, payment_repo)
    # ...
```

## 🔐 Security Features

- **Tokens محفوظ**: SecretStr برای tokens
- **No Token Logging**: Tokens در logs نمایش داده نمی‌شوند
- **SQL Injection Prevention**: Parameterized queries
- **Role-Based Access Control**: RBAC برای admins
- **Audit Logging**: تمام اقدامات ثبت می‌شوند
- **Soft Delete**: داده‌های حذف‌شده قابل بازیابی
- **Rate Limiting**: (آماده برای اضافه‌کردن)

## 📋 دیتابیس

### جداول اصلی

- **users**: کاربران
- **admins**: ادمین‌ها با RBAC
- **services**: سرویس‌های VPN
- **packages**: ترکیب سرویس + نوع + مدت + حجم + قیمت
- **orders**: سفارش‌ها
- **payments**: پرداخت‌ها (جدا از orders)
- **vpn_configs**: فایل‌های config VPN
- **discount_codes**: کد‌های تخفیف
- **discount_usages**: ثبت استفاده کد‌های تخفیف
- **support_tickets**: تیکت‌های پشتیبانی
- **support_ticket_messages**: پیام‌های تیکت
- **settings**: تنظیمات (کارت، متون، etc.)
- **audit_logs**: ثبت اقدامات
- **broadcasts**: پیام‌های همگانی

### Features

- **Soft Delete**: `is_deleted` و `deleted_at`
- **Timestamps**: `created_at`, `updated_at` (UTC)
- **UUID/ULID**: `public_id` برای API و Callbacks
- **Indexes**: روی فیلدهای پرتکرار
- **Relationships**: Cascade delete + Foreign Keys

## 🔄 Workflow مثال (خرید)

### 1. کاربر /start

```python
# Handler دریافت پیام
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_service = UserService(user_repo)
    user = await user_service.get_or_create_user(telegram_id)
    # ...
```

### 2. انتخاب سرویس

```python
# Service منطق را کنترل می‌کند
async def get_active_services(self) -> List[Service]:
    services = await self.service_repo.get_active_services()
    return services
```

### 3. انتخاب پکیج و پرداخت

```python
# Repository query اجرا می‌کند
async def get_package_by_id(self, package_id: int) -> Package:
    package = await self.package_repo.get_by_id_with_relations(package_id)
    if not package:
        raise RecordNotFound("Package not found")
    return package
```

### 4. Transaction برای سفارش + پرداخت

```python
async def create_order_with_payment(self, user_id: int, package_id: int):
    async with self.session.begin():  # Transaction
        order = await self.order_repo.create(...)
        payment = await self.payment_repo.create(order_id=order.id, ...)
        await self.audit_repo.log_action("create_order", ...)
        # در صورت خطا: auto-rollback
```

## 🚀 Deployment

### روی Railway/Render (رایگان)

```bash
# 1. Push به GitHub
git push origin main

# 2. Connect Repository در Railway
# 3. Set Environment Variables
# 4. Deploy!
```

### روی VPS

```bash
# 1. SSH to VPS
ssh root@your_vps

# 2. Clone repo
git clone ...
cd vpn-telegram-bot

# 3. Setup & Run
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Create systemd service
sudo nano /etc/systemd/system/vpn-bot.service
```

## 📊 Logging

### فایل‌های Log

- `logs/app.log`: جنرال logs (rotating, max 10MB)
- `logs/app_daily.log`: روزانه (keep 30 days)
- `logs/errors.log`: فقط errors

### Log Levels

```
DEBUG   - جزئیات
INFO    - اطلاعات
WARNING - هشدار
ERROR   - خطا
```

## 🎯 Convention‌ها

### Naming

- **Classes**: `PascalCase` (OrderService)
- **Functions**: `snake_case` (get_user_orders)
- **Constants**: `UPPER_SNAKE_CASE` (MAX_PAGE_SIZE)
- **Private**: Prefix `_` (_build_query)

### Type Hints

```python
async def get_user(self, user_id: int) -> Optional[User]:
    """Get user by ID"""
    pass
```

### Docstrings

```python
async def create_order(self, user_id: int, package_id: int) -> Order:
    """
    Create new order
    
    Args:
        user_id: User ID
        package_id: Package ID
    
    Returns:
        Created Order instance
    
    Raises:
        RecordNotFound: If package not found
        TransactionError: If database error
    """
```

## 📚 منابع

- [SQLAlchemy AsyncIO](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

## 📞 Support

- Issues: [GitHub Issues](https://github.com/llpouyagamell-lang/vpn-telegram-bot/issues)

## 📄 License

MIT License - See LICENSE file

---

**Created with ❤️ for Production Ready Applications**
