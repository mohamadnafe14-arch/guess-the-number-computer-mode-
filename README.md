# Guess The Number

A simple Python command-line game where the computer chooses a secret number and the player tries to guess it.

## How It Works

The program:

- picks a random number between `1` and `10`
- asks the player to guess the number
- tells the player if the guess is too low or too high
- keeps going until the correct number is guessed

When the player wins, the game prints a congratulatory message with the correct number.

## Example

```text
Guess a number between 1 and 10: 4
Sorry, guess again. Too low.
Guess a number between 1 and 10: 8
Sorry, guess again. Too high.
Guess a number between 1 and 10: 6
Yay, congrats. You have guessed the number 6 correctly!
```

## Requirements

- Python 3

This project only uses Python's built-in `random` module, so no extra packages are required.

## How To Run

Open a terminal in this folder and run:

```bash
python guess_the_number.py
```

If your system uses `python3`, run:

```bash
python3 guess_the_number.py
```

## Project Structure

```text
guess_the_number(computer)/
|-- guess_the_number.py
`-- README.md
```

## Code Highlights

This project is a good beginner exercise for practicing:

- importing and using modules
- generating random numbers
- writing functions
- using `while` loops
- comparing values with conditional statements
- collecting user input from the terminal

## Next Ideas

Here are a few ways to make the game even better:

- Count how many guesses the player used.
- Let the player choose the maximum number.
- Handle invalid input, like letters or blank guesses.
- Add a replay option after the game ends.
- Create a reverse version where the player chooses a number and the computer guesses.
