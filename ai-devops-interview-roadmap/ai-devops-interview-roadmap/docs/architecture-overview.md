# AI platform architecture

```mermaid
flowchart LR
 U[Candidate] --> UI[React UI]
 UI --> API[FastAPI]
 API --> AUTH[Auth and session layer]
 API --> ORCH[Agent orchestrator]
 ORCH --> PLAN[Planner agent]
 ORCH --> Q[Question generator]
 ORCH --> INT[Interviewer agent]
 ORCH --> EVAL[Evaluator agent]
 ORCH --> COACH[Coach agent]
 ORCH --> RET[Retrieval agent]
 RET --> KB[(Reviewed question bank)]
 ORCH --> DB[(PostgreSQL)]
 ORCH --> LLM[LLM provider adapter]
 API --> OBS[Logs, metrics, traces]
```

## Interview sequence
```mermaid
sequenceDiagram
 participant C as Candidate
 participant UI as Web UI
 participant API as FastAPI
 participant O as Orchestrator
 participant Q as Question agent
 participant E as Evaluator
 C->>UI: Choose role, topic and level
 UI->>API: Start session
 API->>O: Validate context
 O->>Q: Generate/retrieve question
 Q-->>O: Question and rubric
 O-->>UI: Show question
 C->>UI: Submit answer
 UI->>API: Answer payload
 API->>O: Evaluate
 O->>E: Score against rubric
 E-->>O: Feedback and follow-up
 O-->>UI: Results
```

Keep the orchestrator in control. Validate structured outputs. Retrieve reviewed material before generating. Persist evidence and scores. Never expose provider keys in the frontend.
