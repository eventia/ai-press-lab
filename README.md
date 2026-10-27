# AI 보도자료 작성 실습 자료

생성형 AI(Claude Code)로 통계 보도자료 작성 도구를 만드는 2~10차시 실습 자료입니다.
수강생은 **프롬프트를 내려받아 Claude Code로 직접 코드를 만들어 보고**, 막히면 **강사가 같은 프롬프트로 만든 코드**를 내려받아 이어서 실습합니다.

> **데이터 안내**: `data/`의 수치는 실습용으로 만든 **가상 데이터**이며 실제 통계가 아닙니다. 자세한 내용은 [data/README.md](data/README.md)를 보세요.

## 폴더 구성

```text
ai-press-lab/
├─ README.md            이 문서
├─ requirements.txt     2~10차시 전체에서 쓰는 패키지
├─ .env.example         API 키 설정 예시 (.env 로 복사해서 사용, 공개 금지)
├─ .gitignore
├─ data/                실습 데이터 (가상 수치)
└─ ch02/ … ch10/        차시별 자료
   ├─ README.md         그 차시의 프롬프트·코드 목록과 쓰는 법
   ├─ prompts/          Claude Code에 붙여넣는 프롬프트 (A 모듈 · B 실행 · C 관찰 · D 실제 API 호출 · 수정요청예시)
   ├─ check/            기준 검증(check.py)과 기대 결과 — 내가 만든 코드를 정답과 대조
   ├─ CLAUDE_chNN블록.md   그 차시에 CLAUDE.md 에 이어 붙일 규칙 (3차시부터)
   ├─ 결과_CLAUDE.md     그 차시를 마친 시점의 CLAUDE.md 전체
   └─ code/             강사 코드 — 그 차시를 마친 시점의 프로젝트 상태
      ├─ mywork/        모듈 + press_data.json(표준 데이터)
      └─ run_·obs_·api_chNN.py
```

## 차시 목록

| 차시 | 폴더 | 주제 | 강사 코드 |
| --- | --- | --- | --- |
| 2 | [ch02/](ch02/) | 텍스트 정제·표준화·구조화 | 정답 코드 |
| 3 | [ch03/](ch03/) | 주요 NLP 기법 | 정답 코드 |
| 4 | [ch04/](ch04/) | LLM 기반 텍스트 요약 | 정답 코드 |
| 5 | [ch05/](ch05/) | 통계 계산과 해석문 | 정답 코드 |
| 6 | [ch06/](ch06/) | 표·그래프 설명문 | 정답 코드 |
| 7 | [ch07/](ch07/) | 원자료 입력·제목·부제·리드문 | 정답 코드 |
| 8 | [ch08/](ch08/) | 본문 단락 확장 | 정답 코드 |
| 9 | [ch09/](ch09/) | 문체 통일·검수·AI 감수 | 정답 코드 |
| 10 | [ch10/](ch10/) | 보도자료 자동 생성 시스템 | 정답 코드 |

## 실습 준비 (처음 한 번)

Windows PowerShell 기준입니다. 경로에 한글·공백이 없는 위치를 씁니다.

```powershell
# 1) 실습 폴더와 가상환경
New-Item -ItemType Directory C:\dev\quick-practice -Force | Out-Null
Set-Location C:\dev\quick-practice
python -m venv .venv
.\.venv\Scripts\Activate.ps1
$env:PYTHONUTF8 = "1"

# 2) 이 저장소에서 내려받은 requirements.txt 와 data 폴더를 실습 폴더로 복사한 뒤 설치
python -m pip install -r requirements.txt

# 3) (4차시부터) API 키 — .env.example 을 .env 로 복사하고 키를 채움
```

## 차시마다 하는 일

1. `chNN/README.md`를 엽니다.
2. CLAUDE.md를 준비합니다(2차시는 `결과_CLAUDE.md`를 `CLAUDE.md`로 저장, 3차시부터는 `CLAUDE_chNN블록.md`를 맨 아래에 이어 붙임).
3. 실습 폴더에서 `claude`로 Claude Code를 시작하고, `prompts/`의 프롬프트를 A → B → C → D 순서로 붙여넣습니다.
4. `check/check.py`를 실습 폴더에 `check.py`로 저장하고 `python check.py`로 검증합니다. `ChNN OK`가 나오면 통과입니다.
   실패하면 `수정요청예시.txt`처럼 오류 메시지를 붙여 수정을 요청합니다(검증 코드는 고치지 않습니다).
5. 그래도 막히면 `chNN/code/`의 강사 코드를 실습 폴더에 복사해 이어 갑니다. 중간 차시부터 시작할 때도 **바로 앞 차시**의 `code/`와 `결과_CLAUDE.md`를 복사하면 됩니다.

## 지켜야 할 것

- **API 키는 코드에 적지 않고 `.env`에만 둡니다.** `.env`는 저장소에 올리지 않습니다.
- 수치 계산은 AI가 아니라 파이썬 코드(`mywork/stats.py`)가 합니다. AI가 쓴 문장의 숫자는 원본과 교차 검증합니다.
- 생성형 AI는 같은 프롬프트에도 매번 조금 다른 코드를 만듭니다. 강사 코드는 정답이 아니라 **하나의 예시**입니다.
