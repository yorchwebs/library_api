from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter",
            subtitle="The Sorcerer's Stone",
            author="J.K. Rowling",
            isbn="0-7475-3269-9",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Harry Potter")
        self.assertEqual(self.book.subtitle, "The Sorcerer's Stone")
        self.assertEqual(self.book.author, "J.K. Rowling")
        self.assertEqual(self.book.isbn, "0-7475-3269-9")

    def test_book_list_view(self):
        response = self.client.get(reverse("-home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")
