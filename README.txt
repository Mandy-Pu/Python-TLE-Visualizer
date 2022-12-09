TLE Visualizer Python Application

This application calclulates the position of a constellation of satellites (e.g Iridium and Starlink) using the SGP4 python library. Matplotlib is used to plot the positions
of the satellite on a 3d scatter plot.

This application requires date and time as well as a path to a TLE file as input. TLE data can be acquired from Celestrak(https://celestrak.org): For Starlink 
(https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle)and for Iridium (https://celestrak.org/NORAD/elements/gp.php?GROUP=iridium&FORMAT=tle). Simply copy the
data from one of these links into a txt file, however, the txt file for Iridium TLE is already inside the project directory (Iridium.txt).

Required python libraries are: sgp4, matplotlib, and numpy.


URL to GitHub repository: 

URL to Docker Hub image: https://hub.docker.com/repository/docker/mandypu980/python-visualize

