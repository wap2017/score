from flask import Flask
from flask import request
from flask import render_template
from functools import reduce

app = Flask(__name__)


def str2float(s):
    if s == "":
        return 0

    if "." not in s:
        return int(s)

    def str2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def fnMuti(x, y):
        return x * 10 + y

    def fnDivid(x, y):
        return x / 10 + y

    dotIndex = s.index('.')
    return reduce(fnMuti, map(str2num, s[:dotIndex])) + reduce(fnDivid, list(map(str2num, s[dotIndex + 1:]))[::-1]) / 10


@app.route('/score_form')
def form():
    return render_template('form.html')


def get_gpa(type):
    if type == "优秀":
        return 4.5
    elif type == "良好":
        return 3.5
    elif type == "中等":
        return 2.5
    elif type == "合格":
        return 1.5
    else:
        return 0


@app.route('/score', methods=['POST'])
def score():
    s1 = get_gpa(request.form["score1"])
    s2 = get_gpa(request.form["score2"])
    s3 = get_gpa(request.form["score3"])

    a = str2float(request.form["score4"])
    print(a == 54)

    r1 = (s1 * 2 + s2 * 4 + s3 * 2) / 8
    r2 = (r1 + 5) * 9

    r3 = 0.6 * a
    r4 = r3 / 6 + 1

    return render_template('result.html', score1=request.form["score1"],
                           score2=request.form["score2"],
                           score3=request.form["score3"],
                           score4=request.form["score4"],
                           result1=r1, result2=r2, result3=r3, result4=r4)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")
