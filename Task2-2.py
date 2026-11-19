import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
print("API key loaded successfully : ",API_KEY)




BASE_URL = "https://jsonplaceholder.typicode.com"

try:
    response = requests.get(
        f"{BASE_URL}/users",
        timeout=5
    )

    response.raise_for_status()

    users = response.json()

    print("\nFirst 3 Users:")

    for user in users[:3]:
        print(
            user.get("id"),
            "-",
            user.get("name"),
            "-",
            user.get("email")
        )

    
    parsed_users = []

    for user in users:

        user_data = {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
            "company": user.get("company", {}).get("name")
        }

        parsed_users.append(user_data)


    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(parsed_users, file, indent=4)

    print("\nUsers saved successfully to users.json")


except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)



try:
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=5
    )
    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    
    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("/users/9999 -> Timeout")

except requests.exceptions.ConnectionError:
    print("/users/9999 -> Connection Error")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
