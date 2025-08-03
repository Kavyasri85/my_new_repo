import random

def hangman():
    words = ["apple", "brain", "cloud", "ghost", "plant"]
    word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6
    display_word = ["_"] * len(word)

    print("\nWelcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while attempts_left > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠  Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠  You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    display_word[i] = guess
            print("✅ Correct!")
        else:
            attempts_left -= 1
            print("❌ Incorrect.")

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over! The word was:", word)

def main():
    while True:
        hangman()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()