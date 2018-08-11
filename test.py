import time
import random
import math
import numpy as np
import cv2
from PIL import Image
import cython_verify
import python_verify

def cython_test(num_verifs, tolerance):
    test_start_time = time.time()
    ver_times = []
    for i in range(num_verifs):
        # Choose random reference and test images
        ref_num = random.randrange(32)
        test_num = random.randrange(32)
        print("Reference Image: {}, Test Image: {}".format(ref_num, test_num))
        start_time = time.time()
        # Store images as 2D np array with elements being np arrays of len 3 containing RGB values
        ref_data = cv2.imread("images/white-{}.jpg".format(ref_num))
        test_data = cv2.imread("images/white-{}.jpg".format(test_num))
        # Cython verify
        fail_img_data = cython_verify.verify_image(ref_data, test_data, tolerance, i)
        # Save failure comparison image
        fail_img_data = np.asarray(fail_img_data)
        cv2.imwrite("failure_images/fail-{}.png".format(i), fail_img_data)
        ver_times.append(time.time() - start_time)
    print("Total time elapsed for {} random image verifications using Cython and cv2: {}".format(num_verifs, time.time() - test_start_time))
    print("Avg time per Cython verify: {}".format(sum(ver_times) / num_verifs))

def python_test(num_verifs, tolerance):
    test_start_time = time.time()
    ver_times = []
    for i in range(num_verifs):
        # Choose random reference and test images
        ref_num = random.randrange(32)
        test_num = random.randrange(32)
        print("Reference Image: {}, Test Image: {}".format(ref_num, test_num))
        start_time = time.time()
        ref_img = Image.open("images/white-{}.jpg".format(ref_num))
        test_img = Image.open("images/white-{}.jpg".format(test_num))
        # Store images as a list of tuples of 3 elements
        ref_data = ref_img.getdata()
        test_data = test_img.getdata()
        # Python verify
        fail_img_data = python_verify.verify_image(ref_data, test_data, tolerance, i)
        # Save failure comparison image
        fail_img = Image.new("RGB", (1024, 768))
        fail_img.putdata(fail_img_data)
        fail_img.save("failure_images/fail-{}.png".format(i))
        ver_times.append(time.time() - start_time)
    print("Total time elapsed for {} random image verifications using Python and PIL: {}".format(num_verifs, time.time() - test_start_time))
    print("Avg time per Python verify: {}".format(sum(ver_times) / num_verifs))
