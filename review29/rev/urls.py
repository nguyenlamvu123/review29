from django.urls import path
from .views import get_csrf_token_view, save_review_view, list_reviews, get_review_by_url

urlpatterns = [
    path('', get_csrf_token_view),
    path('save-review/', save_review_view),
    path('reviews/', list_reviews),
    path('review-by-url/', get_review_by_url),
]
