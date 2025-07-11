import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.tool import function_tool
from agents.run import RunConfig
from typing import List, cast
import chainlit as cl

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")


@cl.set_starters
def starter() -> List[cl.Starter]:
    return [
        cl.Starter(
            label="Greeting",
            message="Hello, how can I help you today?",
        ),
        cl.Starter(
            label="Weather",
            message="Find the weather in Karachi.",
        ),
    ]


@function_tool
@cl.step(type="weather tool")
def weather_tool(location: str, unit: str = "C") -> str:
    return f"The weather in {location} is 22 degrees {unit}."


@cl.on_chat_start
async def on_chat_start():
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )

    agent = Agent(
        name="Career Spark Agent",
        tools=[weather_tool],
        model=model,
        instructions="You are a helpful assistant that can answer questions and help with tasks."
    )

    cl.user_session.set("agent", agent)
    cl.user_session.set("config", config)
    cl.user_session.set("chat_history", [])

    await cl.Message(content="Hello, how can I help you today?").send()


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent = cast(Agent, cl.user_session.get("agent"))
    config = cast(RunConfig, cl.user_session.get("config"))
    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    try:
        result = Runner.run_sync(agent, history, run_config=config)  # make sure run_sync exists
        response = result.final_output

        msg.content = response
        await msg.update()

        history.append({"role": "assistant", "content": response})  # ✅ Correct

        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"Error: {e}"
        await msg.update()

