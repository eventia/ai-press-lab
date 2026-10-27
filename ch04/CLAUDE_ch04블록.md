<!-- quick-practice:ch04:start -->
## 4차시 규칙 — Claude API 호출과 요약
- Claude API 호출은 `mywork/write.py`의 `call_claude` 한 곳을 거친다. `load_dotenv()`는 `anthropic.Anthropic()`보다 먼저 호출한다.
- 모델은 `MODEL_NAME = "claude-sonnet-5-5"`, `thinking={"type": "between_tools"}`를 쓰고 `temperature`는 넣지 않는다.
- 응답은 `content`에서 `type == "text"`인 블록만 모아 쓴다. `stop_reason`이 "refusal"이면 예외를 낸다.
- 프롬프트에 넣는 숫자는 콤마·단위를 붙인 표기로 넣고, 감소는 abs()로 부호를 떼어 "감소"로 쓴다.
- 결과는 JSON으로 요청하고 `parse_json_response`로 파싱한다. 생성된 문장의 숫자는 `verify_numbers`로 검증한다.
<!-- quick-practice:ch04:end -->
