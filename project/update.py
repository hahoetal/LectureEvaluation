# 강의 정보 업데이트
# bulk_update(objs,fields,batch_size=None)

# django 환경 설정
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# 코드 예시
# 핵심전공 -> 전공으로 변경하기

from crud.models import Lecture # 강의 모델 가져오기

lects = Lecture.objects.filter(separation='핵심전공') # 강의 구분이 '핵심전공'인 것만 가져오고, 

for lect in lects:
    lect.separation = "전공" # 강의 구분을 핵심전공에서 전공으로 변경

Lecture.objects.bulk_update(lects, ['professor']) # db에 저장!
# 모델(클래스).objects.bulk_update(objs, ['변경할 field'])