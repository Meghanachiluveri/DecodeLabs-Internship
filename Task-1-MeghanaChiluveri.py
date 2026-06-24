# Project 1: Rule-Based AI Chatbot

responses = {
    "hello":        "Hey there! How can I assist you today?",
    "hi":           "Hi! Welcome to DecodeLabs Assistant.",
    "hey":          "Hey! What can I help you with?",
    "how are you":  "I'm just a bot, but I'm running perfectly! How about you?",
    "what is ai":   "AI stands for Artificial Intelligence — machines simulating human thinking!",
    "what is your name": "I'm DecoBot, your Rule-Based AI assistant by DecodeLabs.",
    "help":         "Sure! You can ask me: 'hello', 'how are you', 'what is ai', 'what is your name'.",
    "bye":          "Goodbye! Keep building great things.",
    "thanks":       "You're welcome! Happy to help.",
    "who made you": "I was built by an AI Engineering intern at DecodeLabs as Project 1!",
}

# --- CHATBOT ENGINE ---
print("  DecoBot - Rule-Based AI Chatbot")
print("  Type 'QUIT' or 'EXIT' to stop.")

while True:

    # PHASE 1: INPUT & SANITIZATION
    raw_input_text = input("\nYou: ")
    clean_input = raw_input_text.lower().strip()  

    if clean_input in ("quit", "exit", "bye"):
        print("DecoBot: Bye! See you next time.")
        break

    # PHASE 2: PROCESS — Dictionary lookup with fallback (O(1))
    reply = responses.get(clean_input, "I don't understand that yet. Try asking 'help'!")

    # PHASE 3: OUTPUT
    print(f"DecoBot: {reply}")