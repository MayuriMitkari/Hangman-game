import random

def hangman():
    # Predefined list of words
    words = ["python", "computer", "science", "hangman", "programming"]
    word = random.choice(words)  # Randomly choose a word
    guessed_word = ["_"] * len(word)  # Hide word with underscores
    guessed_letters = []
    attempts = 6  # Max incorrect guesses
    
    print("🎯 Welcome to Hangman Game!")
    print("You have 6 attempts to guess the word.")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord: ", " ".join(guessed_word))
        print("Guessed letters:", " ".join(guessed_letters))
        print(f"Attempts left: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check input validity
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1
    
    # Game result
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()
