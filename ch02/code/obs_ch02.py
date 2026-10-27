# 2차시 관찰 스크립트 — 원본은 그대로, 정제본만 바뀌는지 확인한다
import json
import sys

sys.path.insert(0, ".")
from mywork.clean import mask_sensitive_info

with open("data/raw_202601.json", encoding="utf-8") as f:
    raw = json.load(f)
with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)

# ① 원문 앞부분 비교 — repr로 보여 주어 공백·줄바꿈 차이가 드러나게 한다
print("① [원본 원문]", repr(raw["원문"][:60]), "...")
print("① [정제 원문]", repr(data["원문"][:60]), "...")
# ② 공표일자 표준화와 계산지표 보존
print("② [원본 공표일자]", raw["공표일자"], "→ [정제]", data["문서정보"]["공표일자"])
print("② [계산지표 동일?]", raw["계산지표"] == data["계산지표"])
# ③ 마스킹 사례 — 지역번호는 휴대전화가 아니므로 그대로
for s in ["문의 010-1234-5678", "문의 011-123-4567", "문의 02-123-4567", "주민 900101-1234567"]:
    print("③", s, "->", mask_sensitive_info(s))
