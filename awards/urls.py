from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectCreateView
urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^directory/',views.directory, name='directory'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^site/(\d+)',views.site,name='site'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),

    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^project/new/',ProjectCreateView.as_view(),name='newProject'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
