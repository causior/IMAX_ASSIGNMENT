from agent import ColdCallAgent
from utils import speak_text, listen_audio

def main():
    agent = ColdCallAgent()
    
    print("Select Scenario:")
    print("1. Demo Scheduling")
    print("2. Candidate Interviewing")
    print("3. Payment/Order Follow-up")
    
    choice = input("Enter the scenario number (1/2/3): ")
    
    if choice == '1':
        response = agent.schedule_demo()
    elif choice == '2':
        response = agent.conduct_interview()
    elif choice == '3':
        response = agent.payment_followup()
    else:
        print("Invalid choice")
        return

   
    speak_text(response)
    
    
    user_input = listen_audio()
   
    print("User said:", user_input)

if __name__ == "_main_":
    main()
