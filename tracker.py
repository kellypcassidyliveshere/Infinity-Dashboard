import time
from datetime import datetime

def mood_booster(mood):
    mood = mood.lower()
    if any(word in mood for word in ["sad", "low", "tired", "anxious"]):
        return "Gemini's Technique: Try 'Box Breathing' (4s inhale, 4s hold, 4s exhale, 4s hold). This resets your nervous system."
    elif any(word in mood for word in ["good", "happy", "excited", "determined"]):
        return "Gemini's Commemoration: Channel that energy into your Architecture. Write down one 'Big Win' you want to secure in the next hour."
    else:
        return "Gemini's Elevation: Take 2 minutes to visualize the Cyber Lounge opening day. Feel the success."

def run_54321():
    print("\n--- 5-4-3-2-1 Grounding Technique ---")
    input("Name 5 things you can SEE (Press Enter when done)")
    input("Name 4 things you can TOUCH")
    input("Name 3 things you can HEAR")
    input("Name 2 things you can SMELL")
    input("Name 1 thing you can TASTE")
    return "Grounding Complete. You are present. You are powerful."

def log_entry():
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 1. Mood Question
    mood = input("\nHow is your mood today, Kelly-Ann?\n> ")
    elevator = mood_booster(mood)
    print(f"\n{elevator}")
    
    # 2. Goal Question
    goal = input("\nWhat is your main goal today?\n> ")
    print(f"\nGemini's Strategy: To stay on track with '{goal}', set a 25-minute timer now. Work ONLY on this. I will hold the space for you.")
    
    # 3. Grounding
    grounding_result = run_54321()
    print(f"\n{grounding_result}")

    # Save everything
    with open("spiritual_log.txt", "a") as f:
        f.write(f"\n[{date}]\nMOOD: {mood}\nGOAL: {goal}\nTECHNIQUE: {elevator}\n{'-'*40}")

if __name__ == "__main__":
    log_entry()
