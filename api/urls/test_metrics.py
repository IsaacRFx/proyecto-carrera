from django.urls import path

from api.views.test_metrics import AllTestView, KuderView, LearningTypeView

urlpatterns = [
    path('<str:user_id>/kuder', KuderView.as_view()),
    path('<str:user_id>/learning', LearningTypeView.as_view()),
    path('<str:user_id>/all', AllTestView.as_view()),
]