from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, LogoutView, RegisterView, HomeView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)