from rest_framework.viewsets import ModelViewSet
from item.models import Item
from item.serializers import ItemSerializer


class ItemModelViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
