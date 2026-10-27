# AI 보도자료 작성 실습 자료

생성형 AI(Claude Code)로 통계 보도자료 작성 도구를 만드는 2~10차시 실습 자료입니다.

- 강의에서는 **프롬프트로 Claude Code가 코드를 만드는 과정**을 시연합니다. 이때 생성된 코드는 참고용입니다.
- 실습은 강사가 미리 만든 **강사 코드**(`chNN/code/`)로 진행합니다. 모두가 같은 코드로 같은 결과를 확인할 수 있습니다.
- 명령은 모두 Windows **명령 프롬프트(cmd)** 에서 실행합니다.

> **데이터 안내**: `data/`의 수치는 실습용으로 만든 **가상 데이터**이며 실제 통계가 아닙니다. 자세한 내용은 [data/README.md](data/README.md)를 보세요.

## 폴더 구성

```text
ai-press-lab/
├─ README.md            이 문서
├─ requirements.txt     2~10차시 전체에서 쓰는 패키지
├─ .env.example         API 키 설정 예시 (실습 폴더에 .env 로 복사해서 사용, 공개 금지)
├─ data/                실습 데이터 (가상 수치)
└─ ch02/ … ch10/        차시별 자료
   ├─ README.md         그 차시의 실습 순서(cmd 명령)와 파일 목록
   ├─ prompts/          Claude Code 시연용 프롬프트 (A 모듈 · B 실행 · C 관찰 · D 실제 API 호출)
   ├─ check/            기준 검증(check.py)과 기대 결과
   ├─ 결과_CLAUDE.md     그 차시에 쓰는 CLAUDE.md 전체
   └─ code/             강사 코드 — 그 차시를 마친 시점의 실습 폴더 상태
```

## 차시 목록

| 차시 | 폴더 | 주제 |
| --- | --- | --- |
| 2 | [ch02/](ch02/) | 텍스트 정제·표준화·구조화 |
| 3 | [ch03/](ch03/) | 주요 NLP 기법 |
| 4 | [ch04/](ch04/) | LLM 기반 텍스트 요약 |
| 5 | [ch05/](ch05/) | 통계 계산과 해석문 |
| 6 | [ch06/](ch06/) | 표·그래프 설명문 |
| 7 | [ch07/](ch07/) | 원자료 입력·제목·부제·리드문 |
| 8 | [ch08/](ch08/) | 본문 단락 확장 |
| 9 | [ch09/](ch09/) | 문체 통일·검수·AI 감수 |
| 10 | [ch10/](ch10/) | 보도자료 자동 생성 시스템 |

## 실습 준비 (처음 한 번)

명령 프롬프트(cmd)를 열고 차례로 실행합니다. 파이썬 3.10 이상이 필요합니다(3.13에서 확인).

**1) 실습 자료 내려받기** — `C:\dev\ai-press-lab`에 둡니다.

```bat
mkdir C:\dev
cd /d C:\dev
git clone https://github.com/eventia/ai-press-lab.git
```

git이 없으면 https://github.com/eventia/ai-press-lab 에서 **Code → Download ZIP**으로 내려받아 `C:\dev`에 압축을 풀고, 폴더 이름을 `ai-press-lab`으로 바꿉니다.

**2) 실습 폴더와 가상환경** — 실습은 자료 폴더와 따로 `C:\dev\quick-practice`에서 합니다.

```bat
mkdir C:\dev\quick-practice
cd /d C:\dev\quick-practice
python -m venv .venv
.venv\Scripts\activate
set PYTHONUTF8=1
set LAB=C:\dev\ai-press-lab
copy %LAB%\requirements.txt .
python -m pip install -r requirements.txt
```

**3) (4차시부터) API 키** — `copy %LAB%\.env.example .env` 후 `notepad .env`로 `ANTHROPIC_API_KEY=` 뒤에 키를 적고 저장합니다.

> 명령 프롬프트 창을 새로 열 때마다 `cd /d C:\dev\quick-practice`, `.venv\Scripts\activate`, `set PYTHONUTF8=1`, `set LAB=C:\dev\ai-press-lab` 네 줄을 다시 실행합니다. 각 차시 README의 첫 명령에 들어 있습니다.

## 차시마다 하는 일

1. `chNN/README.md`를 엽니다.
2. 실습 폴더를 앞 차시를 마친 상태로 맞추고, 이번 차시의 `CLAUDE.md`를 복사합니다.
3. (시연) `claude`로 Claude Code를 시작하고 `prompts/`의 프롬프트를 붙여넣어 코드가 만들어지는 과정을 봅니다.
4. 강사 코드(`chNN/code/`)를 실습 폴더에 덮어쓰고 실행합니다.
5. `check/check.py`로 기준 검증을 합니다. 마지막 줄에 `ChNN OK`가 나오면 통과입니다.

## 지켜야 할 것

- **API 키는 코드에 적지 않고 `.env`에만 둡니다.** `.env`는 저장소에 올리지 않습니다.
- 수치 계산은 AI가 아니라 파이썬 코드(`mywork/stats.py`)가 합니다. AI가 쓴 문장의 숫자는 원본과 교차 검증합니다.
- 생성형 AI는 같은 프롬프트에도 매번 조금 다른 코드를 만듭니다. 그래서 실습은 강사 코드로 진행합니다.
