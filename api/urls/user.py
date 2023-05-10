from django.urls import path

from api.views.user import UserDetailsView, UserView

urlpatterns = [
    path('<str:user_id>/', UserView.as_view()),
    path('<str:user_id>/update/', UserDetailsView.as_view())
]