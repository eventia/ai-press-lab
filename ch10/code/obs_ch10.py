# 10차시 관찰 스크립트 — AI를 부르기 전의 보안 전처리(보안등급 확인·개인정보 마스킹)만 따로 실행해 본다
import os
import sys

import pandas as pd

sys.path.insert(0, ".")
from mywork.clean import check_data_grade, clean_and_structure, mask_personal_info
from mywork.data_io import load_input

원본 = "data/온라인쇼핑동향_2026_01.xlsx"
시험 = "data/보안전처리_실험.xlsx"


def 시험용_엑셀(보안등급, 덧붙일_원문=""):
    # 원자료 엑셀을 복사해 요약 시트의 보안등급·원문만 바꾼다(원본은 건드리지 않는다)
    시트 = pd.read_excel(원본, sheet_name=None, dtype={"연월": str, "공표일자": str})
    시트["요약"]["보안등급"] = 보안등급
    시트["요약"]["원문"] = 시트["요약"]["원문"] + 덧붙일_원문
    with pd.ExcelWriter(시험) as w:
        for 이름, 표 in 시트.items():
            표.to_excel(w, sheet_name=이름, index=False)


def 보안_전처리(경로):
    data = clean_and_structure(load_input(경로))
    check_data_grade(data)
    return mask_personal_info(data)


try:
    # ① 공개 자료 — 통과
    data = 보안_전처리(원본)
    print("① 공개:", data["문서정보"]["보안등급"], "→ 통과(AI 단계로 진행 가능)")
    # ② 대외비 자료 — AI 호출 전에 중단
    시험용_엑셀("대외비")
    try:
        보안_전처리(시험)
        print("② 대외비: 통과됨(문제!)")
    except PermissionError as e:
        print("② 대외비:", e)
    # ③ 원문에 연락처가 섞인 공개 자료 — 마스킹된 뒤에만 AI로 보낸다
    시험용_엑셀("공개", " 담당자 문의 010-1234-5678")
    print("③ 마스킹 후 원문 끝:", 보안_전처리(시험)["원문"][-30:])
finally:
    if os.path.exists(시험):
        os.remove(시험)
