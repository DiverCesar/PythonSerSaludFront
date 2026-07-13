import os
from flask import Blueprint, render_template

frontend_bp = Blueprint("frontend", __name__, template_folder="templates")

@frontend_bp.route("/")
@frontend_bp.route("/home")
@frontend_bp.route("/patients")
@frontend_bp.route("/patient/create")
@frontend_bp.route("/doctors")
@frontend_bp.route("/doctor/create")
@frontend_bp.route("/appointments")
@frontend_bp.route("/appointment/create")
def index():
    api_base = os.environ.get("API_BASE", "")
    return render_template("dashboard.html", api_base=api_base)
