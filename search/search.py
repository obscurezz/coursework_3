from flask import Blueprint, render_template, request

from utils import DataLoader

POSTS = DataLoader('data/data.json')

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='../templates')


@search_blueprint.route('/search')
def search_form():
    """
    :return: search.html
    """
    return render_template('search.html')


@search_blueprint.route('/search_results', methods=['GET', 'POST'])
def search_result():
    """
    :return: search results at search.html, max is 10 posts
    """
    search_query: str | None = request.args.get('query', '')
    # full results
    result_of_search_full: list[dict] = [obj for obj in POSTS.get_posts_all() if
                                         search_query.lower() in obj['content'].lower()]
    count_of_results = len(result_of_search_full)
    # results from 1 to 10
    result_of_search = result_of_search_full if count_of_results <= 10 else result_of_search_full[:10]

    return render_template('search.html', query=search_query, posts=result_of_search, count=count_of_results)
