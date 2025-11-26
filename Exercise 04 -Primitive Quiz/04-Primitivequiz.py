quiz = {
    "France": "Paris",
    "Malta": "Valletta",
    "Cyprus": "Nicosia",
    "Georgia": "Tbilisi",
    "Poland": "Warsaw",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Slovenia": "Ljubljana",
    "Estonia": "Tallinn",
    "Latvia": "Riga"
}

score = 0

for country, capital in quiz.items():
    ans = input(f"Capital of {country}? ").strip().lower()
    if ans == capital.lower():
        print(f"{country}:  Correct ({capital})")
        score += 1
    else:
        print(f"{country}:  Wrong (Answer: {capital})")

print(f"\nYou scored {score}/{len(quiz)}")
