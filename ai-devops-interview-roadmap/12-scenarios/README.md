# Production scenarios and troubleshooting

## Kubernetes Pod failure
```mermaid
flowchart TD
 A[Pod unhealthy] --> B{Status?}
 B -->|Pending| C[describe Pod and events]
 C --> D[Check scheduler, resources, PVC and taints]
 B -->|ImagePullBackOff| E[Check image tag, registry auth and network]
 B -->|CrashLoopBackOff| F[Check current and previous logs]
 F --> G[Check command, config, secrets, probes and dependencies]
 B -->|Running but unavailable| H[Check readiness, Service selector and endpoints]
 H --> I[Check Ingress, DNS, policy and app listener]
 D --> J[Fix and verify rollout]
 E --> J
 G --> J
 I --> J
```

## Incident response
```mermaid
flowchart TD
 A[Alert] --> B[Validate impact]
 B --> C[Declare incident and assign roles]
 C --> D[Stabilize: rollback, fail over or scale]
 D --> E[Verify service health]
 E --> F[Collect timeline and evidence]
 F --> G[Root cause analysis]
 G --> H[Prevent recurrence]
 H --> I[Blameless postmortem]
```

## Scenario checklist
- **Service has no endpoints:** compare Service selector with Pod labels, readiness and EndpointSlices.
- **Ingress returns 502:** inspect ingress controller, backend Service, endpoints, target port and app health.
- **Pipeline failed after dependency update:** inspect lockfile, cache, build logs, test results and dependency source.
- **Deployment caused production errors:** stop rollout, assess blast radius, rollback known-good immutable artifact, verify and communicate.
- **EKS nodes cannot join:** check IAM role, subnet routes, security groups, API endpoint reachability and bootstrap logs.

Always establish impact, stabilize safely, gather evidence, recover, validate, communicate and document prevention.
