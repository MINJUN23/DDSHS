from django.core.management.base import BaseCommand
from users.models import University

DEFAULT_UNIVERSITIES = [
    {"name": "서울대학교", "acronym": "SNU"},
    {"name": "고려대학교", "acronym": "KU"},
    {"name": "연세대학교", "acronym": "YU"},
    {"name": "서강대학교", "acronym": "Sogang"},
    {"name": "성균관대학교", "acronym": "SKKU"},
    {"name": "한양대학교", "acronym": "HYU"},
    {"name": "중앙대학교", "acronym": "CAU"},
    {"name": "경희대학교", "acronym": "KHU"},
    {"name": "한국외국어대학교", "acronym": "HUFS"},
    {"name": "서울시립대학교", "acronym": "UOS"},
    {"name": "건국대학교", "acronym": "Konkuk"},
    {"name": "동국대학교", "acronym": "Dongguk"},
    {"name": "홍익대학교", "acronym": "Hongik"},
    {"name": "인하대학교", "acronym": "Inha"},
    {"name": "아주대학교", "acronym": "Ajou"},
    {"name": "단국대학교", "acronym": "DKU"},
    {"name": "숭실대학교", "acronym": "SSU"},
    {"name": "국민대학교", "acronym": "KMU"},
    {"name": "세종대학교", "acronym": "SEJONG"},
    {"name": "과학기술대학교", "acronym": "SEOULTECH"},
    {"name": "광운대학교", "acronym": "KW"},
    {"name": "명지대학교", "acronym": "MJU"},
    {"name": "상명대학교", "acronym": "SMU"},
    {"name": "가톨릭대학교", "acronym": "CUK"},
    {"name": "한성대학교", "acronym": "HSU"},
    {"name": "서경대학교", "acronym": "SKU"},
    {"name": "삼육대학교", "acronym": "SYU"},
    {"name": "충남대학교", "acronym": "CNU"},
    {"name": "충북대학교", "acronym": "CBNU"},
    {"name": "전북대학교", "acronym": "JBNU"},
    {"name": "부산대학교", "acronym": "PNU"},
    {"name": "경북대학교", "acronym": "KNU"},
    {"name": "전남대학교", "acronym": "JNU"},
    {"name": "가천대학교", "acronym": "GU"},
    {"name": "이화여자대학교", "acronym": "EWHA"},
    {"name": "숙명여자대학교", "acronym": "SMWU"},
    {"name": "성신여자대학교", "acronym": "SSWU"},
    {"name": "동덕여자대학교", "acronym": "DWU"},
    {"name": "덕성여자대학교", "acronym": "DSWU"},
    {"name": "한국과학기술원", "acronym": "KAIST"},
    {"name": "포항공과대학교", "acronym": "POSTECH"},
    {"name": "광주과학기술원", "acronym": "GIST"},
    {"name": "대구과학기술원", "acronym": "DGIST"},
    {"name": "울산과학기술원", "acronym": "UNIST"},
    {"name": "-추가 필요-", "acronym": "NEED ADD"},
]


class Command(BaseCommand):
    help = 'Set default universities'

    def handle(self, *args, **options):
        for UNIVERSITY in DEFAULT_UNIVERSITIES:
            university = University.objects.get_or_create(
                name=UNIVERSITY["name"],
                acronym=UNIVERSITY["acronym"])
            print(university)
