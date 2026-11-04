from app.core.config import get_settings

settings = get_settings()

print(f"app name: {settings.app_name}")
print(f"app env: {settings.app_env}")