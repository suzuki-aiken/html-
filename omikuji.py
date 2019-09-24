"""
課題
/omikuji　にリクエストを送ると
大吉　吉　凶　のいずれかの結果を変える　ViewFunctionを実装する
"""

import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/omi')
def omikuji():
    mylist = ['大吉', '吉', '凶']

    result = random.choice(mylist)

    # if 文で場合分け
    #  return f'{result}'

    return render_template('omikuji.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)  # app.run(debug=True port=7777)でurl変更可能
