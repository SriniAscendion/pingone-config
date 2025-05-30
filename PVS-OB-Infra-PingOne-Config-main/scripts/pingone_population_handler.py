import requests
from common.utils import setup_logging

logger = setup_logging()
 
def create_population(base_url, env_id, token, population_payload):
    url = f"{base_url}/v1/environments/{env_id}/populations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
   
    response = requests.post(url, headers=headers, json=population_payload)
    response.raise_for_status()
    return response.json()
   