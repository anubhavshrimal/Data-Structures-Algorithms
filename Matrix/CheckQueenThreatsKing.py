"""
Given the Coordinates of King and Queen on a chessboard, check if queen threatens the king.
"""


def check_threat(king_x, king_y, queen_x, queen_y):
    # If coordinates are non-integer or outside the bounds of the chessboard
    if not (validate(king_x) and validate(king_y) and validate(queen_x) and validate(queen_y)):
        return False
    
    # if king is in the vertical column of queen, king_x = queen_x
    # if king is in the horizontal row of queen, king_y = queen_y
    # if king is in the diagonal of queen, abs(king_y - queen_y) = abs(king_x - queen_x) because the will form a square
    if king_x == queen_x or king_y == queen_y or abs(king_y - queen_y) == abs(king_x - queen_x):
        return True

    return False


def validate(coordinate):
    if type(coordinate) is int and 1 <= coordinate <= 8:
        return True

    return False
    

print("Queen threatens King") if check_threat(1, 1, 5, 5) else print("Queen does not threaten King")
