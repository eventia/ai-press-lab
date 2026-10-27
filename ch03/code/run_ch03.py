# 3차시 실행 스크립트 — 원문에서 핵심 키워드·주요 문장을 뽑아 press_data.json에 더해 저장한다
import json
import sys

sys.path.insert(0, ".")
from mywork.nlp import analyze_document, extract_keywords_tfidf

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

# NLP분석결과 외의 기존 필드는 그대로 두어야 한다
기존 = {k: v for k, v in data.items() if k != "NLP분석결과"}
data = analyze_document(data["원문"], data)
if {k: v for k, v in data.items() if k != "NLP분석결과"} != 기존:
    sys.exit("오류: NLP분석결과 외의 필드가 바뀌었습니다 — 저장하지 않았습니다.")

print("[키워드 점수]", extract_keywords_tfidf(data["원문"]))
print("[핵심키워드]", data["NLP분석결과"]["핵심키워드"])
for s in data["NLP분석결과"]["주요문장"]:
    print("[주요문장]", s)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"저장 완료 — {DATA_PATH}")
