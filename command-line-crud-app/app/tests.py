from django.test import TestCase
from app import models


class TestClient(TestCase):
    def test_can_add_client(self):
        client = models.add_client(
            "John Doe",
            "555-1234",
            "ABC Inc.",
        )

        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, "John Doe")
        self.assertEqual(client.company, "ABC Inc.")

    def test_can_view_all_clients(self):
        client_data = [
            {
                "name": "Alice Johnson",
                "phone": "555-1234",
                "company": "Tech Solutions Inc.",
            },
            {
                "name": "Bob Smith",
                "phone": "555-5678",
                "company": "Web Innovations",
            },
            {
                "name": "Charlie Davis",
                "phone": "555-9876",
                "company": "Data Enterprises",
            },
        ]

        for client in client_data:
            models.add_client(
                client["name"],
                client["phone"],
                client["company"],
            )
        clients = models.view_clients()

        self.assertEqual(len(clients), len(client_data))

        client_data = sorted(client_data, key=lambda c: c["name"])
        clients = sorted(clients, key=lambda c: c.name)

        for data, client in zip(client_data, clients):
            self.assertEqual(data["name"], client.name)
            self.assertEqual(data["phone"], client.phone)
            self.assertEqual(data["company"], client.company)

    def test_can_search_client(self):
        client_data = [
            {
                "name": "Alice Johnson",
                "phone": "555-1234",
                "company": "Tech Solutions Inc.",
            },
            {
                "name": "Bob Smith",
                "phone": "555-5678",
                "company": "Web Innovations",
            },
            {
                "name": "Charlie Davis",
                "phone": "555-9876",
                "company": "Data Enterprises",
            },
        ]

        for client in client_data:
            models.add_client(
                client["name"],
                client["phone"],
                client["company"],
            )

        self.assertIsNone(models.search_client("adj fjav"))

        client = models.search_client("Alice Johnson")

        self.assertIsNotNone(client)
        self.assertEqual(client.phone, "555-1234")

    def test_can_view_clients(self):
        client_data = [
            {
                "name": "Alice Johnson",
                "phone": "555-1234",
                "company": "Tech Solutions Inc.",
            },
            {
                "name": "Bob Smith",
                "phone": "555-5678",
                "company": "Web Innovations",
            },
            {
                "name": "Charlie Davis",
                "phone": "555-9876",
                "company": "Data Enterprises",
            },
        ]

        for client in client_data:
            models.add_client(client["name"], client["phone"], client["company"])

        self.assertEqual(len(models.filter_clients("Bob Smith")), 1)

    def test_can_update_client(self):
        client_data = [
            {
                "name": "Alice Johnson",
                "phone": "555-1234",
                "company": "Tech Solutions Inc.",
            },
            {
                "name": "Bob Smith",
                "phone": "555-5678",
                "company": "Web Innovations",
            },
            {
                "name": "Charlie Davis",
                "phone": "555-9876",
                "company": "Data Enterprises",
            },
        ]

        for client in client_data:
            models.add_client(
                client["name"],
                client["phone"],
                client["company"],
            )

        models.update_client(
            "Alice Johnson", "Alison Johnson", "123-5555", "Apples Org."
        )

        self.assertEqual(models.search_client("Alison Johnson").name, "Alison Johnson")
        self.assertEqual(models.search_client("Alison Johnson").phone, "123-5555")
        self.assertEqual(models.search_client("Alison Johnson").company, "Apples Org.")

    def test_remove_client(self):
        client_data = [
            {
                "name": "Allison Johnson",
                "phone": "555-1234",
                "company": "Tech Solutions Inc.",
            },
            {
                "name": "Bob Smith",
                "phone": "555-5678",
                "company": "Web Innovations",
            },
            {
                "name": "Charlie Davis",
                "phone": "555-9876",
                "company": "Data Enterprises",
            },
        ]

        for client in client_data:
            models.add_client(
                client["name"],
                client["phone"],
                client["company"],
            )
        models.remove_client("Allison Johnson")

        self.assertEqual(len(models.view_clients()), 2)
