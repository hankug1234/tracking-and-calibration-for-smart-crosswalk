import numpy as np
import cv2


def homogeneous_coordinate(vec):
    return np.array([vec[0], vec[1], 1])


def undistort(vec, distortV, mtx):
    return cv2.undistortPoints(vec, mtx, distortV)[0][0]


def to_realworld_coordinate(inv, vec, transv):
    cameraworld_zero = np.array([0, 0, 0])
    transv = np.array(transv, dtype='f')
    transv = transv.reshape(-1, 1).transpose()
    cameraworld_camera_location = cameraworld_zero - transv[0]
    t_vec = vec - transv[0]
    realworld_camera_location = np.dot(inv, cameraworld_camera_location)
    realworld_vec = np.dot(inv, t_vec)

    dr = realworld_vec - realworld_camera_location
    k = -(realworld_camera_location[2] / dr[2])
    re = [realworld_camera_location[0] + k * dr[0], realworld_camera_location[1] + k * dr[1],
          realworld_camera_location[2] + k * dr[2]]
    return re


def translate_to_realworld_coordinate(vec, inRevecsMetrix, tvecs, dist, Mtx):
    vec = undistort(vec, dist, Mtx)
    vec = homogeneous_coordinate(vec)
    vec = to_realworld_coordinate(inRevecsMetrix, vec, tvecs)
    return vec
