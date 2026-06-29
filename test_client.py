import asyncio
import logging
import httpx

# Set up simple logging for visibility
logging.basicConfig(level=logging.INFO)

async def main():
    url = "http://localhost:8080/a2a/jira_agent"
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
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers={"Content-Type": "application/json"})
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
