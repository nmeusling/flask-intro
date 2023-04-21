from flask import (
    Blueprint, g, render_template
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('profile',__name__)

def get_posts_by_author(author_id):
    db = get_db()
    posts = db.execute(
        'SELECT p.id , title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.author_id = ?',
        (author_id,)
    ).fetchall()
    # TODO what if there are no posts; or lots of posts?
    return posts

@bp.route('/profile', methods=('GET',))
@login_required
def view():
    posts = get_posts_by_author(g.user['id'])
    return render_template("profile/view.html", posts=posts)