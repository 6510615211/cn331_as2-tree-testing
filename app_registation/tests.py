from django.test import TestCase
from django.urls import reverse
from .models import Student

class ViewsTestCase(TestCase):
    def setUp(self):
        self.student_data = {
            'student_id': 'S001',
            'name': 'John Doe',
        }

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # เช็คสถานะ HTTP
        self.assertTemplateUsed(response, 'app_registation/home.html')  # เช็คว่าใช้เทมเพลตที่ถูกต้อง

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_registation/about.html')

    def test_enroll_check_view(self):
        response = self.client.get(reverse('enroll_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_registation/enroll_check.html')

    '''def test_regist_view_get(self):
        response = self.client.get(reverse('regist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_registation/regist.html')  # ตรวจสอบว่าใช้เทมเพลตที่ถูกต้อง

    def test_regist_view_post(self):
        response = self.client.post(reverse('regist'), data=self.student_data)
        self.assertEqual(response.status_code, 302)  # เช็คสถานะ HTTP หลังจากโพสต์
        self.assertRedirects(response, reverse('home'))  # ตรวจสอบว่าเปลี่ยนไปหน้าโฮม
        self.assertTrue(Student.objects.filter(student_id='S001').exists())  # ตรวจสอบว่าสร้างนักเรียนสำเร็จ
'''
