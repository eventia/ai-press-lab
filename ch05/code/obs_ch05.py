# 5차시 관찰 스크립트 — 동월 비교와 abs()가 필요한 이유를 눈으로 확인한다
import json
import sys

import pandas as pd

sys.path.insert(0, ".")
from mywork.stats import derive_history_indicators, generate_interpretation

with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)

# ① pct_change 한 줄로 전월대비증감률 — 첫 행은 비교할 전월이 없어 NaN이 정상
df = pd.DataFrame({"연월": ["2025-12", "2026-01"], "거래액": [198276, 201250]})
df["전월대비증감률"] = (df["거래액"].pct_change() * 100).round(1)
print("① pct_change")
print(df.to_string(index=False))

# ② 이번 달이 186,000억 원이었다면? 같은 달(1월)끼리 비교 vs 모든 달과 비교
과거 = [h for h in data["월별이력"] if h["연월"] < "2026-01"]
print("② 동월(1월) 기준 역대 최대:", derive_history_indicators(과거, "2026-01", 186000)["역대최대여부"])
print("② 모든 달과 비교한 최대:", 186000 >= max(h["값"] for h in 과거))

# ③ 감소 템플릿에 부호를 그대로 넣은 문장과 abs()로 뗀 문장
print("③ abs 없음:", generate_interpretation("온라인쇼핑 거래액", -6.2, "%", "전월 대비 큰 폭 감소"))
print("③ abs 사용:", generate_interpretation("온라인쇼핑 거래액", abs(-6.2), "%", "전월 대비 큰 폭 감소"))
