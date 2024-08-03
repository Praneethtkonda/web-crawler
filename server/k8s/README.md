# Kubernetes setup

```bash
minikube start
kubectl create secret generic ghcr-secret \
  --from-file=.dockerconfigjson=config.json \
  --type=kubernetes.io/dockerconfigjson
kubectl apply -f ./server/k8s/
kubectl get pods
```