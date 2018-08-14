# verify-image
Python vs Cython implementations of image comparison with tolerance.

Tested on i7 4600U in Ubuntu: Cython w/ cv2 achieves ~3.8x speed improvement over pure Python w/ PIL.

Experiment:
- In each trial, two 1024x768 images are randomly selected from a test bank of 30 images.
- Image comparison done with 35% tolerance.
- Failure images (pixel difference) saved every trial even if images pass.
- Average improvement over 5 experiments, 100 trials per experiment.
