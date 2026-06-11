"""
Option A is incorrect itself as cv2.imread gives images in BGR format, not in RGB.
Option B is correct, since in grayscale images only a
single channel helps to impart colour
Option C is also correct, when we want that cv2.waitkey() remains for long
we put 0, and putting 1 there means image is staying for 1 millisecond,
after that it turns out.
Option 4 is incorrect as the co-ordinates are for boundary corners not for centre.
"""