from django.urls import path

from .views import TestView, TestTransactionView

urlpatterns = [
    path('view', TestView.as_view(), name='test'),
    path('transaction_view', TestTransactionView.as_view(), name='transaction'),
    path('threading_view', TestTransactionView.as_view(), name='threading'),

]
