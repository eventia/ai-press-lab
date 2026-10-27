# 검증 Ch03
import sys, json, os, copy
sys.path.insert(0, ".")
from mywork.nlp import (extract_nouns, split_sentences, extract_keywords_tfidf,
                        extract_main_sentences, analyze_document)

assert os.path.exists("run_ch03.py"), "run_ch03.py가 없음 — 강사 코드(code 폴더)를 먼저 복사"

# ① 슬라이드 8의 예시를 그대로 재현 ("온라인쇼핑"이 쪼개지지 않아야 함)
nouns = extract_nouns("온라인쇼핑 거래액은 전월 대비 1.5% 증가하였다.")
print("명사:", nouns)
assert nouns == ["온라인쇼핑", "거래액", "전월", "대비", "증가"], "슬라이드 8과 다름(사용자 사전 확인)"

with open("mywork/press_data.json", encoding="utf-8") as f:
    data = json.load(f)
with open("data/raw_202601.json", encoding="utf-8") as f:
    raw = json.load(f)
text = data["원문"]
sentences = split_sentences(text)
assert len(sentences) == 4, f"문장 수가 4가 아님: {len(sentences)}"

# ② 키워드: 원문에 실제로 있는 두 글자 이상의 명사만, 점수는 파이썬 float
kw = extract_keywords_tfidf(text)
print("키워드 점수:", kw)
all_nouns = set(extract_nouns(text))
assert len(kw) == 5 and all(type(s) is float and w in all_nouns and len(w) > 1 for w, s in kw), "키워드 조건 위반"
assert "거래액" not in [w for w, _ in kw], "문장 단위 TF-IDF가 아님(문서 1건 TF-IDF는 '거래액'이 1위)"

# ③ 주요 문장: 원문 문장 그대로, 원문 순서
main = extract_main_sentences(sentences)
assert len(main) == 2 and all(s in sentences for s in main), "원문에 없는 문장이 나옴"
assert main == [s for s in sentences if s in main], "원문 순서가 아님"

# ④ run_ch03.py가 저장한 결과
assert "NLP분석결과" in data, "NLP분석결과가 저장되지 않음 — python run_ch03.py를 먼저 실행"
r = data["NLP분석결과"]
print("핵심키워드:", r["핵심키워드"])
print("주요문장:", r["주요문장"])
assert r == analyze_document(text, copy.deepcopy(data))["NLP분석결과"], "저장된 결과가 analyze_document 결과와 다름"
assert r["핵심키워드"] == [w for w, _ in kw]
assert all(s in sentences and any(k in s for k in r["핵심키워드"]) for s in r["주요문장"])
assert data["계산지표"] == raw["계산지표"], "계산지표가 원자료와 달라짐"
print("Ch03 OK — nlp.py 분석과 run_ch03.py 저장 결과 확인")
