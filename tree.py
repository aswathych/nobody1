# GEO1000 - Assignment 2
# Authors:
# Studentnumbers:

import math


def distance(p1, p2):
    """Returns Cartesian distance (as float) between two 2D points"""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def point_angle_distance(pt, beta, distance):
    """Compute new point that is distance away from pt in direction beta"""
    return float(pt[0] + distance * math.cos(beta)), float(pt[1] + distance * math.sin(beta))


def absolute_angle(p1, p2):
    """Returns the angle (in radians) between the positive x-axis 
    and the line through two given points, p1 and p2"""
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])


def opposite_edge(p1, p2):
    """Compute and return the edge (as a tuple of two points p3 and p4) 
    parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    dis = distance(p1, p2)
    beta = math.pi / 2 + absolute_angle(p1, p2)
    p3 = point_angle_distance(p2, beta, dis)
    p4 = point_angle_distance(p1, beta, dis)
    return p3, p4


def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines 
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    dis = distance(p1, p2) * math.cos(alpha)
    beta = absolute_angle(p1, p2)
    return point_angle_distance(p1, beta + alpha, dis)


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square
    """
    return 'POLYGON (({:.4f} {:.4f}, {:.4f} {:.4f}, {:.4f} {:.4f}, {:.4f} {:.4f}, {:.4f} {:.4f}))'.format(p1[0], p1[1],
                                                                                                          p2[0], p2[1],
                                                                                                          p3[0], p3[1],
                                                                                                          p4[0], p4[1],
                                                                                                          p1[0], p1[1])


def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    if totalorder >= 0:
        p3, p4 = opposite_edge(p1, p2)
        geometry = as_wkt(p1, p2, p3, p4)
        area = (distance(p1, p2) ** 2)
        with open(filename, 'a') as fh:
            fh.write('{};{};{:.4f}\n'.format(geometry, currentorder, area))
        p1 = split_point(p4, p3, alpha)
        p2 = p3
        draw_pythagoras_tree(p1, p2, alpha, currentorder + 1, totalorder - 1, filename)
        p1 = p4
        p2 = split_point(p4, p3, alpha)
        draw_pythagoras_tree(p1, p2, alpha, currentorder + 1, totalorder - 1, filename)


if __name__ == "__main__":
    with open('out.wkt', 'w') as fh:  # 'with' statement closes 
        # file automatically
        fh.write("geometry;currentorder;area\n")
    draw_pythagoras_tree(p1=(5, 0),
                         p2=(6, 0),
                         alpha=math.radians(45),
                         currentorder=0,
                         totalorder=6,
                         filename='out.wkt')
