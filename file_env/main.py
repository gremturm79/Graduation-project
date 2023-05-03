import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

MY_TELEGRAM_KEYS = os.getenv('MY_SECRET_KEY')

config = {
    **dotenv_values('.env.shared'),
    **dotenv_values('.env.secret'),
}

# config = dotenv_values('.env')
print(config)
