# Simple audio recorder demo

This simple little project records audio in the the browser and sends the resulting WAV file to the server written in Python
(using the Flask library) where it can be fruther processed and its results displayed on screen.

This demo simply runs the ffprobe program (from the ffmpeg package) on the file that was previously written to temp.

This demo uses the audio recorder library from https://webaudiodemos.appspot.com/AudioRecorder/ (MIT license). The reason
for using that particular library is the ability to view audio in realtime before and during recording as well as the ability
to save the audio as a simple WAV file instead of OPUS, which is the only option for the built-in MediaRecorder component.  