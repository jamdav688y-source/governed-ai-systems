from pathlib import Path
import sys

gate_path = Path("doctrine/diagnostics/00-governance-gate.md")

required_sections = [
"## 1. System Name",
"## 2. Purpose and Scope",
"## 3. Decision Owner",
"## 4. Stop Authority",
"## 5. Rollback Viability",
"## 6. Evidence Path",
"## 7. Governance Classification",
"## 8. Approval Checklist",
]

if not gate_path.exists():
print("Missing governance gate file.")
sys.exit(1)

content = gate_path.read_text(encoding="utf-8")

missing = [section for section in required_sections if section not in content]

if missing:
print("Governance gate validation failed.")
for item in missing:
print(f"Missing section: {item}")
sys.exit(1)

print("Governance gate validation passed.")
