# run_justice_map.py

import os
from agent import JusticeMapAgent

# PUT YOUR API KEY HERE
API_KEY = ""


def main():

    if not API_KEY:
        print("ERROR: Add your Gemini API key inside run_justice_map.py")
        return

    agent = JusticeMapAgent(api_key=API_KEY)

    print("\n=== JusticeMap Capstone Project (GenAI Version) ===\n")

    # Initial message
    message = "My employer has not paid my salary for the last two weeks."
    print("USER:", message)
    reply = agent.handle_message(message)
    print("AGENT:", reply)

    # Test messages
    test_inputs = [
        "My name is Ramesh Kumar.",
        "My father's name is Suresh.",
        "I live at 14/B Gandhi Street, Chennai.",
        "My boss is Mr. Sharma.",
        "It happened between June 1 and June 14.",
        "The total money owed is 15000 rupees."
    ]

    for msg in test_inputs:
        print("\nUSER:", msg)
        reply = agent.handle_message(msg)
        print("AGENT:", reply)

    print("\nUSER: Please continue.\n")
    final = agent.handle_message("continue")

    print("=== FINAL DOCUMENT GENERATED ===\n")
    print(final)


if __name__ == "__main__":
    main()
