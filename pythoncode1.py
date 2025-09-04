import random

def hangman():
    words = ["apple", "train", "house", "plane", "grape"]
    word = random.choice(words)
    guessed = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        # Show word with guessed letters
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"
        print("Word:", display)

        # Check win
        if display == word:
            print("You win! 🎉 The word was:", word)
            break

        # Ask for input
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that.")
        elif guess in word:
            print("Good job!")
            guessed.append(guess)
        else:
            print("Wrong guess.")
            attempts -= 1
            guessed.append(guess)
            print("Attempts left:", attempts)

    else:
        print("Game over! 😢 The word was:", word)



hangman()        
