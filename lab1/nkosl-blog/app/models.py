from app import db


class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    body = db.Column(db.String())

    def __repr__(self):
        return '<Title {}>'.format(self.title)
