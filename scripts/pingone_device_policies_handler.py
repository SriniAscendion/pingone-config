import requests
from typing import Dict, Any

import logging
logger = logging.getLogger(__name__)


def create_device_policy(base_url: str, env_id: str, token: str, policy_data: Dict[str, Any]) -> requests.Response:
    """
    Make an API request to create a device authentication policy in PingOne.
    """
    url = f"{base_url}/v1/environments/{env_id}/deviceAuthenticationPolicies"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(url, headers=headers, json=policy_data, timeout=10)
        response.raise_for_status()
        logging.info(f" Created device policy: {policy_data.get('name')}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f" Failed to create policy: {policy_data.get('name')}")
        logging.debug(response.text if 'response' in locals() else '')
        logging.exception(e)
        raise
