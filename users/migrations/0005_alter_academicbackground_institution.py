# Generated by Django 4.1.1 on 2022-10-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_academicbackground_academy_field_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicbackground",
            name="institution",
            field=models.CharField(
                choices=[
                    ("-추가 필요-", "-추가 필요-(선택시 추가 가능)"),
                    ("-추가 필요-", "-추가 필요-(NEED ADD)"),
                    ("가천대학교", "가천대학교(GU)"),
                    ("건국대학교", "건국대학교(Konkuk)"),
                    ("경북대학교", "경북대학교(KNU)"),
                    ("경희대학교", "경희대학교(KHU)"),
                    ("고려대학교", "고려대학교(KU)"),
                    ("광운대학교", "광운대학교(KW)"),
                    ("국민대학교", "국민대학교(KMU)"),
                    ("단국대학교", "단국대학교(DKU)"),
                    ("동국대학교", "동국대학교(Dongguk)"),
                    ("명지대학교", "명지대학교(MJU)"),
                    ("부산대학교", "부산대학교(PNU)"),
                    ("삼육대학교", "삼육대학교(SYU)"),
                    ("상명대학교", "상명대학교(SMU)"),
                    ("서강대학교", "서강대학교(Sogang)"),
                    ("서경대학교", "서경대학교(SKU)"),
                    ("서울대학교", "서울대학교(SNU)"),
                    ("세종대학교", "세종대학교(SEJONG)"),
                    ("숭실대학교", "숭실대학교(SSU)"),
                    ("아주대학교", "아주대학교(Ajou)"),
                    ("연세대학교", "연세대학교(YU)"),
                    ("인하대학교", "인하대학교(Inha)"),
                    ("전남대학교", "전남대학교(JNU)"),
                    ("전북대학교", "전북대학교(JBNU)"),
                    ("중앙대학교", "중앙대학교(CAU)"),
                    ("충남대학교", "충남대학교(CNU)"),
                    ("충북대학교", "충북대학교(CBNU)"),
                    ("한성대학교", "한성대학교(HSU)"),
                    ("한양대학교", "한양대학교(HYU)"),
                    ("홍익대학교", "홍익대학교(Hongik)"),
                    ("가톨릭대학교", "가톨릭대학교(CUK)"),
                    ("성균관대학교", "성균관대학교(SKKU)"),
                    ("과학기술대학교", "과학기술대학교(SEOULTECH)"),
                    ("광주과학기술원", "광주과학기술원(GIST)"),
                    ("대구과학기술원", "대구과학기술원(DGIST)"),
                    ("덕성여자대학교", "덕성여자대학교(DSWU)"),
                    ("동덕여자대학교", "동덕여자대학교(DWU)"),
                    ("서울시립대학교", "서울시립대학교(UOS)"),
                    ("성신여자대학교", "성신여자대학교(SSWU)"),
                    ("숙명여자대학교", "숙명여자대학교(SMWU)"),
                    ("울산과학기술원", "울산과학기술원(UNIST)"),
                    ("이화여자대학교", "이화여자대학교(EWHA)"),
                    ("포항공과대학교", "포항공과대학교(POSTECH)"),
                    ("한국과학기술원", "한국과학기술원(KAIST)"),
                    ("한국외국어대학교", "한국외국어대학교(HUFS)"),
                ],
                max_length=200,
            ),
        ),
    ]
