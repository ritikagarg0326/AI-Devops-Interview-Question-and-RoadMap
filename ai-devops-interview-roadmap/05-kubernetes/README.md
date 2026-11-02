# Kubernetes

## Core concepts
API server, etcd, scheduler, controller manager, kubelet, CNI, Pods, ReplicaSets, Deployments, StatefulSets, DaemonSets, Jobs, Services, Ingress, ConfigMaps, Secrets, PV/PVC, probes, resources, HPA, RBAC and NetworkPolicy.

## Commands and tools
`kubectl get`, `describe`, `logs`, `logs --previous`, `exec`, `events`, `top`, `rollout`, `scale`, `cordon`, `drain`, `uncordon`, `auth can-i`, `port-forward`.

## Interview questions
What happens after kubectl apply? How does a Service find Pods? Readiness vs liveness vs startup? Requests vs limits? How does HPA work? Secure a cluster?

## Hands-on lab
Deploy an app, expose it, configure probes and resource limits, then troubleshoot bad image, failing probe and missing selector.

## Answer framework
Use **Context → Explanation → Example → Trade-off → Validation**. For scenarios use **Impact → Evidence → Hypothesis → Test → Mitigation → Prevention**.
