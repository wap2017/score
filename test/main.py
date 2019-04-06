from flask import Flask
from flask import jsonify
from flask import Response

app = Flask(__name__)


@app.route('/hello/<name>/<words>', methods=['GET'])
def hello(name, words):
    x = [{"name":"zhangsan","age":4},{"name":"lisi","age":3}]
    x=str(x)
    return jsonify({'name': x})  # 也可以传入key=value形式的参数，如jsonify(name=name,words=words)

if __name__ == '__main__':
    app.run()
