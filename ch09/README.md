# 9차시 — 문체 통일·검수·AI 감수

## 1. 프롬프트 (`prompts/`)

Claude Code에 **그대로 붙여넣어** 코드를 직접 만들어 봅니다. 위에서부터 순서대로 씁니다.

| 파일 | 하는 일 |
| --- | --- |
| [프롬프트A.txt](prompts/프롬프트A.txt) | 모듈 만들기 (mywork/) |
| [프롬프트C.txt](prompts/프롬프트C.txt) | 관찰 실험 스크립트 만들기 (obs_chNN.py) |
| [프롬프트D.txt](prompts/프롬프트D.txt) | 실제 API 호출 스크립트 만들기 (api_chNN.py, API 키 필요) |
| [수정요청예시.txt](prompts/수정요청예시.txt) | 결과가 기대와 다를 때 오류 메시지를 붙여 수정 요청 |

## 2. 기준 검증 (`check/`)

프롬프트로 만든 코드가 강의 내용대로 동작하는지 정답과 대조합니다. **검증 코드는 Claude Code에게 만들게 하거나 고치게 하지 않습니다**(코드와 테스트를 같은 AI가 만들면 서로 맞춰 버릴 수 있음).

1. [check/check.py](check/check.py)를 실습 폴더 **바로 아래**에 `check.py`로 저장합니다(`mywork` 안이 아님).
2. `python check.py`를 실행합니다.
3. 마지막 줄에 `Ch09 OK`가 나오면 통과입니다. 출력은 [check/기대결과.txt](check/기대결과.txt)와 비교합니다.
4. `AssertionError`가 나오면 그 메시지를 [prompts/수정요청예시.txt](prompts/수정요청예시.txt)처럼 붙여 Claude Code에 수정을 요청합니다.

> 검증은 가짜 응답을 쓰므로 실제 API를 부르지 않습니다(비용 0, API 키 불필요).

## 3. CLAUDE.md

- [CLAUDE_ch09블록.md](CLAUDE_ch09블록.md) — 이번 차시 규칙. 실습 폴더의 `CLAUDE.md` **맨 아래에 이어 붙인 뒤** Claude Code를 새로 시작합니다.
- [결과_CLAUDE.md](결과_CLAUDE.md) — 9차시를 마쳤을 때의 CLAUDE.md 전체(비교·복구용).

## 4. 강사 코드 (`code/`) — 정답 코드

강사가 위 프롬프트로 만든 코드입니다. **9차시를 마친 시점의 프로젝트 상태** 그대로이므로, 직접 만든 코드가 동작하지 않을 때 내려받아 실습 폴더에 덮어쓰거나, 다음 차시를 이 상태에서 시작할 수 있습니다.

| 파일 | 설명 |
| --- | --- |
| `mywork/__init__.py` | 빈 파일(패키지 표시) |
| `mywork/charts.py` | 앞 차시에서 만든 파일 |
| `mywork/clean.py` | 앞 차시에서 만든 파일 |
| `mywork/config.py` | 앞 차시에서 만든 파일 |
| `mywork/data_io.py` | 앞 차시에서 만든 파일 |
| `mywork/nlp.py` | 앞 차시에서 만든 파일 |
| `mywork/press_data.json` | 9차시를 마친 시점의 표준 데이터 |
| `mywork/review.py` | **9차시에 만들거나 고친 파일** |
| `mywork/stats.py` | 앞 차시에서 만든 파일 |
| `mywork/write.py` | **9차시에 만들거나 고친 파일** |
| `api_ch09.py` | 프롬프트로 만든 스크립트 — 실습 폴더 바로 아래에 둡니다 |
| `obs_ch09.py` | 프롬프트로 만든 스크립트 — 실습 폴더 바로 아래에 둡니다 |

**쓰는 법** (실습 폴더에서, 가상환경을 켠 상태)

```powershell
# 내려받은 ch09\code 폴더의 내용을 실습 폴더로 복사 (경로는 내려받은 위치로 바꾸세요)
Copy-Item <내려받은 위치>\ch09\code\* . -Recurse -Force
python obs_ch09.py
```

> 실제 API를 부르는 코드는 실습 폴더의 `.env`에 `ANTHROPIC_API_KEY`가 있어야 합니다(저장소 루트의 `.env.example` 참고).

> 생성형 AI가 만든 코드는 실행할 때마다 조금씩 다를 수 있습니다. 내 코드가 강사 코드와 모양이 달라도, 같은 입력에 같은 결과를 내면 됩니다.
