# Module 9 - Step 2: Open Notify API - Current Astronauts in Space
# CSD-325 | Garvin Stewart
# Tutorial: https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json

# Test connection first
response = requests.get("http://api.open-notify.org/astros.json")
print("Status Code:", response.status_code)

# Print raw response (no formatting)
print("\n--- Raw Response ---")
print(response.text)

# Print formatted response
print("\n--- Formatted Response ---")
data = response.json()
print("Number of astronauts currently in space:", data["number"])
print("\nAstronauts currently in space:\n")
for astronaut in data["people"]:
    print("  Name:", astronaut["name"])
    print("  Craft:", astronaut["craft"])
    print()
