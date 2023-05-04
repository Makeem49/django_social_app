from django.test import TestCase
from django.contrib.auth import get_user_model
from blogs.models import Post


# Create your tests here.
class TestBlogPost(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="bob", email="pop@gmail.com", password="password"
        )
        cls.post = Post.objects.create(
            title="Banking X", body="The best banking system", author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.user.username, "bob")
        self.assertEqual(self.post.author, self.user)
        
