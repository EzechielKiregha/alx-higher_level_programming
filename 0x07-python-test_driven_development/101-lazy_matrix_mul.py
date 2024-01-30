#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
        
    Returns:
        np.ndarray: The result of the matrix multiplication.
        
    Raises:
        ValueError: If the matrices are not compatible for multiplication.
        TypeError: If the input matrices are not lists of lists.
    """
    # Check if inputs are lists of lists
    if not (isinstance(m_a, list) or isinstance(m_b, list)):
        raise TypeError("Inputs must be lists of lists")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    # Check if input matrices are 2D arrays
    if m_a.ndim != 2 or m_b.ndim != 2:
        raise ValueError("Input matrices must be 2D arrays")

    # Check if matrices are compatible for multiplication
    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("Matrices are not compatible for multiplication")

    # Perform matrix multiplication
    result = np.matmul(m_a, m_b)
    return result
