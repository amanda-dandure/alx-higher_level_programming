#!/usr/bin/python3
""" Defining a Pascals triangle func """


def pascal_triangle(n):
    """ Representing Pascals tringle of size m

    Returns  list of int representing the triangle
    """
    if m <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != m:
        tri = triangles[-1]
        tmp = [1]
        for p in range(len(tri) - 1):
            tmp.append(tri[p] + tri[p + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
