import requests
from common.utils import setup_logging
 
logger = setup_logging()
 
def create_user(base_url: str, env_id: str, token: str, user_payload: dict) -> dict:
    url = f"{base_url}/v1/environments/{env_id}/users"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
 
    response = requests.post(url, headers=headers, json=user_payload)
    response.raise_for_status()
    return response.json()

    # if response.status_code in [200, 201]:
    #     logger.info(f"[SUCCESS] User created successfully with status code: {response.status_code}")
    #     return {
    #         "status": "success",
    #         "code": response.status_code,
    #         "data": response.json()
    #     }
    # else:
    #     logger.error(f"[ERROR] Failed to create user. Status Code: {response.status_code}, Message: {response.text}")
    #     return {
    #         "status": "failure",
    #         "code": response.status_code,
    #         "message": response.text
    #     }
