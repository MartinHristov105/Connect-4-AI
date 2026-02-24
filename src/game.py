from src.utils import *

# Give estimates for AI moves.
def rate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    # Give him points if he makes good moves.
    if window.count(piece) == 4:
        score += 100000  # Winnig move.
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5000  # Strong attack.
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 500  # Prepare attack.

    # Punish him if he plays badly.
    if window.count(opp_piece) == 4:
        score -= 99999 
    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4999  # Blocks a player's strong attack.
    elif window.count(opp_piece) == 2 and window.count(EMPTY) == 2:
        score -= 499  # Blocks the player from preparing an attack.

    return score

# Different positions in which the checkers can be.
def calculate_position_score(board, piece):
    score = 0

    # Priority to center
    center_arr = [int(i) for i in list(board[:, COLUMN//2])]
    center_count = center_arr.count(piece)
    score += center_count

    # Horizontally
    for row in range(ROW):
        row_arr = [int(i) for i in list(board[row,:])]
        for col in range(COLUMN - 3):
            window = row_arr[col:col + WINDOW]
            score += rate_window(window, piece)

    # Vertically.
    for col in range(COLUMN):
        col_arr = [int(i) for i in list(board[:,col])]
        for row in range(ROW - 3):
            window = col_arr[row:row + WINDOW]
            score += rate_window(window, piece)

    # Bottom-left, top-right.
    for row in range(ROW - 3):
        for col in range(COLUMN - 3):
            window = [board[row + i, col + i] for i in range(WINDOW)]
            score += rate_window(window, piece)

    # Top-left, bottom-right.   
    for rol in range(ROW - 3):
        for col in range(COLUMN - 3):
            window = [board[row + 3 - i, col + i] for i in range(WINDOW)]
            score += rate_window(window, piece)

    return score

# Bottom of recursion.
def check_game_end(board):
    return win_move(board, PLAYER_PIECE) or win_move(board, AI_PIECE) or len(get_loc_free(board)) == 0   

# Algorithm
def minimax(board, depth, alpha, beta, maximizingPlayer):
    free_locations = get_loc_free(board)
    terminal = check_game_end(board)

    if depth == 0 or terminal:
        if terminal:
            if win_move(board, AI_PIECE):
                return (None, 10000000 + calculate_position_score(board, AI_PIECE))
            elif win_move(board, PLAYER_PIECE):
                return (None, -10000000 + calculate_position_score(board, AI_PIECE))
            else: # No more valid moves. 
                return (None, 0)    
        else: # Depth == 0.
            return (None, calculate_position_score(board, AI_PIECE))
        
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(free_locations)
        for col in free_locations:
            row = open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, AI_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
        
    else: # Minimizing player.
        value = math.inf
        column = random.choice(free_locations)
        for col in free_locations:
            row = open_row(board, col)
            temp_board = board.copy()
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

# Game.
def PLAYER_VS_AI(level):   
    # Create the board.
    board = create_board()

    # Flag to interrupt the game on win or draw.
    GAMEOVER = False
    
    # Who starts first.
    TURN = random.randint(PLAYER, AI)

    while not GAMEOVER:
        # Draws the board on the screen and then refreshes the drawing every time. 
        draw_board(SCREEN, board)

        # Track the mouse.
        for event in pygame.event.get():
            # Safe exit.
            if event.type == pygame.QUIT:
                sys.exit()

            # Move the mouse to move the checker.
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(SCREEN, BLACK, (0, 0, WIDTH, RECT))
                posx = event.pos[0]
                pygame.draw.circle(SCREEN, YELLOW, (posx, int(RECT / 2)), RAD)

            # Tracks the placement of a checker. Checks if it is the player's move and if the column is valid.
            if event.type == pygame.MOUSEBUTTONDOWN and TURN == PLAYER:
                posx = event.pos[0]
                col = int(math.floor(posx / RECT))

                if is_loc_free(board, col):
                    row = open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)
                    draw_board(SCREEN, board)
                    
                    if win_move(board, PLAYER_PIECE):
                        # Winner indication.
                        label = WINNER.render("PLAYER WINS!", 1, YELLOW)
                        SCREEN.blit(label, (150, 15))
                        GAMEOVER = True
                    
                    TURN = AI

        # AI move.
        if TURN == AI and not GAMEOVER:
            # Best column according to the minmax algorithm.
            col, _ = minimax(board, depth=level, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)

            if is_loc_free(board, col):
                # Short delay in placing the checkers.
                pygame.time.wait(500)
                row = open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                draw_board(SCREEN, board)

                if win_move(board, AI_PIECE):
                    # Winner indication
                    label = WINNER.render("AI WINS!", 1, BLUE)
                    SCREEN.blit(label, (150, 15))
                    GAMEOVER = True
            
                TURN = PLAYER

        # Checking for tie.
        if full_board(board) and not GAMEOVER:
            # Tie indication
            label = WINNER.render("DRAW!", 1, WHITE)
            SCREEN.blit(label, (150, 15))
            GAMEOVER = True

        # Short delay before program shutdown.
        if GAMEOVER:
            pygame.display.update()
            pygame.time.wait(3000)
            sys.exit()

# Test.
PLAYER_VS_AI(4)