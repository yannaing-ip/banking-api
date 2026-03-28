from django.urls import path
from .views import TransferView, TransactionListView
from .views import TransferView, TransactionListView, TransactionDetailView

urlpatterns = [
    path('transfer/', TransferView.as_view(), name = 'transfer'),
    path('', TransactionListView.as_view(), name = 'transaction-list'),
    path('<int:pk>/', TransactionDetailView.as_view(), name = 'transaction-detail'),
]
