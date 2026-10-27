# 2차시 실행 스크립트 — 원본 자료를 정제·구조화해 표준 데이터(press_data.json)로 저장한다
import json
import sys

sys.path.insert(0, ".")
from mywork.clean import clean_and_structure

RAW_PATH = "data/raw_202601.json"
DATA_PATH = "mywork/press_data.json"

with open(RAW_PATH, encoding="utf-8") as f:
    raw = json.load(f)

data = clean_and_structure(raw)

print("[정제 전]", raw["원문"][:70].replace("\n", "\n"), "...")
print("[정제 후]", data["원문"][:70], "...")
print("[문서정보]", data["문서정보"])
print("[계산지표]", data["계산지표"])
print(f"[품목별지표] {len(data.get('품목별지표', []))}개, [월별이력] {len(data.get('월별이력', []))}개")

# 원본 파일은 열어서 읽기만 하고, 결과는 다른 파일에 저장한다
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"저장 완료 — {DATA_PATH} (원본 {RAW_PATH}는 그대로)")
