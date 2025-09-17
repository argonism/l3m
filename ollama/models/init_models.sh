#!/bin/sh
set -e

echo "Creating models via Ollama daemon..."

ollama pull gpt-oss:20b
ollama create sarashina-3b -f /ollama/models/Modelfile.sarashina-3b
ollama pull qwen3:8b

echo "All custom models created successfully."
