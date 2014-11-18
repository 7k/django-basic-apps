from django_comments.models import Comment
from django_comments.forms import CommentForm


def get_model():
    return Comment


def get_form():
    return CommentForm