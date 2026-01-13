# Cyber Hygiene Quiz App
# Author: Qhayiya Zintle Lalapi
# A simple quiz to teach basic cybersecurity awareness.

def cyber_quiz():
    print("=== Cyber Hygiene Quiz ===")
    
    score = 0
    
    # ANSI escape codes for bold
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Question 1
    print("\nQ1: Is it safe to use '12345' as your password?")
    answer1 = input("Enter Yes or No: ").strip().lower()
    if answer1 == "no":
        print(f"{BOLD}Correct!{RESET} Strong passwords should be complex.")
        score += 1
    else:
        print(f"{BOLD}Incorrect.{RESET} Weak passwords are unsafe.")
    
    # Question 2
    print("\nQ2: Should you click links in suspicious emails?")
    answer2 = input("Enter Yes or No: ").strip().lower()
    if answer2 == "no":
        print(f"{BOLD}Correct!{RESET} Avoid phishing attempts.")
        score += 1
    else:
        print(f"{BOLD}Incorrect.{RESET} Phishing emails can steal your data.")
    
    # Final score
    print(f"\nYour final score: {score}/2")

# Run the quiz
cyber_quiz()
