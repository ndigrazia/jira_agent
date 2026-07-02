import asyncio
import logging
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up simple logging for visibility
logging.basicConfig(level=logging.INFO)

async def main():
    url = "http://127.0.0.1:8080/a2a/jira_agent"
    #url = "https://jira-agent-service-154372397551.us-central1.run.app/a2a/jira_agent"
    print(f"Connecting to {url} using custom JSON-RPC transport client...")
    
    payload = {
        "jsonrpc": "2.0",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": "msg-12345",
                "role": "user",
                "parts": [
                    {
                        "text": "¿Qué es Jira?"
                    }
                ]
            }
        },
        "id": 1
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        headers = {
            "Content-Type": "application/json",
            "Authorization": os.environ.get("AUTHORIZATION", "Bearer sk-1234")
        }
        response = await client.post(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}")
        try:
            res_json = response.json()
            print("\nResponse payload:")
            import json
            print(json.dumps(res_json, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
