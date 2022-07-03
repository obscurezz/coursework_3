from flask import Blueprint, jsonify

from utils import DataLoader

POSTS = DataLoader('data/data.json')

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_json_posts():
    posts = POSTS.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_json_post_by_id(post_id: int):
    post = POSTS.get_post_by_pk(post_id)
    return jsonify(post)