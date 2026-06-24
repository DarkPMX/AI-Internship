from google import genai
import random
import time

client = genai.Client(api_key="AQ.Ab8RN6JvrjBd4x1F-K-TBepWVE7O6QPuonXEadcUw0qLXaeKnw")

print("🚀 AI FACT BATTLE 🚀")
print()

topics = ["Space", "Dinosaurs", "Technology", "Ocean", "Animals"]

topic = random.choice(topics)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Generate 3 amazing facts about {topic}.
One fact should be fake.
Number them 1, 2, and 3.
At the end write:
ANSWER: <number>
"""
)

text = response.text

answer = text.split("ANSWER:")[-1].strip()
facts = text.split("ANSWER:")[0]

print(f"🎯 Topic: {topic}")
print()
print(facts)

guess = input("\nWhich fact is fake? (1-3): ")

if guess == answer:
    print("\n🏆 Correct! You're a fact detective!")
else:
    print(f"\n❌ Wrong! Fact {answer} was fake.")