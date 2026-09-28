import vertexai

PROJECT_ID = "my-project-id"  # Replace with your Google Cloud project ID   
LOCATION = "us-central1"

print(f"Connecting to Vertex AI in project={PROJECT_ID}, location={LOCATION}...")
client = vertexai.Client(project=PROJECT_ID, location=LOCATION)

print("Creating Vertex AI Memory Bank / Agent Engine...")
engine = client.agent_engines.create(
    config={
        "display_name": "jira-agent-memory-bank",
        "context_spec": {
            "memory_bank_config": {}
        }
    }
)

resource_name = engine.api_resource.name
engine_id = resource_name.split("/")[-1]

print("\n Memory Bank Created Successfully!")
print(f"Full Resource Name: {resource_name}")
print(f"Engine ID: {engine_id}")
print(f"\nYou can now run:")
print(f"uv run adk web --memory_service_uri agentengine://{engine_id} .")
