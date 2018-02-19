from django.test import TestCase
from datetime import date


from .models import Education, Experience, Resume

class ResumeTest(TestCase):
    resume = Resume(first_name="Pritha", last_name="Dutta")
    education = Education(institution_name = "University of New Hampshire", location = "United States",
        degree = "Master of Science", major = "Information Technology", gpa = 3.78)
    experience = Experience(title = "Sftware Engineer", location = "India",
        start_date = 2014-01-17, end_date = 2017-05-31,
        description = "Software Development")

    def setUp(self):
        self.resume.save()
        self.education.save()
        self.experience.save()

    def test_get_full_name(self):
        """
        Tests get_full_name method of Resume model class
        """
        self.assertEqual(self.resume.get_full_name(), "Pritha Dutta")

    def test_get_last_name_first_name(self):
        """
        Tests get_last_name_first_name method of Resume model class
        """
        self.assertEqual(self.resume.get_last_name_first_name(), "Dutta Pritha")
    def test_get_experience(self):
        """
        Tests get_experience method of Resume model class
        """
        self.assertEqual(self.resume.get_experience().first(), self.experience)

    def test_get_education(self):
        """
        Tests get_education method of Resume model class
        """
        self.assertEqual(self.resume.get_education().first(), self.education)

# Create your tests  here.
