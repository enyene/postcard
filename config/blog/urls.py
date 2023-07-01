from django.urls import path
from .views import post_index,PostDetail,draft,DraftDetail,publish,detail

app_name = "blog"

urlpatterns = [
    path('',post_index,name='home'),
    # path('draft/',draft,name='draft'),
    # path('<slug:slug>/',detail,name='detail'),
    
    # path('<slug:slug>/<int:id>/',DraftDetail.as_view(),name='items'),
    # path('publish/<slug:slug>/<int:pk>/',publish,name='publish')
]