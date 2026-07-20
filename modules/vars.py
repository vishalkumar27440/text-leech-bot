import os

API_ID    = os.environ.get("API_ID", "21595709")
API_HASH  = os.environ.get("API_HASH", "6b683b86a90c6fae0fbe50a6494bdd53")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8919674457:AAFoqHcf-ywkOCxJJupfEenU2C0LC4hYEWU") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
