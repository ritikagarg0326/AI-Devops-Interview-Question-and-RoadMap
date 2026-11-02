# AI DevOps Interview Roadmap

A learning repository and AI interview-coach starter for DevOps, Cloud and SRE roles (weighted toward 2–5 years' experience).

## Included
- 30-day and 60-day roadmaps
- Topic-wise notes, interview questions and practical labs
- Mermaid flowcharts for learning, incident response, Kubernetes debugging and AI-agent orchestration
- AI-agent architecture, roles, prompts, guardrails and evaluation plan
- FastAPI backend starter with mock mode and tests
- React frontend implementation blueprint
- JSON sample question bank, progress tracker and contribution guide

## Start here
1. Read `00-roadmap/learning-path.md`.
2. Follow `00-roadmap/30-day-plan.md`.
3. Study topic folders in order.
4. Practise scenarios in `12-scenarios/`.
5. Explore `ai-platform/` for the AI application scaffold.

## Run the API
```bash
cd ai-platform/backend
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`. Mock mode works without an API key.

Run tests with `pytest`.

## Important
This is a learning scaffold, not a production-ready autonomous agent. AI-generated technical answers need review. Never allow agents to execute commands against production infrastructure. Keep future tools read-only, sandboxed, permissioned and audited.
