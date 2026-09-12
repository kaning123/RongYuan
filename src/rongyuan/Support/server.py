import flask
from . import url

def create_app(url_file = url.merge(url.MY_DIR, 'URL')):
    app = flask.Flask(__name__)

    urls = url.get_urls(url_file)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    @app.route('/sample/', defaults={'subpath': ''})
    @app.route('/sample/<path:subpath>')
    def sample(subpath):
        query = flask.request.query_string.decode()

        for base in urls:
            parts = [base.rstrip('/')]
            if subpath:
                parts.append(subpath.lstrip('/'))
            full_url = '/'.join(parts)
            if query:
                full_url += '?' + query

            print('checking:', full_url)
            if url.check_url_exists(full_url):
                return flask.redirect(full_url)

        return 'No valid URL found.', 404
    return app