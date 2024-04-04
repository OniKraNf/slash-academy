from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),
    path('', include('courses.urls')),
    path('', include('slash_academy.urls')),
    path("cart/", include('cart.urls')),
    path("profile/", include('user_profile.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('webinars/', include('webinars.urls'))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)