# 8차시 관찰 스크립트 — 계산이 맞아도 원본에 없는 파생 수치는 검증에서 걸러지는지 확인한다
import json
import sys

sys.path.insert(0, ".")
from mywork.review import find_unverified_numbers

with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)

# 상위 3개 품목 비중의 합 82.0은 맞는 계산이지만 원본 데이터에는 없는 숫자다
비중 = [r["비중"] for r in data["품목별지표"][:3]]
문장 = "품목별 비중을 살펴보면 의류가 32.3%로 가장 컸으며, 상위 세 품목이 전체의 82.0%를 차지하였다."
print("상위 3개 비중:", 비중, "→ 합계", round(sum(비중), 1))
print("문장:", 문장)
print("근거 없는 숫자:", find_unverified_numbers(문장, data))
