from django.test import SimpleTestCase

# Create your tests here.
class TestNearView(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/near-hundred/93/")
        self.assertContains(response, "True")

    def test_near_hundred_90(self):
        response = self.client.get("/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundred_89(self):
        response = self.client.get("/near-hundred/89/")
        self.assertContains(response, "False")

class TestStringView(SimpleTestCase):
    def test_string_splosion_Code(self):
        response = self.client.get("/String-Splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_string_splosion_abc(self):
        response = self.client.get("/String-Splosion/abc/")
        self.assertContains(response, "aababc")

    def test_string_splosion_ab(self):
        response = self.client.get("/String-Splosion/ab/")
        self.assertContains(response, "aab")

class TestCatDogView(SimpleTestCase):
    def test_cat_dog_catdog(self):
        response = self.client.get("/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_cat_dog_catcat(self):
        response = self.client.get("/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_cat_dog_cat_1cat1cadodog(self):
        response = self.client.get("/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")

class TestLoneView(SimpleTestCase):
    def test_lone_view_123(self):
        response = self.client.get("/lone-sum/1/2/3/")
        self.assertContains(response, "6")
    def test_lone_view_323(self):
        response = self.client.get("/lone-sum/3/2/3/")
        self.assertContains(response, "2")
    def test_lone_view_333(self):
        response = self.client.get("/lone-sum/3/3/3/")
        self.assertContains(response, "0")