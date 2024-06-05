Create Filter Menu
===================

In this activity, you will learn to create a filter menu.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10495566/readingvideo.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Import libraries

* Open the main.py file.

* Import math library

    `import math`

* Import cvzone library

    `import cvzone`

* Count the number of images in the `menuList`.

    `menuCount = len(menuImages)`

* Get width and height of final output screen.

    `wHeight, wWidth, wChannel = cameraFeedImg.shape`

* Set initial position to 0 (menu will start displaying at 0).

   ` x = 0`

* Calculate increments to display next menuImage.

    `xIncrement = math.floor(wWidth / menuCount)`

2. Overlay menu images to camera feed.
* Use for loop to loop through the `menuImages`.
        
        `for image in menuImages:`

* Set Margin to 20.

    `margin = 20`

* Resize the image using `cv2.resize()` and by decreasing the margin from the `xIncrement` values.
    
    `image = cv2.resize(image, (xIncrement - margin, xIncrement - margin))`

* Overlay the image on the camera feed using `cvzone.overlayPNG` and increament the `x` with `xIncrement`.

    `cameraFeedImg = cvzone.overlayPNG(cameraFeedImg, image, [x, 0])`

    `x = x + xIncrement`

* Save and run the code to check the output.






