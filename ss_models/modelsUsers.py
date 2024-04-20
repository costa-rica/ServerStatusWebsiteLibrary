print("- in modelsUsers")
from .base import Base, DatabaseSession
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table
from itsdangerous.url_safe import URLSafeTimedSerializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]



class Users(Base_users, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    permission = Column(Text)
    posts = relationship('BlogPosts', backref='author', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def get_reset_token(self):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):

        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:

            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        db_session = DatabaseSession()
        try:
            user = db_session.query(Users).get(user_id)
        finally:
            db_session.close()  # Ensure the session is closed after use

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, permission: {self.permission})'


class BlogPosts(Base_users):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_dir_name = Column(Text)
    word_doc_to_html_filename = Column(Text)
    images_dir_name = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)


    def __repr__(self):
        return f'BlogPosts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'
# if 'users' in inspect(engine).get_table_names():
#     print("db already exists")
# else:

#     Base.metadata.create_all(engine)
#     print("NEW db created.")