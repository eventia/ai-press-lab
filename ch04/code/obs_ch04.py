# 4차시 관찰 스크립트 — load_dotenv 순서와, 숫자 검증이 잡는 것·못 잡는 것을 확인한다
import os
import sys

sys.path.insert(0, ".")
# ① .env는 저절로 읽히지 않는다 — load_dotenv() 전후로 키가 보이는지 비교
print("① load_dotenv 전:", "키 있음" if os.getenv("ANTHROPIC_API_KEY") else "키 없음")
from dotenv import load_dotenv

load_dotenv()
print("① load_dotenv 후:", "키 있음" if os.getenv("ANTHROPIC_API_KEY") else "키 없음(.env 확인)")

# ② 숫자 검증은 바꿔 쓴 숫자는 잡지만, 과장 표현과 1~2자리 정수는 못 잡는다
from mywork.review import find_unverified_numbers

data = {"계산지표": {"총거래액": 201250, "전월대비증감률": 1.5, "전년동월대비증감률": 8.7}}
for s in ["거래액은 201,250억 원으로 전월 대비 1.5% 증가하였다.",
          "거래액은 201,520억 원으로 전월 대비 1.6% 증가하였다.",
          "역대 최대 실적을 압도적으로 경신하며 사상 최고의 성장세를 보였다.",
          "모바일쇼핑 비중은 78%로 15% 늘었다."]:
    print("② 근거 없는 숫자:", find_unverified_numbers(s, data), "←", s)
