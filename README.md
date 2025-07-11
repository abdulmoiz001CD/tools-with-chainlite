## Tools with Chainlit

This project showcases a conversational AI assistant built with Chainlit, leveraging the Google Gemini API and the agents library for custom tool integration. It provides a simple chat interface capable of answering questions and utilizing a weather tool.

## Features
Interactive Chat: User-friendly web interface via Chainlit.

Gemini AI: Powered by the Google Gemini 2.0 Flash model.

Custom Tooling: Demonstrates a weather_tool for location-based weather information.

Starter Messages: Quick access to common queries.

## Tech Stack
Python

Chainlit

agents Library

Google Gemini API

python-dotenv

## Installation
Clone the repository:

git clone https://github.com/your-username/tools-with-chainlit.git
cd tools-with-chainlit

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

(Ensure requirements.txt includes chainlit, python-dotenv, agents, and openai.)

Set up your Gemini API Key: Create a .env file in the root directory:

GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

## Usage
Run the Chainlit application:

chainlit run main.py -w

Open your browser to http://localhost:8000 to interact with the assistant. Use the provided starters or type your queries (e.g., "Find the weather in Karachi").


## Contribution Guidelines
Contributions are welcome! Please fork the repository, create a new branch, commit your changes, and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.