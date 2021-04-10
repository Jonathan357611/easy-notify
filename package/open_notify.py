import requests
import urllib
import urllib.parse





global is_token_defined, nothing
nothing = ""
is_token_defined = False
class TokenError(Exception):
    pass
class send_message_error(Exception):
    pass
def token(token):
    global TOKEN, is_token_defined
    is_token_defined = True
    TOKEN = token
def send_message(title="Title", message="none", vibrate=True, vibration_pattern="---", server="https://easynotify.pythonanywhere.com/", flash=False):
    if is_token_defined == False:
        raise TokenError("\nPlease provide a Token using:\ntoken(\"YOUR_TOKEN_HERE\")")
    if message == "none":
        raise send_message_error("\nPlease define message!")
    if flash == True:
        print("flash currently not available!")
    else:
        final_vibration_pattern = ""
        for letter in vibration_pattern:
            if letter == "-":
                final_vibration_pattern = f"{final_vibration_pattern}a"
            if letter == "_":
                final_vibration_pattern = f"{final_vibration_pattern}b"
        if vibrate == True or vibrate == False:
            response = requests.post(server + f"write/{TOKEN}/{urllib.parse.quote(message, safe=nothing)}/{urllib.parse.quote(title, safe=nothing)}/{str(vibrate)}/{final_vibration_pattern}/{str(flash)}")      #SERVERIP/<Token>/<message>/<title>/<vibrate True|False>/<The pattern the phone should be vibrating>/<flash True|False>
            print(urllib.parse.quote(message))
            return response.text
        else:
            raise TokenError("\nPlease define vibration as True or False!")
def send_group_message(title="Title", message="none", vibrate=True, vibration_pattern="---", server="https://easynotify.pythonanywhere.com/", flash=False):
    if is_token_defined == False:
        raise TokenError("\nPlease provide a Token using:\ntoken(\"YOUR_TOKEN_HERE\")")
    else:
        final_vibration_pattern = ""
        for letter in vibration_pattern:
            if letter == "-":
                final_vibration_pattern = f"{final_vibration_pattern}a"
            if letter == "_":
                final_vibration_pattern = f"{final_vibration_pattern}b"
        if vibrate == True or vibrate == False:
            response = requests.post(server + f"write_to_group/{TOKEN}/{urllib.parse.quote(message, safe=nothing)}/{urllib.parse.quote(title, safe=nothing)}/{str(vibrate)}/{final_vibration_pattern}/{str(flash)}")
            print(urllib.parse.quote(message))
            return response.text
        else:
            raise TokenError("\nPlease define vibration as True or False!")
if __name__ == '__main__':
    print(":)")