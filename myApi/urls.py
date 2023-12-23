
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import UserOutputViewSet

router = DefaultRouter()
router.register(r'useroutputs', UserOutputViewSet, basename='useroutput')
router.register(r'agentControl', AllPAgesByAgentControlViewSet, basename='AllPAgesByAgentControlViewSet')



urlpatterns = [
     path('viewset/', include(router.urls)),
    path("register/", UserList.as_view(), name = "register"),
    path('login/', AuthUserLoginView.as_view(), name = "login"),
    path('user-forms/', UserFormListCreateView.as_view(), name='userform-list'),
    path('user-forms/<int:pk>/', UserFormDetailView.as_view(), name='userform-detail'),
    path('userdocuments/', UserFormDocumentCreateView.as_view(), name='userdocument-list'),
    path('userdocuments/<int:pk>/', UserFormDocumentDetailView.as_view(), name='userdocument-detail'),
     path('all-pages-api/', AllPagesApiListCreateView.as_view(), name='all-pages-api-list-create'),


     path('documents/', DocumentListCreateView.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
]