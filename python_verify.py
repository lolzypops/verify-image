import math

def verify_image(ref, test, tol, cnt):
    """
    Pure Python reference implementation of Verify_Image
    Input:
    - ref  := List of 3-element tuples (Red, Green, Blue number values) representing the reference image's pixels
    - test := " " representing the test image's pixels
    - tol  := Tolerance for amount of difference in pixels
    - cnt  := Trial number indicator
    Output:
    - cmp_img_data := List of 3-element tuples representing the failure image's pixels - red indicates a difference in pixel value
    """
    pixel_sum, bad_pixel_cnt = 0, 0
    image_exact_match = 1
    err_sum, amount_diff, avg_err = 0.0, 0.0, 0.0
    cmp_img_data = []
    
    for j in range(1024 * 768): # Checking each pixel
        pixel_sum += 3
        if ref[j] != test[j]: # If the pixels aren't equal, check the differences in color value
            for k in range(3): # Checking each color value (RGB)
                if ref[j][k] != test[j][k]:
                    err_sum += math.sqrt((ref[j][k] - test[j][k]) ** 2)
            image_exact_match = 0
            amount_diff = math.sqrt((ref[j][0] - test[j][0]) ** 2 \
                                    + (ref[j][0] - test[j][0]) ** 2 \
                                    + (ref[j][0] - test[j][0]) ** 2)
            if (amount_diff / 1.5) > 255:
                cmp_img_data.append((1, 0, 0)) # pure red
            else:
                cmp_img_data.append((int(amount_diff / 1.5), 0, 0))
            bad_pixel_cnt += 1
        else:
            cmp_img_data.append((0, 0, 0))
    avg_err = err_sum / pixel_sum

    print("Image " + str(cnt))
    if image_exact_match:
        print("Image is exact match. Zero percent tolerance.")
    elif (avg_err / 255) < tol:
        print("Percentage tolerance given: {}%".format(tol * 100))
        print("Image passed w/ tolerance: {}%".format(avg_err / 255 * 100))
    else:
        print("Percentage tolerance given: {}%".format(tol * 100))
        print("Image passed w/ tolerance: {}%".format(avg_err / 255 * 100))
    print("----------------------------------------")
    return cmp_img_data