# AI Agent for Cold Calling (Hinglish)

## Project Overview
This project implements an AI agent capable of conducting personalized and human-like cold calls in Hinglish for three business scenarios:

1. **Demo Scheduling** - Scheduling product demos for an ERP system.
2. **Candidate Interviewing** - Conducting initial screening interviews.
3. **Payment/Order Follow-up** - Reminding/requesting customers to release payments or place orders.

The agent can understand context, personalize interactions, and exhibit human-like conversational abilities in Hinglish.

## Setup Instructions
### 1. Environment Setup
Ensure you have Python installed and set up a virtual environment:

```sh
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

Install the required dependencies:
```sh
pip install -r requirements.txt
```

### 2. API Keys & Environment Variables
Create a `.env` file in the root directory and add your TogetherAI API key:
```sh
TOGETHERAI_API_KEY=your_api_key_here
```

## Project Structure
```
|-- data/
|   |-- dialogues.json  # Predefined dialogues for different scenarios
|
|-- together_api.py  # Handles API interaction with TogetherAI
|-- cold_call_agent.py  # AI agent for handling conversations
|-- main.py  # Entry point to interact with the AI agent
|-- utils.py  # Utility functions for TTS and STT processing
|-- requirements.txt  # List of dependencies
|-- README.md  # Project documentation
```

## Usage
Run the main script to start the AI agent:
```sh
python main.py
```
Follow the prompts to select a scenario and interact with the AI agent.

## Technologies Used
- **Language Model**: TogetherAI (DeepSeek-R1-Distill-Llama-70B-free)
- **Text-to-Speech (TTS)**: `pyttsx3`
- **Speech-to-Text (STT)**: `speechrecognition`
- **Frameworks**: Python, Requests, Regular Expressions


## Future Enhancements
- Advanced conversation memory and state tracking
- Integration with real-world calendar and CRM APIs
- Sentiment analysis for enhanced personalization
- Fine-tuned Hinglish speech models

