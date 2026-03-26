from django.urls import path
from .views import CreateAccountView, ListAccountView, AccountDetailView

urlpatterns = [
    path('', ListAccountView.as_view(), name = 'account-list'),
    path('create/', CreateAccountView.as_view(), name = 'account-create'),
    path('<int:pk>/', AccountDetailView.as_view(), name = 'account-detail'),
]
