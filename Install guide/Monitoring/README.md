# Monitoring

## Prometheus
```sh
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
Verify with: helm repo list
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
Verify with: kubectl get pods -n monitoring
```

Make Prometheus scrape GPU data
-------------------------------
```sh
kubectl logs -n gpu-operator nvidia-dcgm-exporter-s872m
kubectl describe pod nvidia-dcgm-exporter-s872m -n gpu-operator
check namespace: helm list -A
get the name of prometheus: kubectl get prometheus -n monitoring
```

open file
---------
```sh
kubectl get prometheus prometheus-kube-prometheus-prometheus -n monitoring -o yaml
set servicemonitoring to allow all namespaces:   serviceMonitorNamespaceSelector: {}
check "release" on "servicemonitorselector" is set to "prometheus" (in the file)
```

find or create servicemonitor file
----------------------------------
```sh
kubectl get servicemonitors -A
look at dcgm, if there is none (we did not have one), create a file (see below).
nano dcgm-servicemonitor.yaml 
in file, change namespace to SAME as dcgm's namespace ("gpu-operator" in this case)
make sure "release", "app" and "port" names are correct.
1. release: kubectl get prometheus -n monitoring -- show-labels (check "release" under the labels header)
2. app: kubectl get svc -n gpu-operator --show-labels (check "app" under "label"-header)
3. port: kubectl get svc nvidia-dcgm-exporter -n gpu-operator -o yaml (check spec->ports->name)
apply the file: kubectl apply -f dcgm-servicemonitor.yaml
```

enter the webinterface to check everything works well
-----------------------------------------------------
```sh
check port: kubectl get svc -n monitoring (the namespace)
```
enter following in broswer: *ip*:*port*/targets

## Grafana
```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
Verify with: helm repo list
helm install grafana grafana/grafana --namespace monitoring --create-namespace
verify with: kubectl get pods -n monitoring
```

Öppna tjänst för lokalt nät
---------------------------
Se port för webinterfacet: "kubectl get svc -n monitoring" (namespace)

Grafana
-------
```sh
kubectl get svc grafana -n monitoring
kubectl edit svc grafana -n monitoring
Ändra type från clusterIP till NodePort
```

Prometheus
----------
```sh
kubectl expose svc prometheus-operated --type=NodePort --name=prometheus-ui -n monitoring
```