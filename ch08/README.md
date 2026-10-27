# 8차시 — 본문 단락 확장

> 강의에서는 `prompts/`의 프롬프트로 Claude Code가 코드를 만드는 과정을 **시연**합니다(생성된 코드는 참고용).
> 실습은 강사가 미리 만든 **`code/`의 코드**로 진행합니다. 명령은 모두 **명령 프롬프트(cmd)** 에서 실행합니다.

## 1. 실습 순서

**① 실습 폴더 맞추기** — 앞 차시를 마친 상태로 맞추고, 이번 차시의 CLAUDE.md를 넣습니다(앞 차시를 건너뛰었어도 이것만 하면 됩니다).

```bat
cd /d C:\dev\quick-practice
.venv\Scripts\activate
set PYTHONUTF8=1
set LAB=C:\dev\ai-press-lab
xcopy %LAB%\data data\ /E /I /Y /Q
xcopy %LAB%\ch07\code . /E /Y /Q
copy /Y %LAB%\ch08\결과_CLAUDE.md CLAUDE.md
```

**② (시연) 프롬프트로 코드 만들기** — `claude`로 Claude Code를 시작하고 `prompts/`의 프롬프트를 차례로 붙여넣습니다. 만들어진 코드는 읽어 보고 다음 단계에서 강사 코드로 덮어씁니다.

**③ 강사 코드로 실습하기** — 강사 코드를 복사해 실행하고, 기준 검증으로 확인합니다.

```bat
xcopy %LAB%\ch08\code . /E /Y /Q
python obs_ch08.py
copy /Y %LAB%\ch08\check\check.py check.py
python check.py
```

마지막 줄에 `Ch08 OK`가 나오면 통과입니다([check/기대결과.txt](check/기대결과.txt)와 비교).

**④ 실제 API 호출** (`.env`에 `ANTHROPIC_API_KEY`가 있을 때, 비용 발생)

```bat
python api_ch08.py
```

## 2. 프롬프트 (`prompts/`)

강의에서 시연하는 프롬프트입니다. 집에서 직접 Claude Code로 만들어 보고 싶다면 위에서부터 차례로 붙여넣으세요.

| 파일 | 하는 일 |
| --- | --- |
| [프롬프트A.txt](prompts/프롬프트A.txt) | 모듈 만들기 (mywork/) |
| [프롬프트C.txt](prompts/프롬프트C.txt) | 관찰 실험 스크립트 만들기 (obs_ch08.py) |
| [프롬프트D.txt](prompts/프롬프트D.txt) | 실제 API 호출 스크립트 만들기 (api_ch08.py) |
| [수정요청예시.txt](prompts/수정요청예시.txt) | 직접 만든 코드가 기준 검증에서 실패했을 때 오류 메시지를 붙여 수정 요청 |

## 3. 기준 검증 (`check/`)

코드가 강의 내용대로 동작하는지 정답과 대조합니다. 실제 API는 부르지 않습니다(비용 0, API 키 불필요).
검증 코드는 Claude Code에게 만들게 하거나 고치게 하지 않습니다(코드와 테스트를 같은 AI가 만들면 서로 맞춰 버릴 수 있음).

## 4. 강사 코드 (`code/`)

**8차시를 마친 시점의 실습 폴더 상태** 그대로입니다. 실습 폴더(`C:\dev\quick-practice`)에 덮어써서 씁니다.

| 파일 | 설명 |
| --- | --- |
| `mywork/__init__.py` | 빈 파일(패키지 표시) |
| `mywork/charts.py` | 앞 차시에서 만든 파일 |
| `mywork/clean.py` | 앞 차시에서 만든 파일 |
| `mywork/config.py` | 앞 차시에서 만든 파일 |
| `mywork/data_io.py` | 앞 차시에서 만든 파일 |
| `mywork/nlp.py` | 앞 차시에서 만든 파일 |
| `mywork/press_data.json` | 8차시를 마친 시점의 표준 데이터 |
| `mywork/review.py` | 앞 차시에서 만든 파일 |
| `mywork/stats.py` | 앞 차시에서 만든 파일 |
| `mywork/write.py` | **8차시에 만들거나 고친 파일** |
| `api_ch08.py` | 실제 API 호출(API 키 필요) — 실습 폴더 바로 아래에 둡니다 |
| `obs_ch08.py` | 관찰 실험 — 실습 폴더 바로 아래에 둡니다 |

- [결과_CLAUDE.md](결과_CLAUDE.md) — 이 차시에 쓰는 CLAUDE.md 전체(프로젝트 규칙). 실습 폴더에 `CLAUDE.md`로 복사합니다.
