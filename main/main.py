from flask import Blueprint, render_template

from posts_dao import PostsDAO
from bookmarks_dao import BookmarksDAO

POSTS = PostsDAO()
BOOKMARKS = BookmarksDAO()
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='../templates')
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='../templates')


@main_blueprint.route('/', methods=['GET'])
def main():
    """
    :return: index.html
    """
    posts = POSTS.get_posts_all()
    bookmarks =BOOKMARKS.get_all_bookmarks()
    bookmarks_count = len(bookmarks)
    return render_template('index.html', posts=posts, bookmarks_count=bookmarks_count)


@posts_blueprint.route('/posts/<int:post_id>', methods=['GET', 'POST'])
def posts(post_id: int):
    """
    :param post_id: pk of post
    :return: exact post at post.html and its comments
    """
    post = POSTS.get_post_by_pk(post_id)
    # getting comments
    comments = POSTS.get_comments_by_post_id(post_id)
    comments_counter = len(comments)
    # getting tag identification
    temporary_list = post['content'].split(' ')
    for index, word in enumerate(temporary_list):
        if word[0] == '#':
            new_word = f'<a href="/tag/{word[1:]}">#{word[1:]}</a>'
            temporary_list[index] = new_word

    post['content'] = ' '.join(temporary_list)

    return render_template('post.html', post=post, comments=comments, comments_counter=comments_counter)
