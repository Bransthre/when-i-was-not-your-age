def get_minor(matrix, i):
    """ Returns the minor of the matrix excluding column i of the original matrix.

    Args:
        matrix: The original matrix
        i: The column number to be excluded
    
    Return:
        A 2D list representing a square matrix that is the desired minor.
    """
    dimension = len(matrix)
    assert dimension > i, 'invalud column number has been provided!'

    minor = []
    for rows in matrix[1:]:
        minor.append(rows[:i] + rows[i + 1:])
    return minor

def determinant(matrix):
    """ Returns the determinant of a matrix

    Args:
        matrix: a 2D list representing a matrix
    
    Returns:
        A flaoting point number representing the determinant of the matrix.
    """
    row_lengths = [len(r) for r in matrix]
    assert row_lengths == sorted(row_lengths), "Some row lengths in this matrix are not same"
    assert row_lengths[0] == len(matrix), f"Inputted matrix is not square matrix"

    dimension = row_lengths[0]

    #base case
    if dimension == 1:
        return matrix[0][0]
    
    #recursive case
    total_det, curr_sign = 0, 1
    for ind in range(dimension):
        total_det += curr_sign * matrix[0][ind] * determinant(get_minor(matrix, ind))
        curr_sign *= -1
    
    return total_det