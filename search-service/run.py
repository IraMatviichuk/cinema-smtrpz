import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()

config_name = "development"
app = create_app(config_name)


if __name__ == "__main__":
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
