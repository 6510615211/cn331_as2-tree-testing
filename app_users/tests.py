# from django.test import TestCase
# from .models import User

# class UserModelTest(TestCase):
#     def setUp(self):
#         # สร้างผู้ใช้สำหรับการทดสอบ
#         self.user = User.objects.create(
#             username='testuser',
#             password='testpass',  # ควรใช้วิธีเข้ารหัสรหัสผ่านในการใช้งานจริง
#             email='test@example.com'
#         )

#     def test_user_creation(self):
#         # ตรวจสอบว่าผู้ใช้ถูกสร้างขึ้นอย่างถูกต้อง
#         self.assertEqual(self.user.username, 'testuser')
#         self.assertEqual(self.user.email, 'test@example.com')

#     def test_user_password_hashing(self):
#         # ตรวจสอบว่ารหัสผ่านถูกเข้ารหัส
#         self.assertNotEqual(self.user.password, 'testpass')  # รหัสผ่านต้องไม่เท่ากับรหัสผ่านปกติ

#     def test_unique_username(self):
#         # ตรวจสอบว่าการสร้างชื่อผู้ใช้ซ้ำทำให้เกิดข้อผิดพลาด
#         with self.assertRaises(Exception):  # คาดว่าจะเกิดข้อผิดพลาดเมื่อพยายามสร้างชื่อผู้ใช้ซ้ำ
#             User.objects.create(
#                 username='testuser',  # ชื่อผู้ใช้ที่ซ้ำ
#                 password='anotherpass',
#                 email='another@example.com'
#             )

#     def test_str_method(self):
#         # ทดสอบว่าฟังก์ชัน __str__ คืนค่าถูกต้อง
#         self.assertEqual(str(self.user), 'testuser')

#     def test_user_email_uniqueness(self):
#         # ตรวจสอบว่าอีเมลไม่ซ้ำ
#         User.objects.create(
#             username='anotheruser',
#             password='testpass',
#             email='unique@example.com'
#         )
#         with self.assertRaises(Exception):
#             User.objects.create(
#                 username='yetanotheruser',
#                 password='testpass',
#                 email='unique@example.com'  # อีเมลซ้ำ
#             )

from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        # สร้างผู้ใช้สำหรับการทดสอบ
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'  # รหัสผ่านที่ไม่เข้ารหัส
        )

    def test_user_creation(self):
        # ตรวจสอบว่าผู้ใช้ถูกสร้างขึ้นอย่างถูกต้อง
        self.assertEqual(self.user.username, 'testuser')

    def test_user_password_hashing(self):
        # ตรวจสอบว่ารหัสผ่านถูกเข้ารหัส
        self.assertNotEqual(self.user.password, 'testpass')  # รหัสผ่านต้องไม่เท่ากับรหัสผ่านปกติ

    def test_unique_username(self):
        # ตรวจสอบว่าการสร้างชื่อผู้ใช้ซ้ำทำให้เกิดข้อผิดพลาด
        with self.assertRaises(Exception):  # คาดว่าจะเกิดข้อผิดพลาดเมื่อพยายามสร้างชื่อผู้ใช้ซ้ำ
            User.objects.create_user(
                username='testuser',  # ชื่อผู้ใช้ที่ซ้ำ
                password='anotherpass'
            )

    def test_str_method(self):
        # ทดสอบว่าฟังก์ชัน __str__ คืนค่าถูกต้อง
        self.assertEqual(str(self.user), 'testuser')
