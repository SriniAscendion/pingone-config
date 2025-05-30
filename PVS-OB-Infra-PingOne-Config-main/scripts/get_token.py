import requests
import sys

def get_token(encoded_credentials: str, env_id: str) -> str:
    url = f"https://auth.pingone.com/{env_id}/as/token"

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        token = response.json().get("access_token")
        if token:
            return token
        else:
            print("Failed to retrieve access token.")
            print(response.json())
    except requests.RequestException as e:
        print(f"Error retrieving access token: {e}")
        if response is not None:
            print(response.text)
        sys.exit(1)

if __name__ == "__main__":
    # Prompt user for base64-encoded credentials and environment ID
    encoded_credentials = input("Enter base64-encoded 'client_id:client_secret': ").strip()
    ENV_ID = input("Enter Environment ID: ").strip()

    token = get_token(encoded_credentials, ENV_ID)
    print(f"\nAccess Token:\n{token}")
