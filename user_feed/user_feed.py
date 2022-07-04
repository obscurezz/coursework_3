from flask import Blueprint, render_template

from posts_dao import PostsDAO

POSTS = PostsDAO()

user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder='../templates')


@user_feed_blueprint.route('/users/<username>')
def users(username: str):
    user_posts = POSTS.get_posts_by_user(username)

    return render_template('user-feed.html', posts=user_posts)
