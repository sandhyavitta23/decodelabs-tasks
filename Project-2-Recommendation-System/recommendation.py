# AI Recommendation System

# Categories and recommendations

recommendations = {
    "movies": ["Inception", "Interstellar", "Avengers", "The Dark Knight"],
    "books": ["Atomic Habits", "Rich Dad Poor Dad", "The Alchemist"],
    "music": ["Arijit Singh", "Imagine Dragons", "Taylor Swift"],
    "sports": ["Football", "Cricket", "Badminton"]
}

print("===== AI Recommendation System =====")
print()

print("Available Categories:")
for category in recommendations:
    print("-", category)

choice = input("\nEnter your favorite category: ").lower()

if choice in recommendations:
    print("\nRecommended for you:\n")

    for item in recommendations[choice]:
        print("✔", item)

else:
    print("\nSorry! No recommendations available.")
