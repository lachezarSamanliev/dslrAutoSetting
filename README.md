# dslrAutoSetting

This project includes a MVC model website, which is hosted on a Raspberry Pi, giving a user the ability to manually take and review photos taken from a DLSR Camera.
One separate functionality is the code being able to automaticaly adjust the Shutter, Aperture, and ISO settings, based on the amount of light that the camera is receiving.
Another included functionality is to determine a dominant color (Red, Green, Blue) in the photo and mark it so it can be filtered in the separata color pages. 

Since the Raspberry Pi has a rather limited capability, the way which I decided to analyze the pictures was by starting with 5 small "circles" on designated pixels
and increasing their size if the first circle had positive outputs in terms of light, color similarity, and percentage of the total area scanned. 
Representation of the circles explained above: https://drive.google.com/file/d/1XRXYHxi11ajOCdhgGuFR_xmIVp5bYJLn/view?usp=sharing


Sample video of the working project can be found here: https://youtu.be/NBSVV75398w

Python Libraries used in the project:
  -Pillow
  -NumPy
  -gphoto2
