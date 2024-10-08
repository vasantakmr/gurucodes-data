---
title: "kubernetes commands"
---

### 50 KUBERNETES COMMANDS

1. **kubectl version**
    
Display the Kubernetes client and server version.

kubectl version

2. **kubectl cluster-info**

Display cluster information, including the master and services.

kubectl cluster-info

3. **kubectl get nodes**
    
List all nodes in the cluster.

kubectl get nodes

4. **kubectl get pods**

List all pods in the default namespace.

kubectl get pods

5. **kubectl get deployments**
    
List all deployments in the default namespace.

kubectl get deployments

6. **kubectl describe pod podname**
    
Display detailed information about a specific pod.

kubectl describe pod mypod

7. **kubectl logs pod_name**
    
Display the logs of a specific pod.

kubectl logs mypod

8. **kubectl exec -it podname -- /bin/sh**
    
Start an interactive shell in a specific pod.

kubectl exec -it mypod -- /bin/sh

9. **kubectl create deployment name --image=imagename**

Create a deployment with a specified container image.

kubectl create deployment myapp --image=myimage:tag

10. **kubectl expose deployment name --port=port --type=LoadBalancer**
    
Expose a deployment as a service.

kubectl expose deployment myapp --port=80 --type=LoadBalancer

11. **kubectl scale deployment name --replicas=replicacount**

Scale the number of replicas for a deployment.

kubectl scale deployment myapp --replicas=3

12. **kubectl get svc**
    
List all services in the default namespace.

kubectl get svc

13. **kubectl delete pod podname**
    
Delete a specific pod.

kubectl delete pod mypod

14. **kubectl delete deployment name**
    
Delete a deployment and its associated pods.

kubectl delete deployment myapp

15. **kubectl apply -f file**
    
Apply a configuration file to the cluster.

kubectl apply -f myconfig.yaml

16. **kubectl get configmaps**
    
List all ConfigMaps in the default namespace.

kubectl get configmaps

17. **kubectl describe service servicename**
    
Display detailed information about a specific service.

kubectl describe service myservice

18. **kubectl get namespaces**

List all namespaces in the cluster.

kubectl get namespaces

19. **kubectl create namespace namespacename**
    
Create a new namespace.

kubectl create namespace mynamespace

20. **kubectl get pods -n namespace**
    
List all pods in a specific namespace

kubectl get pods -n mynamespace

21. **kubectl delete namespace namespacename**
    
Delete a namespace and all its resources.

kubectl delete namespace mynamespace

22. **kubectl get services --sort-by=.metadata.name**

List services and sort them by name.

kubectl get services --sort-by=.metadata.name

23. **kubectl rollout status deployment deploymentname**
    
Check the status of a deployment rollout.

kubectl rollout status deployment myapp

24. **kubectl get pods --field-selector=status.phase=Running**
    
List pods that are in the Running phase.

kubectl get pods --field-selector=status.phase=Running

25. **kubectl get events --sort-by=.metadata.creationTimestamp**

List events sorted by creation timestamp.

kubectl get events --sort-by=.metadata.creationTimestamp

26. **kubectl create secret generic secretname --from-literal=key=value**
    
Create a generic secret from literal values.

kubectl create secret generic mysecret --from-literal=username=admin -- from-literal=password=pass123

27. **kubectl describe secret secretname**

Display detailed information about a specific secret.

kubectl describe secret mysecret

28. **kubectl edit deployment deploymentname**

Edit the YAML of a deployment interactively.

kubectl edit deployment myapp

29. **kubectl get pods -o wide**

List pods with additional details like node information.

kubectl get pods -o wide

30. **kubectl get nodes -o custom- columns=NODE:.metadata.name,IP:.status.addresses[0].address**
    
        List nodes with custom output columns.
        
        kubectl get nodes -o custom- columns=NODE:.metadata.name,IP:.status.addresses[0].address
{/*
31. **kubectl top pods**
    
            Display resource usage (CPU and memory) of pods.

            kubectl top pods

32. **kubectl apply -f** **https://url-to-yaml-file**
    
            Apply a configuration file directly from a URL.

            kubectl apply -f https://raw.githubusercontent.com/example/myconfig.yaml

33. **kubectl get pods --selector=labelkey=labelvalue**
    
            List pods with a specific label.
        
            kubectl get pods --selector=app=myapp

34. **kubectl get pods --field-selector=status.phase!=Running**

            List pods that are not in the Running phase.

            kubectl get pods --field-selector=status.phase!=Running

35. **kubectl rollout undo deployment deploymentname**

            Rollback a deployment to the previous version.

            kubectl rollout undo deployment myapp

36. **kubectl label pod podname labelkey=labelvalue**

            Add a label to a specific pod.

            kubectl label pod mypod environment=production

37. **kubectl get componentstatuses**
    
            List the health of different cluster components.
        
            kubectl get componentstatuses

38. **kubectl describe node nodename**
    
            Display detailed information about a specific node.

            kubectl describe node mynode

39. **kubectl rollout history deployment deploymentname**
    
            View the rollout history of a deployment.

            kubectl rollout history deployment myapp

40. **kubectl delete pod --selector=labelkey=labelvalue**
    
        Delete pods with a specific label.
        
        kubectl delete pod --selector=app=myapp

41. **kubectl top nodes**
    
            Display resource usage (CPU and memory) of nodes.

            kubectl top nodes

42. **kubectl get pods --watch**
    
            Watch for changes to pods in real-time.

            kubectl get pods –watch

43. **kubectl rollout pause deployment deploymentname**
    
            Pause a deployment to prevent further rollouts.
        
            kubectl rollout pause deployment myapp

44. **kubectl rollout resume deployment deploymentname**
    
            Resume a paused deployment.

            kubectl rollout resume deployment myapp

45. **kubectl explain resource**
    
            Get information about a Kubernetes resource.

            kubectl explain pod

46. **kubectl get pods -o jsonpath='{.items[*].metadata.name}'**
    
            Extract specific information using JSONPath.

            kubectl get pods -o jsonpath='{.items[*].metadata.name}'

47. **kubectl apply --dry-run=client -f file**
    
            Dry run to validate a configuration file without applying it.

            kubectl apply --dry-run=client -f myconfig.yaml

48. **kubectl exec -it podname -- /bin/sh -c 'command'**

            Execute a command in a specific pod.
        
            kubectl exec -it mypod -- /bin/sh -c 'ls /app'

49. **kubectl get events --sort-by=.metadata.creationTimestamp -n namespace**
    
            List events sorted by creation timestamp in a specific namespace.

            kubectl get events --sort-by=.metadata.creationTimestamp -n mynamespace 

50. **kubectl get secrets**

            List all secrets in the default namespace.
        
            kubectl get secrets
 
 */}