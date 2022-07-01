#!/usr/bin/python3

"""The function multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("m_a must be a list of lists")
    for element2 in m_b:
        if not isinstance(element2, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for element in m_a:
        for ele in element:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError("m_a should contain only integers or floats")
    for element2 in m_b:
        for ele2 in element2:
            if not isinstance(ele2, int) and not isinstance(ele2, float):
                raise TypeError("m_b should contain only integers or floats")
    len_a = len(m_a[0])
    len_b = len(m_b[0])
    for size in m_a:
        if len(size) != len_a:
            raise TypeError("each row of m_a must be of the same size")
    for size2 in m_b:
        if len(size2) != len_b:
            raise TypeError("each row of m_b must be of the same size")
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = [[0 for i in range(0, len_b)] for j in range(0, len(m_a))]
    for row in range(0, len(m_a)):
        for num in range(0, len(new_matrix[0])):
            for n_a in range(0, len_a):
                new_matrix[row][num] += m_a[row][n_a] * m_b[n_a][num]
    return new_matrix
