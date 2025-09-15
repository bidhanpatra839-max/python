questions = [
    {"question": "What is the capital of India?", "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "Who is known as the father of Python?", "options": ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"], "answer": "Guido van Rossum"}
]

prize = 0
for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['question']}")
    for idx, option in enumerate(q['options'], 1):
        print(f"{idx}. {option}")
    
    choice = int(input("Enter your choice (1-4): "))
    if q['options'][choice - 1] == q['answer']:
        prize += 1000
        print("✅ Correct! Prize money:", prize)
    else:
        print("❌ Wrong Answer! Game Over.")
        break

print("\nYour Total Prize Money:", prize)
