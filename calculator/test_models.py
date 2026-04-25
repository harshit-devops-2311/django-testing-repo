import pytest
from calculator.models import Item

@pytest.mark.django_db
def test_create_item():
  item = Item.objects.create(name="Laptop")
  assert item.name == "Laptop"
