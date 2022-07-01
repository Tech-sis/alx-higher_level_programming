#!/usr/bin/python3
""" lazy multi """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Using numpy """
    new_matrix = numpy.matmul(m_a, m_b)
    return new_matrix
