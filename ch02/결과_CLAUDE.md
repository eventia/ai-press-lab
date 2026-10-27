# AI 보도자료 작성 프로젝트 규칙

- 수치 계산(증감률, 비중, 순위 등)은 반드시 `mywork/stats.py`의 파이썬 함수가 처리하며, AI 모델에게 계산을 맡기지 않는다.
- API 비밀키(ANTHROPIC_API_KEY, PUBLIC_API_KEY)는 절대 코드에 직접 적지 않고 `.env` 파일에서 불러온다.
- AI가 생성한 문장은 `mywork/review.py`의 `verify_numbers`/`cross_check_all_numbers`로 원본 수치와 반드시 교차 검증한다.
- 문장은 자연스럽고 명확한 공공 보도자료체(객관적 서술체, "~하였다")로 작성한다.
- 모델 ID는 `mywork/write.py`의 `MODEL_NAME` 상수 한 곳에서만 관리한다.

<!-- quick-practice:common:start -->
## 10분 실습 공통 규칙 (mywork/)
- 모듈은 `mywork/` 패키지 안에, 실행·관찰 스크립트(`run_chNN.py`, `obs_chNN.py`, `api_chNN.py`)는 프로젝트 폴더 바로 아래에 만든다. 프롬프트의 설명만으로 직접 작성하고, 프로젝트 밖의 다른 코드는 열어보거나 복사하지 않는다.
- `mywork` 안의 모듈끼리는 절대 경로로 import 한다 (예: `from mywork.config import REQUIRED_FIELDS`).
- 프롬프트가 지정한 함수 이름·키를 그대로 쓴다. 구현 방법은 자유롭게 정하되, 요청하지 않은 기능·문서 파일은 추가하지 않는다.
- 표준 데이터(`mywork/press_data.json`)의 키 이름은 한글 그대로 쓴다 (`문서정보`, `계산지표`, `핵심내용`, `원문`, `품목별지표`, `월별이력`, `NLP분석결과`, `요약결과`, `통계해석결과`, `시각자료설명`, `헤드라인`, `본문`, `최종본`, `검수결과`).
- 기존 파일에 함수를 추가하라는 요청이면 이미 있는 함수는 고치지 않는다.
- 모듈을 만든 뒤에는 `python -c "import mywork.<모듈>"`로 import 오류를 확인하고, 실행·관찰 스크립트는 직접 실행해 결과를 보여 준다.
- 기준 검증 코드(`check.py`)는 고치지 않는다.
<!-- quick-practice:common:end -->

<!-- quick-practice:ch02:start -->
## 2차시 규칙 — 정제·표준화·구조화
- 정제·표준화 단계(`clean`)는 구조만 표준화하고 수치 계산은 하지 않는다. `계산지표`는 값을 바꾸지 않고 그대로 전달한다.
- 원본 자료(`data/raw_*.json`)와 입력 dict는 수정하지 않는다. 정제는 항상 사본에 적용한다(원본 보존).
- 표기 표준: 금액은 "억 원"처럼 숫자와 단위를 띄우고, 날짜는 YYYY-MM-DD로 통일한다.
- 개인정보(주민등록번호·휴대전화)는 정제 단계에서 코드로 마스킹한다(LLM에 보내기 전에).
<!-- quick-practice:ch02:end -->