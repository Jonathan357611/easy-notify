from flask import Flask
from flask_restful import Api, Resource
import os
from os import listdir
from os.path import isfile, join
import secrets
import urllib.parse

# from sqlalchemy import SQLAlchemy

#x = os.listdir("token")
#print(x)
app = Flask(__name__)
api = Api(app)



class WriteText(Resource):
    def get(self, token, text, title, vibrate, vibration_pattern, flash):
        return "Only POST-Requests!"

    def post(self, token, text, title, vibrate, vibration_pattern, flash):
        try:
            with open(f"token/{token}/title", "w") as f:
                f.write(title)
            with open(f"token/{token}/text", "w") as f:
                f.write(text)
            with open(f"token/{token}/info", "w") as f:
                f.write(f"VIBRATE={vibrate}\nPATTERN={vibration_pattern}\nFLASH={flash}")
            return "written"
        except Exception as e:
            return "invalid"


class ReadTitle(Resource):
    def get(self, token):
        return "Only POST-Requests!"

    def post(self, token):
        try:
            with open(f"token/{token}/title", "r") as f:
                title = f.read()
            with open(f"token/{token}/title", "w") as f:
                f.write("")
            return urllib.parse.unquote(title)
        except:
            return "invalid"


class ReadText(Resource):
    def get(self, token):
        return "Only POST-Requests!"

    def post(self, token):
        try:
            with open(f"token/{token}/text", "r") as f:
                text = f.read()
            with open(f"token/{token}/text", "w") as f:
                f.write("")
            if urllib.parse.unquote(text) == "none":
                text = ""
            return urllib.parse.unquote(text)
        except:
            return "invalid"


class gettoken(Resource):
    def get(self):
        return "Only POST-Requests!"

    def post(self):
        used_tokens = [f for f in listdir("token") if isfile(join("token", f))]
        token = secrets.token_urlsafe(16)
        while token in used_tokens:
            token = secrets.token_urlsafe(16)
        os.mkdir(f"token/{token}")
        with open(f"token/{token}/title", "x") as f:
            pass
        with open(f"token/{token}/text", "x") as f:
            pass
        with open(f"token/{token}/info", "x") as f:
            pass
        return token


class read_info(Resource):
    def get(self):
        return "Only POST-Requests!"

    def post(self, token):
        with open(f"token/{token}/info", "r") as f:
            info = f.read()
            return info


class GroupWrite(Resource):
    def get(self, token, text, title, vibrate, vibration_pattern, flash):
        return "Only POST-Requests!"

    def post(self, token, text, title, vibrate, vibration_pattern, flash):
        try:
            with open(f"groups/{token}/code.txt", "r") as f:
                code = f.read()
            all_clients = os.listdir(f"group-codes/{code}/users")
            print(all_clients)
            for client in all_clients:
                print(client)
                with open(f"token/{client}/title", "w") as f:
                    f.write(title)
                with open(f"token/{client}/text", "w") as f:
                    f.write(text)
                with open(f"token/{client}/info", "w") as f:
                    f.write(f"VIBRATE={vibrate}\nPATTERN={vibration_pattern}\nFLASH={flash}")

            return "written"
        except Exception as e:
            print(e)

api.add_resource(read_info, "/readinfo/<string:token>")
api.add_resource(gettoken, "/gettoken")
api.add_resource(ReadTitle, "/readtitle/<string:token>")
api.add_resource(ReadText, "/readtext/<string:token>")
api.add_resource(WriteText, "/write/<string:token>/<string:text>/<string:title>/<string:vibrate>/<string:vibration_pattern>/<string:flash>")
api.add_resource(GroupWrite, "/write_to_group/<string:token>/<string:text>/<string:title>/<string:vibrate>/<string:vibration_pattern>/<string:flash>")

if __name__ == "__main__":
    app.run("0.0.0.0")