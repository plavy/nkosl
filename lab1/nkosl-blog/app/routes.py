from flask import render_template, flash, redirect, url_for
from app import nkosl_app, db
from app.forms import SubmitForm
from app.models import Posts


@nkosl_app.route('/')
@nkosl_app.route('/index/')
def index():
    # posts = [
    #     {
    #         "title": "Veridian III",
    #         "body": "Classified as M-class, Veridian III was the uninhabited third planet of the Veridian system. The planet had three moons. Its surface contains rocky mountainous regions as well as lush vegetative areas. There were also several large bodies of water. Its ionosphere created enough interference that it was hard to penetrate by sensors. In 2371, the position and orbital path of Veridian III was illustrated in a system map displayed in stellar cartography aboard the USS Enterprise-D."
    #     },
    #     {
    #         "title": "William T. Riker",
    #         "body": "William Thomas \"Will\" Riker was a noted Starfleet officer, perhaps best known for his long assignment as first officer under Captain Jean-Luc Picard aboard the USS Enterprise-D and later the USS Enterprise-E. In 2379 he finally accepted a promotion as captain of the USS Titan."
    #     },
    # ]
    posts = Posts.query.all()
    return render_template("index.html", title="NKOSL index", posts=posts)


@nkosl_app.route('/submit/', methods=['GET', 'POST'])
def submit():
    form = SubmitForm()
    if form.validate_on_submit():
        flash("Submitting a post: {}".format(form.title.data))
        post = Posts(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('submit.html', title="NKOSL submit", form=form)
