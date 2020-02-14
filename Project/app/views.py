from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
import logging, time

from app.models import Book, Author
from app.serializers import BookSerializer, AuthorSerializer

logger = logging.getLogger(__name__)


class BookView(ModelViewSet):
    authentication_classes = ()
    permission_classes = ()

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (DjangoFilterBackend,filters.OrderingFilter)

    filter_fields = ['ctype']

    ordering_fields = ('title', 'created', 'updated')