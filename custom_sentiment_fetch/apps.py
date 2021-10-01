from peace_watch.settings import SENTIMENT_MODEL_DIR
from django.apps import AppConfig
import tensorflow as tf
from django.conf import settings as conf


class CustomSentimentFetchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_sentiment_fetch'
    sentiment_model=tf.keras.models.load_model(conf.SENTIMENT_MODEL_DIR)
    