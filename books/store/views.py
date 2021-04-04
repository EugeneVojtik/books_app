from django.db.models import Count, Case, When, Avg, Max, Min
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from store.models import Book, UserBookRelations
from store.permissions import IsOwnerOrStuffOrReadOnly
from store.serializers import BookSerializer, UserBookRelationsSerializer


class MainPage(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["price"]


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all().annotate(
        annotated_likes=Count(Case(When(users_book__like=True, then=1))),
        ).select_related('critic').prefetch_related('readers').order_by('id')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStuffOrReadOnly]
    filter_fields = ["price"]
    search_fields = ['title', 'authors']
    ordering_fields = ["price", 'authors']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserBookRelationsSerializer
    queryset = UserBookRelations.objects.all()
    lookup_field = 'book'


    def get_object(self):
        obj, created = UserBookRelations.objects.get_or_create(user=self.request.user, book_id=self.kwargs['book'])
        print("created", created)
        return obj


def auth(request):
    return render(request, 'oauth.html')
