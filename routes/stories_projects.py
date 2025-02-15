from flask import Blueprint, render_template

stories_projects_bp = Blueprint('stories_projects', __name__)

@stories_projects_bp.route('/stories_projects')
def stories_projects():
    return render_template('stories_projects.html')