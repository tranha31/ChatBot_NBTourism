from functools import partial
from flask import Flask, request, jsonify
from flask.wrappers import Response
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from blbase import BLBase
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/chat", methods=['POST'])
@cross_origin()
def chatBot():
    r = request
    r = r.json
    type = r['type']
    value = r['value']
    bl = BLBase()
    result = bl.filter(type, value)
    result = json.dumps(result, ensure_ascii=False)

    return Response(response=result, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)