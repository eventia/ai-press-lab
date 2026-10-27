# 8차시 실제 API 호출 스크립트 — 소주제별 본문 단락을 만들고, 모두 숫자 검증을 통과하면 저장한다 (비용 발생, 3회)
import json
import sys

sys.path.insert(0, ".")
from mywork.review import find_unverified_numbers
from mywork.write import generate_body_paragraphs

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

본문 = generate_body_paragraphs(data)
문제 = []
for p in 본문:
    근거없음 = find_unverified_numbers(p["내용"], data)
    문제 += 근거없음
    print(f"[{p['소주제']}] {p['내용']}")
    print("   근거 없는 숫자:", 근거없음)

# 단락 하나라도 근거 없는 숫자가 있으면 저장하지 않는다
if 문제:
    sys.exit(f"근거 없는 숫자 {문제} — 저장하지 않았습니다. 한 번 더 실행해 보세요.")
data["본문"] = 본문
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"본문 저장 — {DATA_PATH}")
