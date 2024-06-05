# Create List of Filters

In this activity, you will learn to create a list of face filters.

<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10495566/readingvideo.gif" width = "480" height = "320">

Follow the given steps to complete this activity:

1. Create a list

- Open the main.py file.

- Declare a variable `menuMagic` and set and empty list to it.

  `menuImages = []`

- Create a `path` variable and set path `filters` to it.

  `path = "filters"`

- Declare a `pathList` variable and set `os.pathList` to get a list of all files stored in `path` variable.

  `pathList = os.listdir(path)`

- Sort all the images in the list using `pathList.sort()`.

  `pathList.sort()`

- Print the type of the list to check the type.

  `print(type(pathList))`

- Print the list of filters.

  `print(pathList)`

# Load all the images in the list

- Use `for` loop to loop through the `pathList` list.

  `for pathImg in pathList:`

- Use `cv2.imread()` to read the images from the list and store them in `img` variable.

  `img = (cv2.imread(path + "/" + pathImg, cv2.IMREAD_UNCHANGED))`

- Append the `img` in the `menuImages` list.

  `menuImages.append(img)`

- Use `cv2.imshow` to show the loaded image.

  `cv2.imshow("Face Filter App", menuImages[2])`

  `cv2.waitKey(1)`

- Save and run the code to check the output.
