# Simple audio recorder demo

This simple little project records audio in the the browser and sends the resulting WAV file to the server written in Python
(using the Flask library) where it can be fruther processed and its results displayed on screen.

This demo simply runs the ffprobe program (from the ffmpeg package) on the file that was previously written to temp.