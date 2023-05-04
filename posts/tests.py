# from django.test import TestCase
# from django.urls import reverse
# from .models import Post


# # Create your tests here.
# class PostTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.post = Post.objects.create(text="hello wolrd")

#     def test_model_content(self):
#         self.assertEqual(self.post.text, "hello wolrd")

#     def test_url_exists_at_correct_location(self):
#         res = self.client.get("/")
#         self.assertEqual(res.status_code, 200)

#     def test_url_available_by_name(self):
#         url = reverse("home")
#         res = self.client.get(url)
#         self.assertEqual(res.status_code, 200)

#     def test_template_use(self):
#         res = self.client.get(reverse("home"))
#         self.assertTemplateUsed(res, "home.html")

#     def test_contains_content(self):
#         res = self.client.get("/")
#         self.assertContains(res, "hello")
