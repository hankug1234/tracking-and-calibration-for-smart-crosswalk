import numpy as np
import math

def normalize(a):
 c = [0,0]
 c[0] = a[0] / math.sqrt((a[0]**2) + (a[1]**2))
 c[1] = a[1] / math.sqrt((a[0]**2) + (a[1]**2))
 return c;


def cross_multiple_length2D(a, b):
 return a[0] * b[1] - a[1] * b[0];


def ccw(a, c, d):
 n1 = c - a
 n2 = d - a
 n1 = normalize(n1);
 n2 = normalize(n2);

 crossV = cross_multiple_length2D(n1, n2);

 if (crossV > 0):
    return False;
 else:
    return True;

def re_arrange(imgpoints,size):

        not_orderd_sequences = []
        not_orderd_sequences.append((0, imgpoints[0][0][0]))
        not_orderd_sequences.append((1, imgpoints[0][size - 1][0]))
        not_orderd_sequences.append((2, imgpoints[0][-size][0]))
        not_orderd_sequences.append((3, imgpoints[0][-1][0]))


        rearrange_leftbottom_top_to_rightbottom_top = list()
        rearrange_leftbottom_top_to_rightbottom_top.append(not_orderd_sequences[0])
        state = False

        for point in not_orderd_sequences[1:]:
            for index, coordination in enumerate(rearrange_leftbottom_top_to_rightbottom_top):
                if coordination[1][0] > point[1][0]:
                    rearrange_leftbottom_top_to_rightbottom_top.insert(index,point)
                    state = True
                    break
            if state == False:
                rearrange_leftbottom_top_to_rightbottom_top.append(point)
            else:
                state = False

        if rearrange_leftbottom_top_to_rightbottom_top[0][1][1] <= rearrange_leftbottom_top_to_rightbottom_top[1][1][1]:
            temp = rearrange_leftbottom_top_to_rightbottom_top[1]
            rearrange_leftbottom_top_to_rightbottom_top[1] = rearrange_leftbottom_top_to_rightbottom_top[0]
            rearrange_leftbottom_top_to_rightbottom_top[0] = temp

        if rearrange_leftbottom_top_to_rightbottom_top[2][1][1] <= rearrange_leftbottom_top_to_rightbottom_top[3][1][1]:
            temp = rearrange_leftbottom_top_to_rightbottom_top[3]
            rearrange_leftbottom_top_to_rightbottom_top[3] = rearrange_leftbottom_top_to_rightbottom_top[2]
            rearrange_leftbottom_top_to_rightbottom_top[2] = temp


        index = rearrange_leftbottom_top_to_rightbottom_top[0][0]
        if index == 0:
            horizontal = ccw(rearrange_leftbottom_top_to_rightbottom_top[0][1],
                             rearrange_leftbottom_top_to_rightbottom_top[1][1],
                             rearrange_leftbottom_top_to_rightbottom_top[3][1])
        elif index == 1:
            horizontal = ccw(rearrange_leftbottom_top_to_rightbottom_top[1][1],
                             rearrange_leftbottom_top_to_rightbottom_top[0][1],
                             rearrange_leftbottom_top_to_rightbottom_top[3][1])
        elif index == 2:
            horizontal = ccw(rearrange_leftbottom_top_to_rightbottom_top[2][1],
                             rearrange_leftbottom_top_to_rightbottom_top[3][1],
                             rearrange_leftbottom_top_to_rightbottom_top[0][1])
        else:
            horizontal = ccw(rearrange_leftbottom_top_to_rightbottom_top[3][1],
                             rearrange_leftbottom_top_to_rightbottom_top[2][1],
                             rearrange_leftbottom_top_to_rightbottom_top[0][1])


        if (index == 0 and horizontal == True):
            objp = np.zeros((size * size, 3), np.float32)
            objp[:, :2] = np.mgrid[0:size, 0:size].T.reshape(-1, 2)

        elif (index == 0 and horizontal == False):
            objp = np.zeros((size * size, 3), np.float32)
            x, y = np.mgrid[0:size, 0:size]
            n = np.array([y, x])
            n = n.T.reshape(-1, 2)
            objp[:, :2] = n
            objp = [objp]

        elif (index == 1 and horizontal == True):
            objp = np.zeros((size * size, 3), np.float32)
            n = np.mgrid[0:size, 0:size].T
            for column_is_ascending_order in range(0, len(n)):
                n[column_is_ascending_order] = np.sort(n[column_is_ascending_order], axis=0)[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        elif (index == 1 and horizontal == False):
            objp = np.zeros((size * size, 3), np.float32)
            x, y = np.mgrid[0:size, 0:size]
            n = np.array([y, x])
            n = n.T
            for column_is_ascending_order in range(0, len(n)):
                n[column_is_ascending_order] = np.sort(n[column_is_ascending_order], axis=0)[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        elif (index == 2 and horizontal == True):
            objp = np.zeros((size * size, 3), np.float32)
            n = np.mgrid[0:size, 0:size]
            n = n.T
            n = n[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        elif (index == 2 and horizontal == False):
            objp = np.zeros((size * size, 3), np.float32)
            x, y = np.mgrid[0:size, 0:size]
            n = np.array([y, x])
            n = n.T
            n = n[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        elif (index == 3 and horizontal == True):
            objp = np.zeros((size * size, 3), np.float32)
            n = np.mgrid[0:size, 0:size]
            n = n.T
            n = n[::-1]
            for column_is_ascending_order in range(0, len(n)):
                n[column_is_ascending_order] = np.sort(n[column_is_ascending_order], axis=0)[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        else:
            objp = np.zeros((size * size, 3), np.float32)
            x, y = np.mgrid[0:size, 0:size]
            n = np.array([y, x])
            n = n.T
            n = n[::-1]
            for column_is_ascending_order in range(0, len(n)):
                n[column_is_ascending_order] = np.sort(n[column_is_ascending_order], axis=0)[::-1]
            objp[:, :2] = n.reshape(-1, 2)
            objp = [objp]

        return objp







