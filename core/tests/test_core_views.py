from django.test import Client, TestCase
from django.urls import reverse

from core.views import (
    filter_by_affiliation,
    filter_by_generation,
    filter_by_institution,
    filter_by_major_field,
    filter_by_search_text,
)
from users.management.commands.create_test_users import create_test_user
from users.management.commands.set_default_universities import set_universities
from users.management.commands.set_interested_fields import set_interested_fields
from users.models import AcademicBackground, Career, InterestedField, User


def create_gist_physics_cs_career_user():
    user = User.objects.create(
        name="!TESTUSER!",
        profile_photo_link="",
        generation="1",
        class_of_freshman="3",
        number_of_freshman = "6",
        contactable_email="testemail@email.com",
        contactable_phone_number="123456789",
        homepage_link="https://testhomapge_link",
        contact_description="TEST_CONTACT_DESCRIPTION",
        brief_self_introduction="TEST_BREIF_SELF_INTRODUCTION"
    )
    gist_physics = AcademicBackground.objects.create(
        user=user,
        academy_affiliation = "NATURAL SCIENCE",
        academy_field = "Physics",
        academy_starting_year = "2016",
        academy_ending_year  = "2022",
        degree="BS",
        institution = "광주과학기술원",
        major="테스트용 물리전공"
    )
    cs_career = Career.objects.create(
        user = user,
        career_affiliation = "ENGINEERING",
        career_field = "Computer Science",
        career_starting_year = "2021",
        career_ending_year = "2021",
        company = "TESTCOMPANY",
        department="테스트부서",
        position="TESTER"
    )
    user.academic_backgrounds.add(gist_physics)
    user.careers.add(cs_career)

    physics = InterestedField.objects.get(field="Physics")
    cs = InterestedField.objects.get(field="Computer Science")
    user.interested_fields.add(cs,physics)

    return user


class UserViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        
        set_universities()
        set_interested_fields()
        self.user = create_test_user(0)
        for i in range(1,11):
            create_test_user(i)
        
        self.gist_physics_cs_career_user = create_gist_physics_cs_career_user()

    def test_api(self):
        response = self.client.get(reverse("core:api"))
        assert len(response.json()["users"])==12

    def test_search_text(self):
        all_users = User.objects.all()
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"!TESTUSER!")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"testemail@email.com")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"123456789")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"testhomapge_link")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"TEST_CONTACT_DESCRIPTION")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"TEST_BREIF_SELF_INTRODUCTION")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"테스트용 물리전공")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"테스트부서")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_search_text(all_users,"TESTCOMPANY")
        )


    def test_search_affiliation(self):
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_affiliation(User.objects.all(), "NATURAL SCIENCE")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_affiliation(User.objects.all(), "ENGINEERING")
        )
    
    def test_search_institution(self):
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_institution(User.objects.all(), "광주과학기술원")
        )

    def test_search_major_field(self):
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_major_field(User.objects.all(), "Physics")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_major_field(User.objects.all(), "Computer Science")
        )

    def test_search_interested_field(self):
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_major_field(User.objects.all(), "Physics")
        )
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_major_field(User.objects.all(), "Computer Science")
        )

    def test_search_generation(self):
        self.assertTrue(
            self.gist_physics_cs_career_user in filter_by_generation(User.objects.all(), "1")
        )
