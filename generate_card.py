import asyncio
from jira_agent.agent import root_agent
from google.adk.a2a.utils.agent_card_builder import AgentCardBuilder

async def main():
    builder = AgentCardBuilder(agent=root_agent)
    card = await builder.build()
    card_json = card.model_dump_json(indent=2)
    with open("agent.json", "w") as f:
        f.write(card_json)
    print("Agent card successfully created and written to agent.json")

if __name__ == "__main__":
    asyncio.run(main())
