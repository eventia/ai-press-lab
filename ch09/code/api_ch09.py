# 9차시 실제 API 호출 스크립트 — 문체 통일 후 3단계 검수를 하고 최종본·검수결과를 저장한다 (비용 발생, 2회)
import json
import sys

sys.path.insert(0, ".")
from mywork.review import check_formatting_errors, cross_check_all_numbers, review_press_release
from mywork.write import assemble_full_text, unify_style

DATA_PATH = "mywork/press_data.json"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

최종본 = unify_style(assemble_full_text(data))
print("[최종본]")
print(최종본)
검수결과 = {
    "표기오류검사": check_formatting_errors(최종본),
    "수치교차검증": cross_check_all_numbers(최종본, data),
    "AI감수지적사항": review_press_release(최종본, data),
}
print("[검수결과]")
print(json.dumps(검수결과, ensure_ascii=False, indent=2))

# 검수결과는 통과 여부와 관계없이 함께 저장해 사람이 판단하게 한다
data["최종본"], data["검수결과"] = 최종본, 검수결과
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
자동통과 = not 검수결과["표기오류검사"] and 검수결과["수치교차검증"]["통과"]
print("자동 검수:", "통과" if 자동통과 else "재검토 필요", f"— 최종본·검수결과 저장({DATA_PATH})")
