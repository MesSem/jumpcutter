# jumpcutter
Automatically edits videos. Explanation here: https://www.youtube.com/watch?v=DQ8orIurGxw

## Some heads-up:

I programmed it in Python 2.

I have only ever tested this on Ubuntu 16.04... not sure if that makes a difference!

This program relies heavily on ffmpeg. It will start subprocesses that call ffmpeg, so be aware of that!

As the program runs, it saves every frame of the video as an image file in a
temporary folder. If your video is long, this could take a LOT of space.
I have processed 17-minute videos completely fine, but be wary if you're gonna go longer.

I want to use pyinstaller to turn this into an executable, so non-techy people
can use it EVEN IF they don't have Python and all those libraries. Jabrils
recommended this to me. However, my pyinstaller build did not work. :( HELP


##Start server

python3 -m venv venvJUMP
. venvJUMP/bin/activate

pip install -r ./requirements.txt   
FLASK_APP=backend.py FLASK_ENV=development flask run  

#Use it
localhost:5000?url=www.youtube.com/2342wqfwe32rf&sound=3&silent=2  :this will open a video player. As soon as the page will load the converted video is not ready so you need to wait a little and than update the page 
