from django.urls import path

from api.views.test_metrics import KuderView

urlpatterns = [
    path('<str:user_id>/kuder', KuderView.as_view()),
]