# 7차시 실제 API 호출 스크립트 — 제목·부제·리드문을 만들고, 모두 숫자 검증을 통과하면 저장한다 (비용 발생)
import json
import sys

sys.path.insert(0, ".")
from mywork.review import find_unverified_numbers
from mywork.write import generate_headline_set

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

hs = generate_headline_set(data)
문제 = []
for 항목 in ["제목", "부제", "리드문"]:
    근거없음 = find_unverified_numbers(hs[항목], data)
    문제 += 근거없음
    print(f"[{항목}] {hs[항목]}")
    print("   근거 없는 숫자:", 근거없음)

# 세 항목 중 하나라도 근거 없는 숫자가 있으면 저장하지 않는다
if 문제:
    sys.exit(f"근거 없는 숫자 {문제} — 저장하지 않았습니다. 한 번 더 실행해 보세요.")
data["헤드라인"] = hs
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"헤드라인 저장 — {DATA_PATH}")
