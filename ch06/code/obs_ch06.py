# 6차시 관찰 스크립트 — 변곡점이 어디인지, 설명문의 주어와 조사를 확인한다
import json

import pandas as pd

with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)

# ① 월별 증감과 방향이 바뀌는 달(이번 달 증감과 다음 달 증감의 부호가 반대)
h = pd.DataFrame(data["월별이력"]).rename(columns={"값": "거래액"}).sort_values("연월").reset_index(drop=True)
h["증감"] = h["거래액"].diff()
h["방향바뀜"] = h["증감"] * h["증감"].shift(-1) < 0
print("① 최근 6개월")
print(h.tail(6).to_string(index=False))

# ② 저장된 설명문 — 주어가 있는지, 조사가 자연스러운지 본다
for v in data["시각자료설명"]:
    print(f"② [{v['소주제']}] {v['설명문']}")
