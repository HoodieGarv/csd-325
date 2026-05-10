# Module 9 - Step 3: Custom API - PokeAPI
# CSD-325 | Garvin Stewart
# API: https://pokeapi.co/ (free, no API key required)
# Endpoint: https://pokeapi.co/api/v2/pokemon/{name}

import requests

POKEMON_NAME = "pikachu"
URL = f"https://pokeapi.co/api/v2/pokemon/{POKEMON_NAME}"

# --- Step 1: Test the connection ---
print("=== Step 1: Connection Test ===")
response = requests.get(URL)
print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Connection failed. Exiting.")
    exit()

# --- Step 2: Raw response (no formatting) ---
print("\n=== Step 2: Raw Response (no formatting) ===")
print(response.text[:500], "...")   # Truncated - full response is very large

# --- Step 3: Formatted response ---
print("\n=== Step 3: Formatted Response ===")
data = response.json()

print(f"Pokemon Name : {data['name'].capitalize()}")
print(f"Pokemon ID   : {data['id']}")
print(f"Base XP      : {data['base_experience']}")
print(f"Height       : {data['height'] / 10} m")
print(f"Weight       : {data['weight'] / 10} kg")

print("\nAbilities:")
for ability_entry in data["abilities"]:
    hidden = " (Hidden)" if ability_entry["is_hidden"] else ""
    print(f"  - {ability_entry['ability']['name'].capitalize()}{hidden}")

print("\nBase Stats:")
for stat in data["stats"]:
    print(f"  {stat['stat']['name'].capitalize():<20}: {stat['base_stat']}")

print("\nTypes:")
for type_entry in data["types"]:
    print(f"  - {type_entry['type']['name'].capitalize()}")
