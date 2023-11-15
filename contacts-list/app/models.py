from django.db import models
from django.db.models import QuerySet


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


def create_contact(name, email, phone, is_favorite) -> Contacts:
    return Contacts.objects.create(
        name=name, email=email, phone=phone, is_favorite=is_favorite
    )


def all_contacts() -> QuerySet:
    return Contacts.objects.all()


def find_contact_by_name(name) -> object:
    try:
        return Contacts.objects.get(name__iexact=name)
    except Contacts.DoesNotExist:
        return None


def favorite_contacts() -> QuerySet:
    return Contacts.objects.filter(is_favorite=True)


def update_contact_email(name, new_email) -> None:
    contact = find_contact_by_name(name)
    if contact:
        contact.email = new_email
        contact.save()


def delete_contact(name) -> None:
    contact = find_contact_by_name(name)
    if contact:
        contact.delete()
