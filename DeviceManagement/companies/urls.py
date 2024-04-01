from django.urls import path
from .views.companyView import CompanyListCreate, CompanyDetail

urlpatterns = [
    path("companies/", CompanyListCreate.as_view(), name="company-list-create"),
    path(
        "companies/<int:pk>/",
        CompanyDetail.as_view(),
        name="company-detail",
    ),
]
