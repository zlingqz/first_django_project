from django.conf.urls import *
from . import views
from django.urls import path

urlpatterns = [path('', views.archive),
               path('create/', views.create_blogpost),]

# urlpatterns = [
#     path(r'blog/', include('blog.urls')),
#     path('admin/', admin.site.urls),
# ]