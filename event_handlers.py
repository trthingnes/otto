from slack_bolt import App
from slack_sdk import WebClient

# This file contains event handlers for the Slack Bolt app
# Sample application: https://github.com/slack-samples/bolt-python-assistant-template/blob/main/listeners/events/assistant_thread_started.py

def register_event_handlers(app: App):
    @app.event("assistant_thread_started")
    def thread_started(payload, client: WebClient):
        thread = payload["assistant_thread"]
        user_id, channel_id = thread["user_id"], thread["channel_id"]
        client.chat_postMessage(text="Hey there <@{user_id}>! How can I help you today?")