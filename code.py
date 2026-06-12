# Define the dictionary of 10 English to Russian words
eng_rus_dict = {
    "Hello": "Привет",
    "Goodbye": "Пока",
    "Cat": "Кот",
    "Dog": "Собака",
    "Book": "Книга",
    "Water": "Вода",
    "Friend": "Дуг",
    "Sun": "Солнце",
    "House": "Дом",
    "Food": "Еда"
}

# Accessing a specific word
print(f"The Russian translation for 'Cat' is: {eng_rus_dict['Cat']}")

# Displaying the entire dictionary
print("\n--- English to Russian Dictionary ---")
for eng, rus in eng_rus_dict.items():
    print(f"{eng}: {rus}")