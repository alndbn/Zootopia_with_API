# data_fetcher.py
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any

API_URL = "https://api.api-ninjas.com/v1/animals"

# .env sicher laden (keine Assertion-Fehler in interaktiven Sessions)
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

# -> Du kannst zunächst auch DEINEN Key hier direkt eintragen,
#    damit es sicher läuft. Danach .env benutzen.
API_KEY = os.getenv("API_KEY") or "k2sC+abhDpqs43guAopVUw==1Gn9KgLvMUzhAN5M"

def fetch_data(animal_name: str) -> List[Dict[str, Any]]:
    if not API_KEY:
        raise RuntimeError("API_KEY fehlt. Lege eine .env mit API_KEY an.")

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name.lower()}  # sicherheitshalber klein

    resp = requests.get(API_URL, headers=headers, params=params, timeout=15)

    # --- DIAGNOSE: zeig uns, was wirklich passiert ---
    if resp.status_code != 200:
        print("[data_fetcher] HTTP", resp.status_code)
        print("[data_fetcher] Body:", resp.text[:300])
        return []

    try:
        data = resp.json()
    except Exception as e:
        print("[data_fetcher] JSON-Fehler:", e)
        print("[data_fetcher] Body (Anfang):", resp.text[:300])
        return []

    if not isinstance(data, list):
        print("[data_fetcher] Unerwartetes Format:", type(data))
        return []

    if not data:
        # nützliche Diagnose, falls leer
        print("[data_fetcher] Leeres Ergebnis für params:", params)
    return data


# Kleiner Direkt-Test: `python3 data_fetcher.py Fox`
if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "fox"
    out = fetch_data(q)
    print("items:", len(out))
    if out:
        print("sample keys:", list(out[0].keys()))
