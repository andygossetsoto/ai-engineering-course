import gradio as gr
import os

gr.ChatInterface(
    fn=response_ai,
    title="Andrea's Digital Twin",
    chatbot=gr.Chatbot(avatar_images=(None, "andrea.png")),
    description="Chat with an AI version of Andrea Gosset a senior Front End Engineer.",
    examples=[
        "Tell me some interesting facts about you.",
        "How many years of experience do you have?",
        "Where did you go to college?",
        "Where are you working now?",
        "Have you worked with AI in a professional project?"
    ]

).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))