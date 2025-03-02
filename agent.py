import json
from together_api import fetch_ai_response 

class ColdCallAgent:
    """AI-powered agent for handling cold calls in different scenarios."""
    
    def __init__(self, dialogue_file='data/dialogues.json'):
        """Loads dialogues from a JSON file."""
        try:
            with open(dialogue_file, 'r', encoding='utf-8') as file:
                self.dialogues = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print(f"🚨 Error loading dialogues: {error}")
            self.dialogues = {}  

    def _generate_scenario_response(self, category):
        """Fetches a response for a given scenario category."""
        if category in self.dialogues:
            prompt = self.dialogues[category][0].get("greeting", "Hello! How can I assist you?")
            print(f"\n🗣 Agent ({category.replace('_', ' ').title()}): {prompt}")
            
            response = fetch_ai_response(prompt)
            print(f"🤖 AI Response: {response}\n")
            return response
        else:
            print(f"⚠️ No dialogues found for '{category}'. Please check your JSON file.")
            return ""

    def schedule_demo(self):
        """Handles demo scheduling scenario."""
        return self._generate_scenario_response("demo_scheduling")

    def conduct_interview(self):
        """Handles candidate interviewing scenario."""
        return self._generate_scenario_response("candidate_interview")

    def payment_followup(self):
        """Handles payment/order follow-up scenario."""
        return self._generate_scenario_response("payment_followup")

if __name__ == "__main__":
    agent = ColdCallAgent()

    