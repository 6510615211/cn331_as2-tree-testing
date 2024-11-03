from django.test import TestCase, Client
from django.urls import reverse
from app_courses.models import Subject, Student
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class SubjectModelTest(TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(
            course_id="CN202",
            course_name="Data algorithms 1",
            course_semester="1/2567",
            course_amount=9999,
            course_status=Subject.CourseStatus.AVAILABLE,
        )

    def test_subject_create(self): #มีวิชาที่สร้างไว้?
        self.assertEqual(self.subject.course_id, "CN202")
        self.assertEqual(self.subject.course_name, "Data algorithms 1")
        self.assertEqual(self.subject.course_semester, "1/2567")
        self.assertEqual(self.subject.course_amount, 9999)
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.AVAILABLE)

    def test_subject_string_representation(self): #ทดสอบว่าการแปลง Subject เป็นข้อความ 
        expected_str = "CN202 Data algorithms 1 1/2567 STATUS: Available"
        self.assertEqual(str(self.subject), expected_str)

    def test_update_course_status_and_amount(self): #ทดสอบว่าเปลี่ยนแปลงค่าได้ตามกำหนด
        self.subject.course_status = Subject.CourseStatus.REGISTERED
        self.subject.course_amount -= 1
        self.subject.save()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
        self.assertEqual(self.subject.course_amount, 9998)

    def test_course_amount_never_negative(self): #ค่า course amount ติดลบไม่ได้
        self.subject.course_amount = 0
        self.subject.save()
        with self.assertRaises(ValidationError):
            self.subject.course_amount -= 1
            self.subject.full_clean()


class StudentModelTest(TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(
            course_id="CN202",
            course_name="Data algorithm 1",
            course_semester="1/2567",
            course_amount=9999,
            course_status=Subject.CourseStatus.AVAILABLE,
        )
        self.student = Student.objects.create(
            student_id="6510681234",
            first_name="likestudy",
            last_name="makmak",
            email="likestudy.mak@dome.tu.ac.th"
        )
        self.student.enrolled_subjects.add(self.subject)

    def test_student_create(self): #ข้อมูลส่วนตัวเหมือนที่ลงทะเบียน?
        self.assertEqual(self.student.student_id, "6510681234")
        self.assertEqual(self.student.first_name, "likestudy")
        self.assertEqual(self.student.last_name, "makmak")
        self.assertEqual(self.student.email, "likestudy.mak@dome.tu.ac.th")

    def test_student_enrollment(self): #ทดสอบว่าลงทะเบียนสำเร็จมีอยู่ในชื่อที่ลงทะเบียน
        self.assertIn(self.subject, self.student.enrolled_subjects.all())
        self.assertIn(self.student, self.subject.students.all())

    def test_remove_student_enrollment(self): #ลบออกจากการลงทะเบียน
        self.student.enrolled_subjects.remove(self.subject)
        self.assertNotIn(self.subject, self.student.enrolled_subjects.all())
        self.assertNotIn(self.student, self.subject.students.all())

    def test_duplicate_id(self): #id ซ้ำเกิด error
        with self.assertRaises(IntegrityError):
            Student.objects.create(
                student_id="6510681234",
                first_name="Student",
                last_name="Study",
                email="student.stu@dome.tu.ac.th"
            )

class CourseViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.subject = Subject.objects.create(
            course_id="CN202",
            course_name="Data algorithm 1",
            course_semester="1/2567",
            course_amount=9999,
            course_status=Subject.CourseStatus.AVAILABLE,
        )

    def test_courses_view_get(self): #view ดึงหน้า html ถูกต้อง
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_courses/courses.html')
        self.assertIn('subjects', response.context)
        self.assertContains(response, self.subject.course_name)

    def test_courses_view_post_valid_data(self): #จำนวนคอร์สลดลงเมื่อกด regist
        response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
        self.assertEqual(self.subject.course_amount, 29)
        self.assertEqual(response.status_code, 302)

    def test_enroll_check_view(self): #กด regist แล้วหน้า enrollสถานะตรง
        response = self.client.get(reverse('enroll_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_courses/enroll_check.html')
        self.assertIn('subjects', response.context)
        self.assertContains(response, self.subject.course_name)

    def test_subject_transition(self): #ถ้าโควต้าเต็มสถานะต้องแสดง
        self.subject.course_amount = 1
        self.subject.save()
        response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.FULL)
   

