from django.test import TestCase

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