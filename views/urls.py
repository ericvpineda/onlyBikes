from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Map usls to view functions
# Note: NEED to end routes with forward slash
urlpatterns = [
    path('',                        views.home,            name='home'),
    path('index/',                  views.index,           name='index'),
    path('temp/',                   views.temp,            name='temp'),
    path('show/<int:id>',           views.show,            name='show'),
    path('logout/',                 views.logout,          name='logout'),
    path('profile/',                views.profile,         name='profile'),
    path('profile/update_profile/', views.update_profile,  name='update_profile'),
    path('cam/',                    views.cam,             name='cam'),
    path('detect/',                 views.detect_bike,     name='detect_bike'),
    path('leaderboard/',            views.leaderboard,     name='leaderboard'),
    path('aboutUs/',                views.about,           name= 'about'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)