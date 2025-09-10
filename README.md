# L3M Gateways

# Get started

Before running components, make sure creating a external network for docker compose:

```shell
docker network create llmnet
```

You can access llm models from any containers within the same network.

Then, you can start ollama server first:


```
docker compose up -d ollama
# if you want to pull models beforehand, run following commands (models to install can be configed in ollama/models/init_models.sh):
# docker compose run --rm ollama-init
docker compose up -d litellm prometheus grafana
```

Now, you can access llm models at `http://localhost:4000`, or `http://litellm:4000` from other containers within the same network.

# Example: accessing models from n8n

Here, we gonna show how to access llm models from n8n hosted in another container.

```shell
docker compose -f docker-compose.n8n.yaml up -d
```
