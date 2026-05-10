# Module 9 - Step 1: Test API Connection
# CSD-325 | Garvin Stewart

import requests

response = requests.get('http://www.google.com')
print(response.status_code)
