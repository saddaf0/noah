Create Vertical Filter
=======================

In this activity, you will learn to create vertical filter.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10495566/readingvideo.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Flag a variable for item selected from the filters menu

* Open the main.py file.

* Create yIncrement variable.

    `yIncrement = math.floor(wHeight / menuCount)`


* Use value `yIncrement` instead of `xIncrement` in `cv2.resize()`.

    `image = cv2.resize(image, (yIncrement - margin, yIncrement - margin))`

* Use value of y while displaying the image and keep x =0.

    `cameraFeedImg = cvzone.overlayPNG(cameraFeedImg, image, [0, y])`

* Change the y location instead of the x location, increment `y` by `yIncrement` and subtract `4` from it.

    `y = y + yIncrement - 4`

* Save and run the code to check the output.






