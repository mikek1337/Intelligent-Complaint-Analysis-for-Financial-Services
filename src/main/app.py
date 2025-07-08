import gradio as gr
import sys
import os
from gradio import ChatMessage, Chatbot
import pandas as pd
from src.generator import Generator
# Get the absolute path to the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
project_root = os.path.dirname(current_dir)
# Add the 'src' directory to sys.path
sys.path.insert(0, os.path.join(project_root, 'src'))

gen = Generator()
def send_message(message:str,history:list):
    """
        send the chat message to LLM and returns the response with sources
        Args:
            message (str): Question you want to ask LLM.
            history (list): previous messages
    """
    response = gen.llm_response(message)
    metadata = [f'Complaint ID - {meta['Complaint ID']} - Product - {meta['Product']} - Company - {meta['Company']} - Issue - {meta['Issue']} - Date recevied - {meta['Date received']}' for meta in response['meta']]
    return response['llm_response'], gr.DataFrame(value=pd.DataFrame(response['meta']))

with gr.Blocks() as demo:
    df = gr.DataFrame(render=False)
    with gr.Row():
        with gr.Column():
            
            gr.ChatInterface(
                send_message,
                additional_outputs=[df],
                type="messages"
            )
        with gr.Column():
            gr.Markdown("<center><h1>Source</h1></center>")
            df.render()
demo.launch()
# gr.ChatInterface(fn=send_message, additional_outputs=[accordion, list]).launch()