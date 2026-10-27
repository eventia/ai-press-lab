# 9차시 관찰 스크립트 — 정규식 표기 검수가 잡는 것과 못 잡는 것을 확인한다
import sys

sys.path.insert(0, ".")
from mywork.review import check_formatting_errors

# 마지막 문장은 증감률에 %p를 잘못 쓴 오류지만 정규식으로는 잡지 못한다
for s in ["거래액은 201,250억 원이다.",
          "거래액은 201,250억원이다.",
          "2026년 거래액은 201250억 원이다.",
          "의류 비중이 3%p 확대되었다.",
          "의류 비중이 3% 확대되었다.",
          "거래액이 3%p 증가하였다."]:
    print(check_formatting_errors(s) or "문제 없음", "←", s)
