"""
Created by Lidor Karako (LK)
May, 2020
"""

import time  # requirement: 20 ms for frame
import cv2
import imutils
import matplotlib.pyplot as plt
import os
import numpy as np

from FindRefPoint.ref_tracker import GetRefPoint