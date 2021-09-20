from .views import *
from django.urls import path

#api application urls ...
urlpatterns = [
    path('task/', TaskView.as_view(), name="Tasks View"),                 #all the Task details using GET and POST
    path('task/<int:id>/', TaskModifyView.as_view(), name="Tasks Modify View"), #all the Task details using PUT and DELETE
    path('task/date/', TaskDateView.as_view(), name="Tasks Date View"),  # all the Task Date details using GET
    path('task/date/<int:id>/', TaskDateDeleteView.as_view(), name="Tasks Date Delete View"),
    # all the Task details using DELETE
    path('history/', HistoryView.as_view(), name="History View"),  # all the History details using GET
    path('history/<int:id>/', HistoryDeleteView.as_view(), name="History Delete View"),
    # all the History using DELETE
    path('history/date/', HistoryDateView.as_view(), name="History Date View"),  # all the History Date details using GET
    path('history/date/<int:id>/', HistoryDateDeleteView.as_view(), name="History Date Delete View"),
    # all the History Date using DELETE

]