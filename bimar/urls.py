from django.urls import path
from bimar.views import (
    NobatDetail,
    EditNobat,
    CreatKhedmat,
    Payment,
)

urlpatterns = [
    path("Nobatdetail", NobatDetail.as_view()),
    path('Editnobat/<int:pk>', EditNobat.as_view()),
    path('CreateKhedmat', CreatKhedmat.as_view()),
    path('Payment', Payment.as_view()),



]