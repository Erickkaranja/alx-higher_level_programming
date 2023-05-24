#!/usr/bin/python3
# Author Erick Karanja
import numpy as np
'''

'''


def lazy_matrix_mul(m_a, m_b):
    '''function that multiplies two matrices.'''
    if (not isinstance(m_a, list) or not isinstance(m_b, list) or
            m_a == [] or m_b == []):
        raise TypeError("matrix must be type list and not empty")

    """if (not all(isinstance(ele, int) for ele in m_a) or
            not all(isinstance(ele, float) for ele in m_a)):
        raise TypeError("Elements must be of type int or float")"""

    result = np.dot(m_a, m_b)
    return result
