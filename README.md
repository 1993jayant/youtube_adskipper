# youtube_adskipper
This is a program written in python programming language. It automatically clicks on the 'skip ad' button on the youtube ads. It uses opencv library's Template Matching functionality to do that.

It loads templates of skip ad button for various resolution and zoom sizes of the screen to make it platform independent.

It is successfully working on different machines with different resolutions.

I have used pyautogui library to take the screenshots of the screen and then in a while loop it matches with different templates for the screenshot. Whenever it finds a match with 70 percent confidence it clicks on the skip ad button automatically.

I have used 70 percent as the confidence to initiate the click after meticulous experimentation. One can change it to check for the change in the performance.

It does not take much RAM, neither it requires huge computational effort. I have optimized it a little bit to decrease its space and time complexity.

It does not have any graphical user interface(GUI). I have used a very ingenious technique to come out of the while loop whenever one wants to stop the script. I have used an conditional statement to check for the coordinates of the mouse pointer. If the coordinates are (0,0), i.e., if the mouse is at the top left corner of the screen, it breaks out of the while loop.

You can launch the app by running youtube_adskipper.exe file directly.

You can launch the app by running youtube_adskipper.exe file directly.