from django.test import TestCase
from django.urls import reverse
from .models import Student

class ViewsTestCase(TestCase):
    def setUp(self):
        self.student_data = {
            'student_id': '6510681234',
            'name': 'likestudy makmak',
        }

    def test_home_view(self): #หน้า home view ทำงานถูกต้อง
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # เช็คสถานะ HTTP
        self.assertTemplateUsed(response, 'app_registation/home.html')  # เช็คว่าใช้เทมเพลตที่ถูกต้อง

    def test_about_view(self):#หน้า about view ทำงานถูกต้อง
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_registation/about.html')

    def test_enroll_check_view(self): #หน้า enroll check view ทำงานถูกต้อง
        response = self.client.get(reverse('enroll_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_registation/enroll_check.html')
