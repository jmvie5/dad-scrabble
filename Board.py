class Board:
    def __init__(self, size=28):

        self.size = size
        self.available_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.letters_on_board = []
        # Initialize the board with empty spaces (' ')
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.word_count = 0


    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.grid])
    

    def place_tile(self, x, y, tile):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[y][x] = tile
        else:
            raise ValueError("Invalid coordinates", x, y)
        
        
    def add_word(self, word):
        word_is_valid, message = self.is_valid_word(word)
        if not word_is_valid:
            raise ValueError(f"Invalid word : {message}")

        start_x, start_y, direction = self.get_word_position(word)
       
        # Place each letter of the word on the board
        for i, letter in enumerate(word):
            
            if direction == 'horizontal':
                self.place_tile(start_x + i, start_y, letter)
            elif direction == 'vertical':
                self.place_tile(start_x, start_y + i, letter)
            else:
                raise ValueError("Invalid direction. Use 'horizontal' or 'vertical'.")
            
            

        # Validate board before adding the word for real
        is_board_valid, message = self.validate_board()

        if not is_board_valid:
            raise ValueError(f"Invalid board : {message}")
        
        
        for letter in word:
            # Add played letters to letter on board
            if letter not in self.letters_on_board:
                self.letters_on_board.append(letter)
            
            # Remove used letters from available letters
            if letter in self.available_letters:
                self.available_letters.remove(letter)
        
    
        self.word_count += 1
        

    def get_word_position(self, word):
        # Logic to determine where to place the word on the board
        
        # If no words on the board
        if self.word_count == 0:
            start_x = round(self.size/2 - len(word)/2)
            start_y = round(self.size/2)
            direction = "horizontal"
            return start_x, start_y, direction

        # If words on the board, we need to check where the word is crossing and what direction the new word is going to be
        common_letter = (set(word) & set(self.letters_on_board)).pop()
        if not common_letter:
            raise ValueError("A new word needs one common letter to be placed.")
        
        # Find position of common_letter
        start_x, start_y = self.get_letter_position_in_board(common_letter)

        # If no letter at the left and right of common_letter, direction of new word is horizontal, else vertical
        if self.grid[start_y][start_x-1] == " " and self.grid[start_y][start_x+1] == " ":
            direction = "horizontal"
        elif self.grid[start_y-1][start_x] == " " and self.grid[start_y+1][start_x] == " ":
            direction = "vertical"
        else:
            raise ValueError("Can't place this word, conflict with other letters.")
        
        if direction == "horizontal":
            start_x -= word.index(common_letter)
        elif direction == "vertical":
            start_y -= word.index(common_letter)

        return start_x, start_y, direction
    

    def get_letter_position_in_board(self, letter):
        for row in self.grid:
            for tile in row:
                if tile == letter:
                    start_x = row.index(letter)
                    start_y = self.grid.index(row)
                    return start_x, start_y
        return None, None


    def is_valid_word(self, word):
        # If word has the same letter twice, it's not valid
        for i in range(len(word)):
            if word[i] in word[:i]:
                return False, "Can't have the same letter twice in the same word."

        common_letter = set(word) & set(self.letters_on_board)
        # If board is not empty and there is no common letter with the word and the board, it's not a valid word
        if self.word_count != 0 and len(common_letter) == 0:
            return False, "Your word has no common letters with words on the board."
            
        # We check if the same letter is used twice on the board after placing the word on. 
        
        return True, "Word is valid"
    

    def validate_board(self):
        # Check if all letters are used exactly once
        used_letters = []
        for row in self.grid:
            for tile in row:
                if tile != " ":
                    used_letters.append(tile)
        
        count_list = []
        for letter in used_letters:
            if letter not in count_list:
                count_list.append(letter)
            elif letter in count_list:
                return False, "You have repeated letters on the board."
            
        return True, "Board is valid"
        
    
    def get_score(self):
        # TODO implement real scrabble score per letter and return total score for the used letters
        return len(self.letters_on_board)