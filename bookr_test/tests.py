from django.test import TestCase , Client

# Create your tests here.

from .models import Publisher

class TestPublisherModel(TestCase):
    """ Test the publisher model. """ 
    def setUp(self):
        self.p = Publisher(name="Packt",website="www.packt.com",\
              email="contact@packt.com")
        
    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)
        
    def test_str_representation(self):
        self.assertEqual(str(self.p), "Packt")
        
class TestGretingView(TestCase):
    """ Test the greeting view."""
    def setUp(self):
        self.client = Client()
        
    def testing_greeting_view(self):
        response = self.client.get('/test/greeting')
        self.assertEquals(response.status_code, 200)
        