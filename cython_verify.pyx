import numpy as np
from libc.math cimport sqrt

cpdef unsigned char [:, :, :] verify_image(unsigned char [:, :, :] ref, unsigned char [:, :, :] test, float tolerance, int cnt):
    cdef int x, y, h, w, exact_match, bad_pix_cnt, pix_sum
    cdef float err_sum, amt_dif, avg_err
    exact_match, bad_pix_cnt, pix_sum = 1, 0, 0
    err_sum, amt_dif, avg_err = 0.0, 0.0, 0.0
    h = ref.shape[0]
    w = ref.shape[1]
    
    cmp_img_data = np.zeros((768, 1024, 3), dtype="uint8")
    
    for y in range(h):
        for x in range(w):
            pix_sum += 3
            if ref[y, x, 0] != test[y, x, 0] and ref[y, x, 0] != test[y, x, 0] and ref[y, x, 0] != test[y, x, 0]:
                exact_match = 0
                amt_dif = sqrt((ref[y, x, 0] - test[y, x, 0]) ** 2) \
                + sqrt((ref[y, x, 1] - test[y, x, 1]) ** 2) \
                + sqrt((ref[y, x, 2] - test[y, x, 2]) ** 2)
                err_sum += amt_dif
                
                if (amt_dif / 1.5) > 255:
                    cmp_img_data[y][x] = np.array([0, 0, 1])
                else:
                    cmp_img_data[y][x] = np.array([0, 0, int(amt_dif / 1.5)])
            else:
                cmp_img_data[y][x] = np.array([0, 0, 0])
    avg_err = err_sum / pix_sum

    print("Image " + str(cnt))
    if exact_match:
        print("Image is exact match. Zero percent tolerance.")
    elif (avg_err / 255) < tolerance:
        print("Percent tolerance given: {}%".format(tolerance * 100))
        print("Image passed w/ tolerance: {}%".format((avg_err / 255) * 100))
    else:
        print("Percentage tolerance given: {}%".format(tolerance * 100))
        print("Percentage of failure: {}%".format(avg_err / 255 * 100))
    print("----------------------------------------")
    return cmp_img_data