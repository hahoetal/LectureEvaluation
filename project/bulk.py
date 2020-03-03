# 강의 정보를 크롤링하여 csv 파일로 만든 다음에 이를 Lecture 모델로 만들기.
# admin에서 직접 입력하던 것을 자동으로 해봅시다!!

import os
import django # django 내부 설정과 모델 인식을 위해 불러옴.
import csv # csv 파일을 다룰 것이기 때문에 불러 옴.

# django에서 사용한 것과 동일하게 환경설정을 하기.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') # '<프로젝트 명>.settings'
django.setup()

# crud 앱에 있는 Lecture 모델을 불러오고
from crud.models import Lecture

# 강의 정보가 담긴 csv 파일을 읽기 모드로 열고,
f = open('lect.csv', 'r', encoding='utf-8')
info = [] # 강의 정보를 담을 리스트
content = csv.reader(f) # csv 파일을 열어 content에 넣기

#  데이터를 튜플 형태로 만들어서 리스트에 넣기
for c in content:
    lectName=c[0]
    nameP=c[1]
    nameM=c[2]
    detatil=c[3]
    lectInfo = (lectName, nameP, nameM, detatil)
    info.append(lectInfo)

f.close() # 파일을 열었다면... 꼭 파일 닫아주기

lect =[]
for (lectName, nameP, nameM, detatil) in info: # info에 담긴 튜플(강의 정보)를 하나씩 꺼내고 각 요소를 lectName, nameP, nameM, detail에 담고
    lect.append(Lecture(lectureName=lectName, professor=nameP, major=nameM, separation=detatil)) # Lecture 모델을 구성하는 것과 짝지어주기

Lecture.objects.bulk_create(lect) # 리스트 lect의 내용을 기반으로 Lecture 모델 객체 만들어서 DB에 저장

# 위 코드들이 실행되려면... 터미널에서 해당 파일 실행시켜주기!!