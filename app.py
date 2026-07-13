import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend/static", static_url_path="/static")
CORS(app)

from frontend.routes import frontend_bp

app.register_blueprint(frontend_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
