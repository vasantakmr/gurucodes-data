---
title: "kubernetes Resources:A to Z of KIND"
---

### Prerequisite: Kubernetes cluster setup

Creating First Pod in the Kubernetes using the YAML file.

YAML File.
A YAML file is a plain text file that stores data in a human-readable format that can be used by various programming languages. YAML stands for "YAML Ain't Markup Language" or "Yet Another Markup Language", and it's a recursive acronym that emphasizes that YAML is for data, not documents

YAML file contain the element like:
apiVersion: A key-value pair that indicates the API version
kind: A key-value pair that indicates the kind of object, which is "pod" in this case

metadata: Includes the name, labels, and annotations for the deployment
spec: Defines the desired state of the deployment,
including the pod template, number of replicas, and other specifications

Step 1: Create .yaml file vi pod.yml


Step 2: Write a file with image as nginx and port number 80.

```apiVersion: v1
kind: Pod
metadata:
  name: static-web
  labels:
    class: mynginx
spec:
  containers:
    - name: web
      image: nginx
      ports:
        - name: web
          containerPort: 80
          protocol: TCP
```

Step 3: Create a pod using yaml file

```kubectl apply -f pod1.yml```

Step 4: Check pod is created.

```kubectl get pod```

Step 5: To get the more detail of pod use -o wide.

```kubectl get pod -o wide```

Step 6: Access the container.

```kubectl exect -it nginx /bin/bash```

Step 7: We can get pod using the labels also, that we define in metadata.

```kubectl get pod -l class=mynginx```

Step 9: Delete pod command.

```kubectl delete -f pod.yml```

