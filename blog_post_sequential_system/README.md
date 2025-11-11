# Blog Post Sequential System

## 3.1 Example: Blog Post Creation with Sequential Agents

Let's build a system with three specialized agents:

- **Outline Agent** – Creates a blog outline for a given topic.
- **Writer Agent** – Writes a blog post that follows the outline.
- **Editor Agent** – Edits the blog draft for clarity and structure.

Companion project for **Example 3.1: Blog Post Creation with Sequential Agents** in `day-1b-agent-architectures.ipynb`. This mirrors the `simple-agent-with-google-adk` layout so you can run the outline → draft → edit workflow locally with `uv`.

## What’s inside
- `agents/blog_post_sequential_system/agent.py` – defines outline, writer, and editor agents plus a `SequentialAgent` pipeline.
- `pyproject.toml` – dependencies for `uv sync`.
- `.env.example` – template for Gemini credentials.

## Quick start
```bash
cd multi-agent-systems/blog_post_sequential_system
cp .env.example .env         # add your GOOGLE_API_KEY
uv sync                      # install deps
uv run adk web agents --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>, pick the `blog_post_sequential_system` agent, and give it a topic such as “benefits of AI pair programming.” The sequential pipeline will:
1. Outline the post structure with headline, intro, 3–5 sections, and a conclusion.
2. Draft a 200–300 word post that follows the outline.
3. Polish the draft for clarity and grammar before returning the final blog text.

## Customize it
- Update instructions or model names in `agent.py`.
- Inject additional steps by appending agents to the `SequentialAgent` list.
- Export intermediate outputs by supplying unique `output_key` values per agent.
