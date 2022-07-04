from flask import Blueprint, render_template

from posts_dao import PostsDAO

POSTS = PostsDAO()

tags_blueprint = Blueprint('tags_blueprint', __name__, template_folder='../templates')


@tags_blueprint.route('/tag')
def all_tags():
    """
    :return: tag.html
    """
    return render_template('tag.html')


@tags_blueprint.route('/tag/<tagname>')
def get_tags(tagname: str):
    """
    :param tagname: tag name that should be found
    :return: page with posts by tag name
    """
    posts = POSTS.get_posts_all()
    posts_by_tag = [post for post in posts if f'#{tagname}' in post['content']]

    return render_template('tag.html', tag=tagname, posts=posts_by_tag)
