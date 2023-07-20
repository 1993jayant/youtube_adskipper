import cv2
import numpy as np
import pyautogui
import time
import os


# faster version
# lopping over the template matching

# reading the templates
templates = []


# assign templates directory
templates_directory = "templates"

# iterate over template files
for template_file in os.listdir(templates_directory):
    template = cv2.imread(os.path.join(templates_directory, template_file), 0)
    if template is not None:
        templates.append(template)


# setting the threshold for confidence in template matching
threshold = 0.7

# alert box for stopping criteria
pyautogui.alert(
    text="Keep the mouse pointer on the top left corner of screen to stop the program",
    title="Stopping Criteria",
)

# continuous loop to check for YouTube ad
while True:
    time.sleep(1)
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode="L"))
    #     im1.save('im1.png')
    #     im1 = cv2.imread('im1.png', 0)

    # checking each template
    for template in templates:
        res = cv2.matchTemplate(im1, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        # checking if template is matched
        if loc[0].size != 0:
            # clicking on the first match
            pyautogui.click(list(zip(*loc[::-1]))[0])

    #     Stopping criteria
    if pyautogui.position() == (0, 0):
        pyautogui.alert(text="Adskipper is Closed", title="Adskipper Closed")
        break
