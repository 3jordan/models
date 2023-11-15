from django.db import models
from typing import Optional
from django.db.models.query import QuerySet


class ClientList(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone}, Company: {self.company}"


def add_client(name, phone, company) -> ClientList:
    return ClientList.objects.create(name=name, phone=phone, company=company)


def search_client(name) -> Optional[object]:
    try:
        return ClientList.objects.get(name__iexact=name)
    except ClientList.DoesNotExist:
        return None


def remove_client(name) -> None:
    client = search_client(name)
    if client:
        client.delete()


def update_client(name, new_name, new_phone, new_company) -> None:
    client = search_client(name)
    if client:
        client.name = new_name
        client.phone = new_phone
        client.company = new_company
        client.save()


def view_clients() -> QuerySet:
    return ClientList.objects.all()


def filter_clients(name) -> QuerySet:
    return ClientList.objects.filter(models.Q(name__icontains=name))
