#  PingOne Resource Orchestrator

This Python-based tool automates the orchestration of PingOne resources required for application authentication flows and PingFederate integration.

---

## Overview

The orchestration flow provisions and links all required PingOne resources in the following order:

1. Application Creation  
2. Device Authentication Policy Creation  
3. Sign-On Policy Creation  
4. Assignment of Device Policy to Sign-On Policy  
5. Assignment of Sign-On Policy to Application  
6. PingFederate Gateway Connection and Credential Creation

---

## Project Structure

pingone_resource_creator/ 
    ├── common/ 
        │ └── utils.py # Logging and config utilities 
    ├── scripts/ │ 
        ├── orchestrate.py # Main orchestration runner │ 
        ├── pingone_application_handler.py │ 
        ├── device_auth_policy_handler.py │ 
        ├── signon_policy_handler.py │ 
        ├── assign_device_to_signon.py │ 
        ├── assign_signon_to_app.py 
        │ └── pingfed_connection_handler.py 
    ├── config/ 
        │ └── env.yaml # Environment-specific configuration 
    └── README.md


---
##  Running the Orchestrator
**Install Dependencies:**
```sh
    pip install -r requirements.txt
```
**Run the orchestration:**
```sh
    python scripts/orchestrate.py --env dev
```
This triggers the creation and linking of all required PingOne resources
---

## Configuration

Create a YAML file at `config/env.yaml` with the following structure:

```yaml
base_url: "https://api.pingone.eu"
env_id: "your-env-id"
bearer_token: "your-bearer-token"

applications:
  - name: "Example Application"
    enabled: true
    protocol: "OPENID_CONNECT"
    type: "WEB_APP"
    redirectUris:
      - "https://example.com/callback"
    grantTypes:
      - "AUTHORIZATION_CODE"

device_authentication_policies:
  - name: "mfa_policy"
    description: "MFA policy example"
    enabled: true
    factors:
      - type: "EMAIL_OTP"
        enabled: true

signon_policy:
  name: "custom_signon_policy"
  default: false
  
--- 

