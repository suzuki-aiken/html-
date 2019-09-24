"""
課題
/omikuji　にリクエストを送ると
大吉　吉　凶　のいずれかの結果を変える　ViewFunctionを実装する
"""

import random

from flask import Flask

app = Flask(__name__)


@app.route('/omi')
def omikuji():
    mylist = ['大吉', '吉', '凶']

    result = random.choice(mylist)

    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
