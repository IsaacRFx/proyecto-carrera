from django.urls import path

from api.views.sign_up import SignUpAdminView, SignUpView

urlpatterns = [
    path('', SignUpView.as_view()),
    path('admin/', SignUpAdminView.as_view()),
]