from django.urls import path
from main.views import show_main, create_park_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_all_entry, delete_last_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-park-entry', create_park_entry, name='create_park_entry'),
    path('delete-all-entry',delete_all_entry,name='delete_all_entry'),
    path('delete-last-entry',delete_last_entry,name='delete_last_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]