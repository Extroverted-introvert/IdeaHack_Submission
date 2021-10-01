from django.apps import AppConfig
from twilio.rest import Client


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    account_sid = 'ACd2dda6bfec745c73e72e52824b5f5a19'
    auth_token = 'fffca88e54523c8718c6fedf83105c31'
    client = Client(account_sid, auth_token)

+18182085580