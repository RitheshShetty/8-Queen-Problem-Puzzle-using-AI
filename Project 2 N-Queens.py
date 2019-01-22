import random

#no_of_queen = 0
global lst_pri, hur_cnt, opt_plc, succ_cnt, cntr, fail_cnt,violtn, succ_mve, fail_mve, moves, run_count, no_of_queen

no_of_queen = 0
lst_pri = 0
run_count = 0
succ_cnt = 0
fail_cnt = 0
moves = 0
succ_mve = 0
violtn = 0
fail_mve = 0
cntr = 0


#Finding next boards
def next_board(board):
    global hur_cnt, opt_plc
    for i in range(no_of_queen):
        check_board = board[:]
        minheur_count = get_hur_cnt(check_board)
        for j in range(no_of_queen):
            check_board[i] = j
            threat = get_hur_cnt(check_board)
            if(minheur_count >= threat):
                minheur_count = threat
                opt_plc[i] = j
        hur_cnt[i] = minheur_count


def hill_climbing():
    print("\nHILL CLIMBING\n")
    result_board = hill_climbing_algo()
    output_restart_final(result_board)

def hill_climbing_algo():
    global run_count
    board = generate_board()
    print_board(board)
    violtn = get_hur_cnt(board)
    while(violtn != 0):
        run_count += 1 
        board = steep_ascent_board(board)
        violtn = get_hur_cnt(board)
        if(violtn == 0):
            break
        else:
            board = generate_board()
            violtn = get_hur_cnt(board)
    return board


# Board with random queen placement
def generate_board():
    i = 0
    board = []
    while (i < no_of_queen):
        randmint = random.randint(0, (no_of_queen - 1))
        if (randmint not in board):
            board.append(randmint)
            i += 1
    return board



def print_board(board):
    print("Initial Board Position")
    for i in range(len((board))):
        for j in range(len(board)):
            if j == board[i]:
                print("1", end=" ")
            else:
                print("0",end=" ")
        print()
    print()


# Random Restart output
def output_restart_final(board):
    global run_count
    print("N Queen Solutions for {0}".format(len(board)))
    for row in range(len(board)):
        line = ""
        for column in range(len(board)):
            if (board[row] == column):
                line += "1 "
            else:
                line += "0 "
        print(line)
    print("\n")


#Calculate heuristics
def get_hur_cnt(check_board):
    violtn = 0
    global no_of_queen
    for i in range(no_of_queen):
        for j in range(i+1,no_of_queen):
            threat = abs(j-i)
            diagonal_threat =abs(check_board[i] - check_board[j])
            if(check_board[i] == check_board[j] or threat == diagonal_threat):
                violtn += 1
    return violtn




#Steepest Ascent board generation
def steep_ascent_board(board):
    global violtn, hur_cnt, lst_pri, opt_plc, cntr, succ_cnt, fail_cnt, succ_mve, fail_mve, no_of_queen
    moves = 0
    while(violtn != 0):
        moves += 1
        next_board(board)
        minheur_count = min(hur_cnt)
        if(minheur_count < lst_pri ):
            lst_pri = minheur_count
            if(minheur_count == 0):
                value_mincolumn = [i for i, val in enumerate(hur_cnt) if (val == minheur_count)]
                mincolumnvalue = random.choice(value_mincolumn)
                board[mincolumnvalue] = opt_plc[mincolumnvalue]           
                violtn = get_hur_cnt(board)
                succ_cnt += 1
                succ_mve += moves
            else:
                listitem = [i for i, val in enumerate(hur_cnt) if (val == minheur_count)]
                selected_queen = random.choice(listitem)         
                board[selected_queen] = opt_plc[selected_queen]
                violtn = get_hur_cnt(board)
        else:
            fail_cnt += 1
            fail_mve += moves
            break
    return board


#Main function 
if __name__ == '__main__':
    no_of_queen
    no_of_queen = int(input("Please input the number of Queens:"))
    print("\n")
    hur_cnt = list(0 for i in range(0, no_of_queen))
    opt_plc = list(0 for i in range(0, no_of_queen))
    hill_climbing()