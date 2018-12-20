# from flask import Flask, jsonify
#
from latest_episodes import get_anime_list
#
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return jsonify(Data=get_anime_list())
#
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3000, debug=True)
#

get_anime_list()