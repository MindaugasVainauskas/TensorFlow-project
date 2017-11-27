# Free drawn number recognition using Tensorflow library

#### *Mindaugas Vainauskas, 4th year Software Development course, Emerging Technologies Module, GMIT 2017*

## Description
 In this project I developed a prototype web application with simple interface that allows users to draw a number and then a Flask framework working with Tensorflow library in the backend returns a number that it thinks user drew.

## Technologies used
 - Flask Framework;
 - Python 3 programming language;
 - Bootstrap and HTML front end;
 - Fabric.js library for Canvas drawing.

## Downloading and running the project
To run the project you need to have python 3, tensorflow library and Flask framework installed on your machine.
### Installing python
Best way to install python on your machine is with Anaconda package that comes with several other handy tools, namely Jupyter Notebook. This package together with installation instructions is available from [Here](https://conda.io/docs/user-guide/install/index.html)

### Installing Tensorflow
Main function of this application is teaching the machine to recognise the user drawn images. As such Tensorflow machine learning library must be installed on the machine for application to work. Installation instructions for diferent Operating Systems can be found on the [Tensorflow Installation page](https://www.tensorflow.org/install/)

### Installing Flask framework
This application is ran as a Flask app and as such Flask framework must be installed for it to work. Flask Installation instructions are available from [Here](http://flask.pocoo.org/docs/0.12/installation/). Most up-to-date Flask version at the time of writing is v0.12.

After installing the above, project repository can be downloaded and ran from local machine. It runs on localhost:5000.

## Use instructions
Once application is launched, user is presented with simple interface comprised of Canvas, Submit button under it and Reset button beside Submit button. On right side from Canvas is the result area where machine guessed number is outputted.

User can draw on canvas right away once application is running. Once they want to get the guessed number back, users just need to press Submit button and guessed number is output on right side from Canvas. If users want to draw another number or want to clear current unsubmitted number, They need only to click Reset button to reset drawing area. 
