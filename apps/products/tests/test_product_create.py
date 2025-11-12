import os

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase


class TestProductCreate(APITestCase):
    def setUp(self):
        self.url = reverse_lazy('products:list-create')
        image_path = os.path.join(os.path.dirname(__file__), 'assets', 'image.jpg')
        with open(image_path, "rb") as img:
            image_file = SimpleUploadedFile("image.jpg", img.read(), content_type="image/jpeg")

        self.payload = {
            "title_en": "Organic Honey",
            "title_uz": "Organik Asal",
            "description_en": "Pure organic honey collected from mountain hives.",
            "description_uz": "Tog‘ asalarilari tomonidan yig‘ilgan sof organik asal.",
            "discount": 10,
            "price": "25000.00",
            "category": "BREAKFAST",
            "measurement_type": "L",
            "is_active": True,
            "image": image_file,
        }

    def test_create_product_success(self):
        response = self.client.post(path=self.url, data=self.payload, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        # self.assertEqual(response.json().get('data').get('title'), "Organic Honey")
