from django.test import TestCase
from app1.models import Post
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('db test')
        # Set up data for the whole TestCase
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username='testuser2', password='12345')
        cls.new = Post.objects.create(
            new="django", content="New content", slug="django")
        cls.new.likes.set([testuser.pk, testuser2.pk])

    def test_model_str1(self):
        self.assertEqual(str(self.new), "django")

    def test_post_has_an_author(self):
        self.assertEqual(self.new.likes.count(), 2)

    def test_get_absolute_url(self):
        self.new.slug = Post.objects.get(id=1)
        self.assertEqual("/django/", self.new.slug.get_absolute_url())


class TestNew(TestCase):

    def setUp(self):
        self.post = baker.make('app1.Post')
        pprint(self.post.__dict__)

    def test_model_str(self):
        title = Post.objects.create(title="Django Testing")
        content = Post.objects.create(content="This is some content")
        self.assertEqual(str(title), "Django Testing")
