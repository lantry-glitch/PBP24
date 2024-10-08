from django.urls import path
from main.views import show_main, create_park_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_all_entry, delete_last_entry, register, login_user, logout_user, edit_park, delete_park, add_park_entry_ajax
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-park-entry', create_park_entry, name='create_park_entry'),
    path('delete-all-entry',delete_all_entry,name='delete_all_entry'),
    path('delete-last-entry',delete_last_entry,name='delete_last_entry'),
    path('edit-park/<uuid:id>', edit_park, name='edit_park'),
    path('delete/<uuid:id>', delete_park, name='delete_park'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-park-entry-ajax', add_park_entry_ajax, name='add_park_entry_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)