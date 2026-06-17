def main():
    #Hashmap of user inputs and corresponding bot responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi":"Hello! Awesome to chat with you.",
        "greeting": "Greeting! What can I do for you today?",
        "how are you": "I'm a rule-based AI, doing great and ready to help!",
        "help": "You can chat whit me by typing greetings. Type 'exit' to quit.",
        "bye": "Goodbye! Have a great day!" 
    }


    print("===========================================================================")
    print("      Welcome to DecodeLabs Rule-Based AI Bot      ")
    print("      Type 'exit' or 'quit' to stop      ")
    print("===========================================================================")
    #The HeartBeat 
    while True:
    
         #Phase 1 : Input & Sanitization 
         raw_input = input("You: ") 
         clean_input = raw_input.lower().strip()
         if clean_input in ['exit', 'quit']:
             print("Bot: Goodbye! Have a great day!")
             break
         if not clean_input:
            continue
    
         #  Phase 2 :Intent Matching using the efficient .get() method
         bot_response = responses.get(clean_input, "I'm not sure how to respond to that. Type 'help' for options.")
    
         # Phase 3 : Output 
         print (f"Bot: {bot_response}")
if __name__ == "__main__":
    main()
