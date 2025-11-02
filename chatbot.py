print("🤖 Hello! I’m T-REXX. (TIPS) Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("T-REXX: Hello there! How can I help you today?")
    
    elif "how are you" in user_input:
        print("T-REXX: I’m just a program, but I’m doing great! How about you?")
    
    elif "your name" in user_input:
        print("T-REXX: My name is T-REXX , I’m a simple Python chatbot created using if-else statements.")
    
    elif "help" in user_input:
        print("T-REXX: Sure! I can answer simple questions. Try saying hello or asking my name.")
    
    elif "bye" in user_input or "exit" in user_input:
        print("T-REXX: Goodbye! Have a great day! 👋")
        break
    
    else:
        print("T-REXX: I didn’t understand that. Can you say it differently?")
