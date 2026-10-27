# 4차시 실제 API 호출 스크립트 — 3줄 요약·제목 후보를 만들고, 숫자 검증을 통과하면 저장한다 (비용 발생)
import json
import sys

sys.path.insert(0, ".")
from mywork.review import find_unverified_numbers
from mywork.write import MODEL_NAME, generate_summary

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

result = generate_summary(data)
print("모델:", MODEL_NAME)
문제 = []
for 종류, 문장들 in (("요약", result["삼줄요약"]), ("제목", result["제목후보"])):
    for s in 문장들:
        근거없음 = find_unverified_numbers(s, data)
        문제 += 근거없음
        print(f"{종류}: {s} | 근거 없는 숫자: {근거없음}")

# 근거 없는 숫자가 하나라도 있으면 저장하지 않는다
if 문제:
    sys.exit(f"근거 없는 숫자 {문제} — 저장하지 않았습니다. 한 번 더 실행해 보세요.")
data["요약결과"] = result
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"요약결과 저장 — {DATA_PATH}")
