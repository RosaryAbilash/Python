word = "secret"
# You can use Random Module and word list
guesses = []
errors = 7
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Error Left {errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        errors -= 1
        if errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word. It was {word}")
else:
    print(f"Game Over. The word was {word}")
