from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book


class APITEst(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter",
            subtitle="The Sorcerer's Stone",
            author="J.K. Rowling",
            isbn="0-7475-3269-9",
        )

    def test_api_listview(self):

        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
