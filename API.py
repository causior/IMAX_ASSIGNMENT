import os
import requests
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Validate API key availability
if not API_KEY:
    raise ValueError("❌ TOGETHERAI_API_KEY is missing! Please check your .env file.")

def clean_response_text(text):
    """Removes <think> tags and any enclosed content from the response."""
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL | re.IGNORECASE).strip()

def fetch_ai_response(prompt, model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free", max_tokens=1000, temperature=0.7):
    """Sends a request to the Together AI API and retrieves a generated response."""
    api_url = "https://api.together.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        result = response.json()

        # Extract the AI-generated response
        raw_content = result["choices"][0]["message"]["content"]
        return clean_response_text(raw_content)

    except requests.exceptions.RequestException as err:
        print(f"🚨 API Request Error: {err}")
        return None

if __name__ == "__main__":
    sample_prompt = "Namaste! Main XYZ se baat kar raha hoon. Kya aap ERP demo dekhna chaenge?"
    response = fetch_ai_response(sample_prompt)

    if response:
        print("\n🤖 AI Response:", response)
    else:
        print("\n⚠️ No response received from the AI.")
