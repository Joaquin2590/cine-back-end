# En joaquin_rodriguez/settings.py: agrega/modifica SOLO estas partes

INSTALLED_APPS = [
    # ... las que ya vienen por defecto ...
    'home_joaquin_rodriguez',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # <- cambia esta línea
        'APP_DIRS': True,
        # ... el resto igual ...
    },
]

# Al final del archivo:
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
