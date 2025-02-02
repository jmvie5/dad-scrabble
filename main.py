from Board import Board, DadScrabbleError

def main():
    board = Board(15)
    print("Welcome to Dad Scrabble! Enjoy the game!\nType !exit to end the game.\nEnter your first word: ")

    game_over = False
    while not game_over:
        word = input().upper()

        if word == "!EXIT":
            game_over = True
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
