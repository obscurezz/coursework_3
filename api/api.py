from flask import Blueprint, jsonify

from logging_config import get_logger
from posts_dao import PostsDAO

POSTS = PostsDAO()
logger = get_logger(__name__, 'logs/api.log')

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts', methods=['GET'])
def get_json_posts():
    logger.info('Request to /api/posts')
    posts = POSTS.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_json_post_by_id(post_id: int):
    logger.info(f'Request to /api/posts/{post_id}')
    post = POSTS.get_post_by_pk(post_id)
    return jsonify(post)