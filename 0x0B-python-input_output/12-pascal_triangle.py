#!/usr/bin/python3
""" Defining a Pascals triangle func """


def pascal_triangle(n):
    """ Representing Pascals tringle of size m

    Returns  list of int representing the triangle
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
