# verify-image
Python vs Cython implementations of image comparison with tolerance.

Tested on i7 4600U in Ubuntu: Cython w/ cv2 achieves ~3.8x speed improvement over pure Python w/ PIL.

### Experiment:
- In each trial, two 1024x768 images are randomly selected from a test bank of 30 images.
- Image comparison done with 35% tolerance.
- Failure images (pixel difference) saved every trial even if images pass.
- Average improvement over 5 experiments, 100 trials per experiment.

### Requirements:
- Python 3 recommended, everything also available on Python 2.7
- [Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html)
- PIL
- [OpenCV](https://pypi.org/project/opencv-python/)

### Usage:
1. In order to run the Cython test, you need to compile `cython_verify.pyx` file through `setup.py`
   * Run `python3 setup.py build_ext --inplace` to build the c file
2. Run `python3` in cmd, `import test` and call the test functions as you please
   
