from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# ============================================================
# BASE DIR & Load .env
# ============================================================
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# ============================================================
# SECRET / DEBUG
# ============================================================
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

# ============================================================
# HOSTS
# ============================================================
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'python-apps-django-production-e22b.up.railway.app',
]

CSRF_TRUSTED_ORIGINS = [
    'https://python-apps-django-production-e22b.up.railway.app',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]

# ============================================================
# APPLICATIONS
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'work05',
    'work06',
    'work07',
    'work08',
    'work09',
    'work10',
    'sns',
    'polls',
]

# ============================================================
# MIDDLEWARE
# ============================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============================================================
# URL / TEMPLATES
# ============================================================
ROOT_URLCONF = 'python_apps_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'python_apps_django.wsgi.application'

# ============================================================
# DATABASE（Railway / Local 自動切替）
# ============================================================
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.mysql"),
            "NAME": os.getenv("DB_NAME", "new_project_db"),
            "USER": os.getenv("DB_USER", "root"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "3306"),
            "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }

# ============================================================
# PASSWORD VALIDATORS
# ============================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================================================
# INTERNATIONALIZATION
# ============================================================
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC / MEDIA（Admin 404 対策済）
# ============================================================
STATIC_URL = '/static/'

# ★★★ これが絶対必要（admin の static もここにまとめられる） ★★★
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ローカル用（任意 static ディレクトリ）
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================================================
# LOGIN / LOGOUT
# ============================================================
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'work10:todo_list'
LOGOUT_REDIRECT_URL = 'login'

# ============================================================
# BASIC AUTH
# ============================================================
ENABLE_BASIC_AUTH = os.getenv("ENABLE_BASIC_AUTH", "False").lower() in ("true", "1", "yes")
if ENABLE_BASIC_AUTH:
    MIDDLEWARE.insert(0, "basicauth.middleware.BasicAuthMiddleware")
    BASICAUTH_USERS = {
        os.getenv("BASIC_AUTH_USERNAME", "admin"): os.getenv("BASIC_AUTH_PASSWORD", "python-2025"),
    }

# ============================================================
# DEFAULT FIELD
# ============================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============================================================
# GEMINI API KEY
# ============================================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
