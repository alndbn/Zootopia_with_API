
import os
from pathlib import Path
import requests
from dotenv import dotenv_values
from typing import List, Dict, Any

API_URL = "https://api.api-ninjas.com/v1/animals"


ENV = dotenv_values(Path(__file__).with_name(".env"))
API_KEY = ENV.get("API_KEY") or os.getenv("API_KEY")

def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    if not API_KEY:
        raise RuntimeError("API_KEY missing in .env")
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name.lower()}
    r = requests.get(API_URL, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data if isinstance(data, list) else []
