import random

print("===================================")
print("      WORD GUESSING GAME")
print("===================================")

words = ["python", "coding", "program", "developer", "computer"]
random.shuffle(words)   # random order

score = 0

for word in words:
    pattern = ""
    for i in range(len(word)):
        if i % 2 == 0:
            pattern += word[i]
        else:
            pattern += "_"

    attempts = 3
    print("\nGuess the word:")
    print("Word:", pattern)

    while attempts > 0:
        guess = input("Enter the full word: ").lower()

        if guess == word:
            print("🎉 Correct! Moving to next word.")
            score += 1
            break
        else:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts)

    if attempts == 0:
        print("\n💀 Game Over!")
        print("The correct word was:", word)
        break

print("\n==============================")
print("Game Finished!")
print("Your Score:", score, "/", len(words))
print("==============================")
