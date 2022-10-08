from random import choice, choices, randint

from django.core.files.base import File
from django.core.management.base import BaseCommand

from users.models import (
    AFFILIATION_CHOICES,
    DEGREE_CHOICES,
    FIELD_CHOICES,
    GENERATION_CHOICES,
    YEAR_CHOICES,
    AcademicBackground,
    Career,
    InterestedField,
    University,
    User,
)


def set_academic_backgrounds(user):
    for _ in range(randint(1,3)):
        pivot_index = choice(list(range(1,len(YEAR_CHOICES)-1)))
        academy_starting_year = choice(YEAR_CHOICES[:pivot_index])[0]
        academy_ending_year=choice(YEAR_CHOICES[pivot_index:])[0]
        AcademicBackground.objects.create(user=user,
            academy_affiliation=choice(AFFILIATION_CHOICES)[0],
            academy_field=choice(FIELD_CHOICES)[0],
            academy_starting_year=academy_starting_year,
            academy_ending_year=academy_ending_year,
            degree = choice(DEGREE_CHOICES)[0],
            institution=choice(University.get_university_list())[0],
            major = "test_major",
        )

def set_careers(user):
    for _ in range(randint(1,3)):
        pivot_index = choice(list(range(1,len(YEAR_CHOICES)-1)))
        career_starting_year = choice(YEAR_CHOICES[:pivot_index])[0]
        career_ending_year=choice(YEAR_CHOICES[pivot_index:])[0]
        Career.objects.create(user=user,
            career_affiliation=choice(AFFILIATION_CHOICES)[0],
            career_field=choice(AFFILIATION_CHOICES)[0],
            career_starting_year=career_starting_year,
            career_ending_year=career_ending_year,
            company="TEST_COMPANY",
            department="TEST_DEPARTMENT",
            position="TEST_POSITION",
        )


def create_test_user(index):
    cv_file = open('test_cv.pdf', 'rb')
    cv = File(cv_file)
    test_user = User.objects.create(
        username=get_random_username(),
        profile_photo_link = "https://mblogthumb-phinf.pstatic.net/20150427_261/ninevincent_1430122791768m7oO1_JPEG/kakao_1.jpg?type=w2",
        name=f"TEST{index}",
        generation = choice(GENERATION_CHOICES)[0],
        class_of_freshman=f"{choice(list(range(1,6)))}반",
        number_of_freshman = f"{choice(list(range(1,19)))}번",
        contactable_email = "test@email.com",
        contactable_phone_number = "01012345678",
        homepage_link=choices(["https://ddshs.co.kr",None]),
        linkedin_link=choices(["https://kr.linkedin.com/",None]),
        insta_link=choices(["https://www.instagram.com",None]),
        github_link=choices(["https://github.com/",None]),
        cv=cv,
        cv_link=choices(["https://www.feynmanlectures.caltech.edu/I_01.html",None]),
        email_accept =choice([True,False]),
        contact_description="test_contact_description",
        brief_self_introduction="test_brief_self_introduction",
    )
    test_user.interested_fields.set(choices(InterestedField.objects.all(), k=randint(1,4)))

    set_academic_backgrounds(test_user)
    set_careers(test_user)
    
    return test_user


def get_random_username():
    return ''.join([str(randint(0,9)) for _ in range(10)])


class Command(BaseCommand):
    help = 'create order of all curtains that had paid'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('numbers', type=int)

    def handle(self, *args, **options):
        for i in range(1, 1+options["numbers"]):
            create_test_user(i)
            print(f"TEST USER {i} CREATED")
