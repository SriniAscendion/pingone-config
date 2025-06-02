import sys
import os
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.pingone_device_policies_handler import create_device_policy
from common.utils import load_config, setup_logging
from scripts.pingone_user_handler import create_user
from scripts.pingone_population_handler import create_population
from scripts.get_token import get_token

logger = setup_logging()

def main(env: str, client_secret: str):
    logger.info(f"Orchestration started for environment: {env}")

    try:
        config_path = f"configs/{env}"
        config = load_config(config_path)
        base_url = config["base_url"]
        env_id = config["env_id"]
        encoded_credentials = client_secret

        # Get token using encoded credentials
        token = get_token(encoded_credentials, env_id)

        # Step 1: Create Population
        logger.info("[STEP 1] Creating Population...")
        population_payload = config["populations"][0]
        population_response = create_population(base_url, env_id, token, population_payload)
        population_id = population_response["id"]
        logger.info(f"Population '{population_response['name']}' created with ID: {population_id}")

        # Step 2: Create User
        logger.info("[STEP 2] Creating User...")
        user_payload = config["user"]
        user_payload["population"] = {"id": population_id}
        user_response = create_user(base_url, env_id, token, user_payload)
        logger.info(f"User '{user_response['username']}' created with ID: {user_response['id']}")

        # Step 3: Create Device Authentication Policy
        logger.info("[STEP 3] Creating Device Authentication (MFA) Policy...")
        device_auth_payload = config["device_authentication_policies"][0]
        device_json_response = create_device_policy(base_url, env_id, token, device_auth_payload)
        logger.info(f"Device Authentication Policy '{device_json_response['name']}' created with ID: {device_json_response['id']}")
        logger.info("Orchestration completed successfully.")

    except Exception as e:
        logger.exception(f"Orchestration failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orchestrate PingOne setup")
    parser.add_argument("env", help="Environment name")
    parser.add_argument("--client_secret", required=True, help="Client secret")

    args = parser.parse_args()

    main(args.env, args.client_secret)
