<h1>easy:notify</h1>

<h3>What is it?</h3>
easy:notify aims to allow users simple access to notify.
Do you know the feeling when your program runs, but you need to do something else? For such things easy:notify is perfect!


<h3>How to use it</h3>

- Install the APK on your android device


- Put the "easy_notify.py" in the folder where your program is located


- Start the android App and click on "Show Token", You will need this later!


- import the "easy_notify.py" package using :
        ```python
        from easy_notify import send_message, token
        ```


- Now use 
        ```python
        token("YOUR_TOKEN_HERE")
        ``` 
  

- with your token


- To send a simple message just use 
        ```python
        send_message(title="title", message="message")
        ```
- Thats it!

<h3>Advanced Options</h3>
<h5>All atributes for "send_message()":</h5>

>```vibrate=True|False```  de/activate the vibration

>````vibration_pattern="-_--__-```` Use a costum "Pattern", a "-" stands for 0.1 second vibration while a "_" stands for a pause of 0.1 seconds

>````server="costum server"```` costum server is your costum server if you dont want to use the public server

>````flash=True|False```` is a WIP feature ;)


<h3>If you dont want/can use the Python-Module</h3>
Here is explained how to reach the server to build your own module/Application!

<h6>ALL REQUESTS HAVE TO BE A POST-REQUEST!</h6>

>```/gettoken``` 
to receive a token from the Server

>```/write/[str:token]/[str:body]/[str:title]/[bool:vibrate]/[string:vibration_pattern]/[bool:flash]```
> NOTE: You need to pass the vibration-pattern like : "ab", this equals "-_"

>```/read[title|text]/[string:token]``` To read the Title/Text from the server

>```/readinfo/[string:token]``` to read more Information from the server


<h3>To-Do:</h3>

- Add The Flash-light function


- Add a group-Feature


- Upload code to https://pypi.org/

<h6>btw, I know my code is a mess, Im still learning! But feel free to tell me what I can do better!</h6>
