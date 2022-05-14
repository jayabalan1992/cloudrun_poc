import os
import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/runtest")
def eventinfo():
    p=subprocess.run(['python', 'test.py'])
    print('returncode', p.returncode)
    return 'Hi! I am testing a code'



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
