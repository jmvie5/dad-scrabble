from Board import Board, DadScrabbleError
from translations import translations

def main():
    
    lng_opt = ["fr", "en"]
    lng = ""
    while lng not in lng_opt:
        lng = input("Pour jouer en français, tapez \"fr\". To play in english, enter \"en\".\n")

    t = translations[lng]
    print(t["Welcome to Dad Scrabble!\nType !exit to end the game.\nEnter your first word: "])

    game_over = False
    valid_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    board = Board(t)
    
    while not game_over:
        word = input().upper()

        if word == "!EXIT":
            game_over = True
            continue

        # Check if the word contains only valid characters
        try:
            for char in word:
                if char not in valid_char:
                    raise ValueError("Invalid character detected. Please enter a valid word.")

        except ValueError as e:
            print(e)
            print(f"Available letters: {board.available_letters}\nEnter your next word: ")
            continue
        
        try:
            board.add_word(word)
        except DadScrabbleError as e:
            print(e)
            print(f"Available letters: {board.available_letters}\nEnter your next word: ")
            continue

        print(board)

        if len(board.available_letters) == 0:
            game_over = True
            continue

        print(f"Available letters: {board.available_letters}\nEnter your next word: ")

    print(f"Game over! Your final score is {board.get_score()}.")


if __name__ == "__main__":
    main()
