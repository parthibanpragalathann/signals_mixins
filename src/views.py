from django.shortcuts import render
from rest_framework import generics, mixins
# Create your views here.
from .serializer import *
from .models import *

class TaskView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class TaskModifyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskDateView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = TaskDateSerializer
    queryset = TaskDate.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

class TaskDateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskDateSerializer
    queryset = TaskDate.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class HistoryView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

class HistoryDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class HistoryDateView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = HistoryDateSerializer
    queryset = HistoryDate.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

class HistoryDateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = HistoryDateSerializer
    queryset = HistoryDate.objects.all()
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
