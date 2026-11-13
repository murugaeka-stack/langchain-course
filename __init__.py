import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"

print("Current file:", __file__)
print("Env file path:", env_path)
print("Env file exists:", env_path.exists())

load_dotenv(env_path, override=True)

print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))