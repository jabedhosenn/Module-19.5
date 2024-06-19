from django.urls import path

from . import views

urlpatterns = [
    # path('musicians/', views.allMusicians, name='musicians'),
    # path('add_musician/', views.addMusician, name='add_musician'),
    # path('update_musician/<int:id>/', views.updateMusician, name='update_musician'),
    # path('delete_musician/<int:id>/', views.deleteMusician, name='delete_musician'),
    # path('details_musician/<int:id>/', views.detailsMusician, name='details_musician'),

    path('musicians/', views.AllMusicianView.as_view(), name='musicians'),
    path('add_musician/', views.MusicianCreateView.as_view(), name='add_musician'),
    path('update_musician/<int:pk>/', views.UpdateMusicianView.as_view(), name='update_musician'),
    path('delete_musician/<int:pk>/', views.DeleteMusicianView.as_view(), name='delete_musician'),
    path('details_musician/<int:pk>/', views.DetailMusicianView.as_view(), name='details_musician'),
]

