# 7차시 관찰 스크립트 — 엑셀 숫자 타입의 함정과 6하원칙 헤드라인 프롬프트를 확인한다
import json
import sys

import pandas as pd

sys.path.insert(0, ".")
import mywork.write as W

# ① 엑셀 값은 겉보기에 정수여도 numpy 타입이다
v = pd.read_excel("data/온라인쇼핑동향_2026_01.xlsx").iloc[0]["총거래액"]
print("① 엑셀에서 읽은 값의 타입:", type(v).__name__)
try:
    json.dumps({"총거래액": v})
except TypeError as e:
    print("① 그대로 저장하면:", e)

# ② LLM에 보낼 헤드라인 프롬프트 전체 — API는 부르지 않는다
with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)
print("② 헤드라인 프롬프트 ↓")
print(W.build_headline_prompt(W.select_core_indicators(data["계산지표"]), data["통계해석결과"]["특이점목록"], data["문서정보"]))
