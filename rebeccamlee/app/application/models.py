from application import db
from datetime import datetime

class GithubToken(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    github_access_token = db.Column(db.String(200))

    def __init__(self, github_access_token):
        self.github_access_token = github_access_token

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index=True, unique=True)
    is_admin = db.Column(db.Boolean, default=True)
    profile_image = db.Column(db.String(250), index=True, unique=False)
    display_name = db.Column(db.String(250), index=True, unique=True)
    email = db.Column(db.String(250), index=True, unique=True)
    authenticated = db.Column(db.Boolean, default=False)
    custom_blog_title = db.Column(db.String(1224), nullable=True)
    custom_blog_path = db.Column(db.String(512), default="")
    custom_blog_description = db.Column(db.Text(), default="")
    approved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_approved(self):
        """Return True if the user is authenticated."""
        return self.approved

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class StaticPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    public = db.Column(db.String(128), default="True")
    title = db.Column(db.String(500), nullable=False)
    route = db.Column(db.String(512), nullable=False)
    page_data = db.Column(db.Text(), nullable=False)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'))
    public = db.Column(db.String(128), default="True")
    title = db.Column(db.String(500), nullable=False)
    post_path = db.Column(db.String(512), default="")
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    teaser = db.Column(db.String(512))
    body = db.Column(db.Text(), nullable=False)
    tags = db.relationship('Tag', secondary="tags_posts", backref=db.backref('tags', 
        lazy='dynamic'))
    def __repr__(self):
        return '<Blog Post %r >' % self.title

class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    tag_name = db.Column(db.String(500), nullable=False)
    tag_path = db.Column(db.String(500), default="")
    public = db.Column(db.String(128), default="True")

    def __repr__(self):
        return '<Tag %r >' % self.tag_name

class TagsPosts(db.Model):
    __tablename__="tags_posts"
    id = db.Column(db.Integer(), primary_key=True)
    tag_id = db.Column(db.Integer(), db.ForeignKey('tag.id', ondelete='CASCADE'))
    blog_post_id = db.Column(db.Integer(), db.ForeignKey('blog_post.id', ondelete='CASCADE'))