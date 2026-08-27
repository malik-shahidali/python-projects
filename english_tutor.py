from google import genai

client = genai.Client(api_key="YOUR_API_KEY_HERE")

print("=== AI English Tutor ===")
print("Apni English sentence likho — main check karunga!")
print("Bahar jaane ke liye 'quit' likho")
print("=" * 30)

while True:
    sentence = input("\nTumhari sentence: ")
    
    if sentence.lower() == "quit":
        print("Allah Hafiz!")
        break
    
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
        Check this English sentence: "{sentence}"
        
        1. Is it correct? Yes or No
        2. If wrong, what is the correct sentence?
        3. What was the mistake?
        4. Give one example of similar correct sentence
        
        Reply in simple Urdu/English mix so Pakistani student understands.
        """
    )
    
    print("\nAI Tutor:", response.text)
    print("-" * 30)