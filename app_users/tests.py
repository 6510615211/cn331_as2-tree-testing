from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_user_create(self):# ตรวจสอบว่าผู้ใช้ถูกสร้างขึ้นถูก
        self.assertEqual(self.user.username, 'testuser')

    def test_user_password(self):# ตรวจสอบว่ารหัสผ่านถูกเข้ารหัส
        self.assertNotEqual(self.user.password, 'testpassword')

    def test_unique_username(self):# ตรวจสอบว่าการสร้างชื่อผู้ใช้ซ้ำทำให้เกิดข้อผิดพลาด
        with self.assertRaises(Exception):  # คาดว่าจะเกิดข้อผิดพลาดเมื่อพยายามสร้างชื่อผู้ใช้ซ้ำ
            User.objects.create_user(
                username='testuser',  # ชื่อผู้ใช้ที่ซ้ำ
                password='testpassword2'
            )

    def test_str_method(self):# ทดสอบว่าฟังก์ชั่นคืนค่าถูกต้อง
        self.assertEqual(str(self.user), 'testuser')
