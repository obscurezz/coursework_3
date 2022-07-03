from flask import Blueprint, render_template, request

from utils import DataLoader

POSTS = DataLoader('data/data.json')
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='../templates')
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='../templates')


@main_blueprint.route('/', methods=['GET'])
def main():
    """
    :return: index.html
    """
    posts = POSTS.get_posts_all()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/posts/<int:post_id>', methods=['GET', 'POST'])
def posts(post_id: int):
    """
    :param post_id: pk of post
    :return: exact post at post.html and its comments
    """
    post = POSTS.get_post_by_pk(post_id)
    comments = POSTS.get_comments_by_post_id(post_id)
    comments_counter = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_counter=comments_counter)
