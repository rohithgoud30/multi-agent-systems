# Story Refinement Loop System

## 5.1 Example: Iterative Story Refinement

Let's build a system with two agents:

- **Writer Agent** – Writes a draft of a short story.
- **Critic Agent** – Reviews and critiques the story to suggest improvements.

This project mirrors the Example 5.1 loop workflow from `day-1b-agent-architectures.ipynb`. It ships as a uv-ready package so you can run the iterative writer/critic loop locally.

## Quick start
```bash
cd multi-agent-systems/story_refinement_loop_system
cp .env.example .env        # add your GOOGLE_API_KEY
uv sync                     # install deps
uv run adk web agents --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>, choose the `story_refinement_loop_system` agent, and provide a story seed like “Write about a time-traveling botanist.” The workflow will:
1. Generate the initial draft.
2. Enter a refinement loop where the critic reviews the draft and the refiner either rewrites it or exits when “APPROVED.”

## Customize it
- Tweak iteration limits or critique criteria in `agent.py`.
- Add extra review stages by appending more agents to the loop sequence.
- Replace the loop exit condition by editing the `exit_loop` helper or its instructions.
