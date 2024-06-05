Drop the Filter
===================

In this activity, you will learn to find the filter selected by the user on the camera feed.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10495566/readingvideo.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Flag a variable for item selected from the filters menu

* Open the main.py file.

* Create flag variable `isImageSelected` and set it ot `False` to check if a filters is being dragged or not.

    `isImageSelected = False`



*  Set the `isImageSelected` to `False` if `indexFingerTop[1]` is greater then `indexFingerBottom[1]`.

    `if (indexFingerTop[1] > indexFingerBottom[1]):`

        `isImageSelected = False`

* If the image is selected then resize it and drag by passing `indexFingerTop` values to  `cvzone.overlayPNG`.

    `if (isImageSelected):`

        `image = cv2.resize(menuImages[menuChoice], (100, 100))`

        `cameraFeedImg = cvzone.overlayPNG(cameraFeedImg, image, [int(indexFingerTop[0]), int(indexFingerTop[1])])`

* Save and run the code to check the output.






