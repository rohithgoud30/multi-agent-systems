# Parallel Multi-Topic Research System

## 4.1 Example: Parallel Multi-Topic Research

Let's build a system with four agents:

- **Tech Researcher** – Researches AI/ML news and trends.
- **Health Researcher** – Tracks medical breakthroughs and timelines.
- **Finance Researcher** – Covers fintech trends and market implications.
- **Aggregator Agent** – Combines the three reports into a single summary.

Companion project for **Example 4.1** in `day-1b-agent-architectures.ipynb`. This folder mirrors the other uv projects so you can run the parallel + sequential workflow locally.

## Quick start
```bash
cd multi-agent-systems/parallel_multi_topic_research
cp .env.example .env        # add your GOOGLE_API_KEY
uv sync                     # install deps
uv run adk web agents --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>, select the `parallel_multi_topic_research` agent, and run a prompt like “Daily briefing across tech, health, and finance.” The system will:
1. Run all three researcher agents concurrently via `ParallelAgent`.
2. Feed their outputs into the aggregator agent to craft a ~200-word executive summary.

## Customize it
- Adjust each research instruction or add more domain agents in `agent.py`.
- Swap `google_search` for other tools to integrate custom data.
- Extend the sequential workflow (e.g., add a final QA step) by appending agents to the root sequence.
