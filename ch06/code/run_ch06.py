# 6차시 실행 스크립트 — 그래프를 그리고 설명문과 함께 시각자료설명으로 저장한다
import json
import os
import sys

sys.path.insert(0, ".")
from mywork.charts import build_visual_descriptions

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

visuals = build_visual_descriptions(data)
for v in visuals:
    상태 = "있음" if os.path.exists(v["이미지경로"]) else "없음"
    print(f"[{v['소주제']}] {v['그래프유형']} — {v['이미지경로']}({상태})")
    print("  ", v["설명문"])

data["시각자료설명"] = visuals
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"저장 완료 — {DATA_PATH}")
