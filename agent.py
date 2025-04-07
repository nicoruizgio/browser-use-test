from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from dotenv import load_dotenv
import base64
import asyncio

config = BrowserContextConfig(
    save_recording_path="recordings",
)

browser = Browser()

def save_scrensots(history):
    for idx, screenshot in enumerate(history.screenshots()):
        with open(f"screenshots/screenshot_{idx}.png", "wb") as f:
            f.write(base64.b64decode(screenshot))

context = BrowserContext(browser=browser, config=config)
llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Go to https://keen.io/guides/ecommerce-analytics/example-site/ and by the cheapest camera",
        llm=llm,
        use_vision=True,
        save_conversation_path="logs/conversation",
        browser_context=context,
        browser=browser
    )
    history = await agent.run()
    save_scrensots(history)
    print("URLS: ", end="\n\n")
    print(history.urls(), end="\n\n")
    print("EXECUTED ACTIONS: ", end="\n\n")
    print(history.action_names(), end="\n\n")
    print("EXTRACTED CONTENT: ", end="\n\n")
    print(history.extracted_content(), end="\n\n")
    print("ERRORS: ", end="\n\n")
    print(history.errors(), end="\n\n")
    print("ALL ACTIONS WITH PARAMETERS: ", end="\n\n")
    print(history.model_actions(), end="\n\n")

asyncio.run(main())