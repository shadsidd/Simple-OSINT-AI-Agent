from agno.agent import Agent
from agno.models.openrouter import OpenRouter
import os
from agno.tools.thinking import ThinkingTools

company_name = ""

prompt = f"""Perform an OSINT investigation on: {company_name}

Identify publicly available information sources about this target.
For each source type, describe what information would typically be available:
1. Social media footprint
2. Professional presence
3. Public records
4. Digital traces
5. Domain and infrastructure information

Then assess potential security risks this public information might pose.
Focus only on publicly available information sources and ethical collection methods.
DO NOT include any actual private information or suggest illegal methods.
"""

reasoning_agent = Agent(
    model=OpenRouter(
        id="gpt-4o-mini",
    ),
    markdown=True,
    #tools=[ThinkingTools()],
)

print("\n🕵️ OSINT INVESTIGATION \n")
print("=" * 80)
reasoning_agent.print_response(
    prompt,
    stream=True,
    markdown=True,
    show_full_reasoning=True,
)
