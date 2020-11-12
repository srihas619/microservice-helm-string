# Helm-microservice-app
Helm chart to install a microservice-app with one service that serves a string and the other service that gets the string and serves the reverse of the same string.

## Install
1. Make sure minikube is up and running.
2. Make sure helm is configured to work with minikube.
3. (Optional) Create new namespace and set it in context in `~/.kube/config`
4. Execute `helm install ./chart` from root project directory
5. Check pods are running healthy by `kubectl --namespace=<namespace> get pods` where `namespace=default` if nothing is set in step 2.

## Usage
Follow the instructions that are displayed after step 4 above to get the URL and curl to the same to access the app.

## Customization
1. Inorder to run multiple instances of each service the value of `replicaCount` can be set accordingly in `./chart/values.yaml`.
2. If the application code inside `app-*` directories has been changed, please rebuild the respective image from Dockerfile via `docker build -t <repo>:<tag> .` and push to the repository. Change the `image` section in `values.yaml` with the info accordingly.
