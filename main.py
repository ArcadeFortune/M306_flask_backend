from flask import Flask
from flask_cors import CORS

from functions import *

app = Flask(__name__)
CORS(app)


@app.route("/xml")
def xml():
    print('recieved API call')
    big_list = load_xml()
    # print(big_list)
    print('sending data')
    return big_list
    #


@app.route("/esl")
def esl():
    print('recieved API call')
    big_list = load_esl()
    # print(big_list)
    print('sending data')
    return big_list
    #

if __name__ == '__main__':
    app.run(debug=True, port=3001)
