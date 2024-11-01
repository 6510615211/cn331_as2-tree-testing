# from django.test import TestCase, Client
# from django.urls import reverse
# from app_courses.models import Subject, Student
# from django.db.utils import IntegrityError
# from django.core.exceptions import ValidationError

# class SubjectModelTest(TestCase):

#     def setUp(self):
#         self.subject = Subject.objects.create(
#             course_id="CS101",
#             course_name="Intro to Computer Science",
#             course_semester="2024A",
#             course_amount=30,
#             course_status=Subject.CourseStatus.AVAILABLE,
#         )

#     def test_subject_creation(self):
#         self.assertEqual(self.subject.course_id, "CS101")
#         self.assertEqual(self.subject.course_name, "Intro to Computer Science")
#         self.assertEqual(self.subject.course_semester, "2024A")
#         self.assertEqual(self.subject.course_amount, 30)
#         self.assertEqual(self.subject.course_status, Subject.CourseStatus.AVAILABLE)

#     def test_subject_string_representation(self):
#         expected_str = "CS101 Intro to Computer Science 2024A STATUS : Available"
#         self.assertEqual(str(self.subject), expected_str)

#     def test_update_course_status_and_amount(self):
#         self.subject.course_status = Subject.CourseStatus.REGISTERED
#         self.subject.course_amount -= 1
#         self.subject.save()
#         self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
#         self.assertEqual(self.subject.course_amount, 29)

#     def test_course_amount_never_negative(self):
#         # ตรวจสอบว่า course_amount จะไม่ลดลงต่ำกว่า 0
#         self.subject.course_amount = 0
#         self.subject.save()
#         self.subject.course_amount -= 1
#         self.subject.save()
#         self.assertEqual(self.subject.course_amount, 0)

#     def test_invalid_course_status(self):
#         # ตรวจสอบว่า course_status ที่ไม่ถูกต้องจะไม่สามารถบันทึกได้
#         with self.assertRaises(ValueError):
#             self.subject.course_status = "INVALID"
#             self.subject.save()

#     def test_blank_course_id(self):
#         with self.assertRaises(ValidationError):
#             self.subject.course_id = ""
#             self.subject.full_clean()

# class StudentModelTest(TestCase):

#     def setUp(self):
#         self.subject = Subject.objects.create(
#             course_id="CS101",
#             course_name="Intro to Computer Science",
#             course_semester="2024A",
#             course_amount=30,
#             course_status=Subject.CourseStatus.AVAILABLE,
#         )
#         self.student = Student.objects.create(
#             student_id="S001",
#             first_name="John",
#             last_name="Doe",
#             email="john.doe@example.com"
#         )
#         self.student.enrolled_subjects.add(self.subject)

#     def test_student_creation(self):
#         self.assertEqual(self.student.student_id, "S001")
#         self.assertEqual(self.student.first_name, "John")
#         self.assertEqual(self.student.last_name, "Doe")
#         self.assertEqual(self.student.email, "john.doe@example.com")

#     def test_student_string_representation(self):
#         self.assertEqual(str(self.student), "John Doe (john.doe@example.com)")

#     def test_student_enrollment(self):
#         self.assertIn(self.subject, self.student.enrolled_subjects.all())
#         self.assertIn(self.student, self.subject.students.all())

#     def test_remove_student_enrollment(self):
#         self.student.enrolled_subjects.remove(self.subject)
#         self.assertNotIn(self.subject, self.student.enrolled_subjects.all())
#         self.assertNotIn(self.student, self.subject.students.all())

#     def test_duplicate_student_id(self):
#         with self.assertRaises(IntegrityError):
#             Student.objects.create(
#                 student_id="S001",
#                 first_name="Jane",
#                 last_name="Smith",
#                 email="jane.smith@example.com"
#             )


# class CourseViewTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.subject = Subject.objects.create(
#             course_id="CS101",
#             course_name="Intro to Computer Science",
#             course_semester="2024A",
#             course_amount=30,
#             course_status=Subject.CourseStatus.AVAILABLE,
#         )

#     def test_courses_view_get(self):
#         response = self.client.get(reverse('courses'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app_courses/courses.html')
#         self.assertIn('subjects', response.context)
#         self.assertContains(response, self.subject.course_name)

#     def test_courses_view_post_valid_data(self):
#         response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
#         self.subject.refresh_from_db()
#         self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
#         self.assertEqual(self.subject.course_amount, 29)
#         self.assertEqual(response.status_code, 302)

#     def test_courses_view_post_invalid_data(self):
#         response = self.client.post(reverse('courses'), {'subject_id': 999})
#         self.assertEqual(response.status_code, 404)

#     def test_courses_view_post_no_data(self):
#         response = self.client.post(reverse('courses'), {})
#         self.assertEqual(response.status_code, 200)

#     def test_enroll_check_view(self):
#         response = self.client.get(reverse('enroll_check'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app_courses/enroll_check.html')
#         self.assertIn('subjects', response.context)
#         self.assertContains(response, self.subject.course_name)

#     def test_subject_availability_transition(self):
#         self.subject.course_amount = 1
#         self.subject.save()
#         response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
#         self.subject.refresh_from_db()
#         self.assertEqual(self.subject.course_status, Subject.CourseStatus.FULL)

from django.test import TestCase, Client
from django.urls import reverse
from app_courses.models import Subject, Student
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class SubjectModelTest(TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(
            course_id="CS101",
            course_name="Intro to Computer Science",
            course_semester="2024A",
            course_amount=30,
            course_status=Subject.CourseStatus.AVAILABLE,
        )

    def test_subject_creation(self):
        self.assertEqual(self.subject.course_id, "CS101")
        self.assertEqual(self.subject.course_name, "Intro to Computer Science")
        self.assertEqual(self.subject.course_semester, "2024A")
        self.assertEqual(self.subject.course_amount, 30)
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.AVAILABLE)

    def test_subject_string_representation(self):
        expected_str = "CS101 Intro to Computer Science 2024A STATUS: Available"
        self.assertEqual(str(self.subject), expected_str)

    def test_update_course_status_and_amount(self):
        self.subject.course_status = Subject.CourseStatus.REGISTERED
        self.subject.course_amount -= 1
        self.subject.save()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
        self.assertEqual(self.subject.course_amount, 29)

    def test_course_amount_never_negative(self):
        self.subject.course_amount = 0
        self.subject.save()
        with self.assertRaises(ValidationError):
            self.subject.course_amount -= 1
            self.subject.full_clean()

    def test_invalid_course_status(self):
        with self.assertRaises(ValueError):
            self.subject.course_status = "INVALID"
            self.subject.save()

    def test_blank_course_id(self):
        with self.assertRaises(ValidationError):
            self.subject.course_id = ""
            self.subject.full_clean()

class StudentModelTest(TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(
            course_id="CS101",
            course_name="Intro to Computer Science",
            course_semester="2024A",
            course_amount=30,
            course_status=Subject.CourseStatus.AVAILABLE,
        )
        self.student = Student.objects.create(
            student_id="S001",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        self.student.enrolled_subjects.add(self.subject)

    def test_student_creation(self):
        self.assertEqual(self.student.student_id, "S001")
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.email, "john.doe@example.com")

    def test_student_string_representation(self):
        self.assertEqual(str(self.student), "John Doe (john.doe@example.com)")

    def test_student_enrollment(self):
        self.assertIn(self.subject, self.student.enrolled_subjects.all())
        self.assertIn(self.student, self.subject.students.all())

    def test_remove_student_enrollment(self):
        self.student.enrolled_subjects.remove(self.subject)
        self.assertNotIn(self.subject, self.student.enrolled_subjects.all())
        self.assertNotIn(self.student, self.subject.students.all())

    def test_duplicate_student_id(self):
        with self.assertRaises(IntegrityError):
            Student.objects.create(
                student_id="S001",
                first_name="Jane",
                last_name="Smith",
                email="jane.smith@example.com"
            )

class CourseViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.subject = Subject.objects.create(
            course_id="CS101",
            course_name="Intro to Computer Science",
            course_semester="2024A",
            course_amount=30,
            course_status=Subject.CourseStatus.AVAILABLE,
        )

    def test_courses_view_get(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_courses/courses.html')
        self.assertIn('subjects', response.context)
        self.assertContains(response, self.subject.course_name)

    def test_courses_view_post_valid_data(self):
        response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.REGISTERED)
        self.assertEqual(self.subject.course_amount, 29)
        self.assertEqual(response.status_code, 302)

    def test_courses_view_post_invalid_data(self):
        response = self.client.post(reverse('courses'), {'subject_id': 999})
        self.assertEqual(response.status_code, 404)

    def test_courses_view_post_no_data(self):
        response = self.client.post(reverse('courses'), {})
        self.assertEqual(response.status_code, 200)

    def test_enroll_check_view(self):
        response = self.client.get(reverse('enroll_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_courses/enroll_check.html')
        self.assertIn('subjects', response.context)
        self.assertContains(response, self.subject.course_name)

    def test_subject_availability_transition(self):
        self.subject.course_amount = 1
        self.subject.save()
        response = self.client.post(reverse('courses'), {'subject_id': self.subject.id})
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.course_status, Subject.CourseStatus.FULL)
   

