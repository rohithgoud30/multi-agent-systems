# Research & Summarization System

Companion project for the **Example 2.1: Research & Summarization System** section in `day-1b-agent-architectures.ipynb`. It mirrors the `simple-agent-with-google-adk` layout so you can run a multi-agent workflow locally with `uv`.

## What you get
- `agents/research_summarization_system/agent.py` – defines a research agent, a summarizer agent, and a coordinator agent that chains them together via `AgentTool`.
- `pyproject.toml` – minimal dependencies to run with `uv`.
- `.env.example` – template for your Gemini API key.

## Quick start
```bash
cd multi-agent-systems/research_summarization_system
cp .env.example .env        # drop your GOOGLE_API_KEY inside
uv sync                     # install deps
uv run adk web agents --host 127.0.0.1 --port 8000
```

Then visit <http://127.0.0.1:8000>, select the `research_summarization_system` agent, and ask a question like “What do the latest AI chips mean for robotics?”. The coordinator will:
1. Call the research agent, which must use `google_search` to gather 2–3 cited facts.
2. Pass those findings to the summarizer agent, which emits a 3–5 bullet recap.

## Customizing
- Tune instructions or model names inside `agents/research_summarization_system/agent.py`.
- Extend the tool list on `research_agent` if you want additional data sources.
- Add more workflow steps by appending extra `AgentTool(...)` entries to `root_agent`.

This folder stays self-contained, so you can create additional multi-agent workflows alongside it by adding more subdirectories under `agents/`.
