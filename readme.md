#easy:notify

###What is it?
easy:notify aims to allow users simple access to notify.
Do you know the feeling when your program runs, but you need to do something else? For such things easy:notify is perfect!


<h2>How to use it</h2>
1) Install the APK on your android device
2) Put the "easy_notify.py" in the folder where your program is located
3) Start the android App and click on "Show Token", You will need this later!
4) import the "easy_notify.py" package using ```from easy_notify import send_message, token```
5) Now use ```token("YOUR_TOKEN_HERE")``` with your token
6) To send a simple message just use ```send_message(title="title", message="message")```
7) Thats it!

###Advanced Options
All atributes for ```send_message()```
>```vibrate=True|False```  de/activate the vibration

>```vibration_pattern="-_--__-``` Use a costum "Pattern", a "-" stands for 0.1 second vibration while a "_" stands for a pause of 0.1 seconds

>```server="costum server"``` costum server is your costum server if you dont want to use the public server

>```flash=True|False``` is a WIP feature ;)


###If you dont want/can use the Python-Module
Here is explained how to reach the server to build your own module/Application!

######ALL REQUESTS HAVE TO BE A POST-REQUEST!

>```/gettoken``` to receive a token from the Server

>```/write/[str:token]/[str:body]/[str:title]/[bool:vibrate]/[string:vibration_pattern]/[bool:flash]```
> NOTE: You need to pass the vibration-pattern like : "ab", this equals "-_"

>```/read[title|text]/[string:token]``` To read the Title/Text from the server

>```/readinfo/[string:token]``` to read more Information from the server


###To-Do:
- Add The Flash-light function


- Add a group-Feature

######btw, I know my code is a mess, Im still learning! But feel free to tell me what I can do better!
