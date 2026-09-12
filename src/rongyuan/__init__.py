from .Support import create_app
import sys
def main() -> None:
    if len(sys.argv) > 1:
        url_file = sys.argv[1]
        app = create_app(url_file)
    else:
        app = create_app()
    app.run()