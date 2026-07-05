from django.conf import settings


def app_settings(request):
    """Inject global app settings into every template context."""
    return {
        "APP_NAME": getattr(settings, "APP_NAME", "Synkora ERP"),
        "APP_URL": getattr(settings, "APP_URL", ""),
    }
