Create Vertical Filter
=======================

In this activity, you will learn select and drag the vertical filter.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10495566/readingvideo.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Drag vertical filters.

* Open the main.py file.

* Check x axis i.e index[0] i.e finger is on the vertical menu.

    `if (indexFingerTop[0] < 100):`

        `i = 0`

* Replace xIncrement with yIncrement and change wWidth to w Height so that you can pick the right image

    `while (yIncrement*i <= wHeight):`

* Check if `indexFingerTop[1]` is less then `yIncrement*i`.

    `if (indexFingerTop[1] < yIncrement*i):`

        `menuChoice = i-1`
        
        `isImageSelected = True`

* Save and run the code to check the output.






