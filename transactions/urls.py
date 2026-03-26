from django.urls import path
from .views import TransferView, TransactionListView

urlpatterns = [
    path('transfer/', TransferView.as_view(), name = 'transfer'),
    path('', TransactionListView.as_view(), name = 'transaction-list'),
]
