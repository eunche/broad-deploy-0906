"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django-heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "enrz-t%t2gh_tm1#-^@^nuasv3_nt*58d8is=z6_teqa6212c="

# SECURITY WARNING: don't run with debug turned on in production!
#!
DEBUG = True

ALLOWED_HOSTS = ["*"]


def is_ec2_linux():
    """Detect if we are running on an EC2 Linux Instance
    See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
    """
    if os.path.isfile("/sys/hypervisor/uuid"):
        with open("/sys/hypervisor/uuid") as f:
            uuid = f.read()
            return uuid.startswith("ec2")
    return False


def get_linux_ec2_private_ip():
    """Get the private IP Address of the machine if running on an EC2 linux server"""
    from urllib.request import urlopen

    if not is_ec2_linux():
        return None
    try:
        response = urlopen("http://169.254.169.254/latest/meta-data/local-ipv4")
        ec2_ip = response.read().decode("utf-8")
        if response:
            response.close()
        return ec2_ip
    except Exception as e:
        print(e)
        return None


private_ip = get_linux_ec2_private_ip()
if private_ip:
    ALLOWED_HOSTS.append(private_ip)


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# startapp 명령어로 추가해준 App들
PROJECT_APPS = [
    "map.apps.MapConfig",
    "bakeries.apps.BakeriesConfig",
    "posts.apps.PostsConfig",
    "users.apps.UsersConfig",
]

# 외부에서 기능을 미리 만들어놓은 App들
THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if DEBUG is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif DEBUG is False:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": "broad.ciyzxxyksnt2.ap-northeast-2.rds.amazonaws.com",
            "PORT": "5432",
            "NAME": "broad",
            "USER": "postgres",
            "PASSWORD": "espera135",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

"""
Static 관련 설정
"""
# 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
STATIC_URL = "/static/"
# 개발단계에서 사용하는 정적파일들이 위치한 경로
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_local")]
# collectstatic명령어를 통해 Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로(배포시 사용하기 위해)
STATIC_ROOT = os.path.join(BASE_DIR, "static")


"""
Media 관련 설정
"""
if DEBUG is True:
    # 사용자에 의해 업로드되는 미디어 파일을 저장할 경로
    MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
    # 웹 페이지에서 사용할 미디어 파일의 최상위 URL 경로
    MEDIA_URL = "/media/"
else:
    """
    S3사용할때 쓰는 코드
    """
    AWS_REGION = "ap-northeast-2"
    AWS_STORAGE_BUCKET_NAME = "broadbucket"
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = "s3.%s.amazonaws.com" % AWS_REGION
    AWS_ACCESS_KEY_ID = "AKIA3TU3EUO3QU2SBG7U"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    # Media Setting
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


# User 모델 커스터마이징
AUTH_USER_MODEL = "users.User"
MY_AWS_URL = "broad.eba-rgevajz9.ap-northeast-2.elasticbeanstalk.com"
# MY_AWS_URL = "127.0.0.1:8000"

KAKAO_ID = "08a8e8a0fde8d36ad5c30df67d5d41f6"

django_heroku.settings(locals())