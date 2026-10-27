# 5차시 실행 스크립트 — press_data.json에 통계 계산 결과를 더해 저장한다
import copy
import json
import sys

sys.path.insert(0, ".")
from mywork.stats import add_calculated_indicators

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

계산지표_전 = copy.deepcopy(data["계산지표"])
data = add_calculated_indicators(data)

# 계산지표가 바뀌었다면 저장하지 않고 멈춘다
if data["계산지표"] != 계산지표_전:
    sys.exit("오류: 계산지표가 바뀌었습니다 — 저장하지 않았습니다.")

print("[품목별지표]")
print(f"{'품목':<6}{'당월거래액':>10}{'전월대비증감률':>10}{'비중':>7}{'순위':>5}")
for r in data["품목별지표"]:
    print(f"{r['품목']:<6}{r['당월거래액']:>12,}{r['전월대비증감률']:>12}{r['비중']:>9}{r['순위']:>5}")
print("역대최대여부:", data.get("역대최대여부"))
print("최근3개월증감률:", data.get("최근3개월증감률"))
print("특이점목록:", data["통계해석결과"]["특이점목록"])
for s in data["통계해석결과"]["해석문장"]:
    print("해석문장:", s)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"저장 완료 — {DATA_PATH}")
