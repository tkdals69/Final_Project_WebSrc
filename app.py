
# 엔트리포인트

from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config['SECRET_KEY']

    # Jinja2 마크다운 필터 등록
    from markupsafe import Markup
    import markdown

    @app.template_filter('markdown')
    def markdown_filter(text):
        if not text:
            return ''
        return Markup(markdown.markdown(text))

    # 블루프린트 등록
    from routes.main import bp as main_bp
    from routes.recommend import bp as recommend_bp
    from routes.curriculum import bp as curriculum_bp
    from routes.edit import bp as edit_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(curriculum_bp)
    app.register_blueprint(edit_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
