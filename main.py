from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("Api_key")
set_tracing_disabled(disabled=True)


MODEL = 'gemini/gemini-2.0-flash'


agent = Agent(
    name="Assistant",
    instructions="You only respond in haikus.",
    model=LitellmModel(model=MODEL , api_key=api_key),

)

result = Runner.run_sync(agent, "who are you?")
print(result.final_output)
