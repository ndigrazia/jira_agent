import vertexai

PROJECT_ID = "my-project-id"  # Replace with your Google Cloud project ID   
LOCATION = "us-central1"

client = vertexai.Client(project=PROJECT_ID, location=LOCATION)

print('-' * 80)

for engine in client.agent_engines.list():
    res = engine.api_resource
    eng_id = res.name.split('/')[-1]
    name = res.display_name or 'N/A'
    create_time = str(res.create_time) if res.create_time else 'N/A'
    print(f'{eng_id:<22} | {name:<35} | {create_time}')

