from utils import output
from utils.input import Input

puzzle_input = Input()
numbers = puzzle_input.extract_first_row().split(',')
boards = puzzle_input.blocks_of_maps()

winning_board = winning_number = losing_board = None
for number in numbers:
    everyone_won = False
    for board in boards:
        if board.mark:
            continue

        existing = board.get_by_value(number)
        if existing:
            existing.mark = True

        row_checklist = [True for i in range(5)]
        column_checklist = [True for i in range(5)]
        for point in board.points:
            if not point.mark:
                row_checklist[point.y] = column_checklist[point.x] = False

        if row_checklist.count(True) or column_checklist.count(True):
            board.mark = True
            if not winning_board:
                winning_board = board
                winning_number = number

        if not next((board for board in boards if not board.mark), None):
            everyone_won = True
            break

    if everyone_won:
        break

winner_score = sum([int(x.value) if not x.mark else 0 for x in winning_board.points]) * int(winning_number)
loser_score = sum([int(x.value) if not x.mark else 0 for x in board.points]) * int(number)

output.solution(winner_score, loser_score)
