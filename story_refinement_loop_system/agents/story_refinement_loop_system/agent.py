"""Example 5.1 workflow: iterative story refinement with a loop agent."""

from google.adk.agents import Agent, LoopAgent, SequentialAgent
from google.adk.tools import FunctionTool


def exit_loop():
    """Terminate the refinement loop when the critic approves the story."""
    return {"status": "approved", "message": "Story approved. Exiting refinement loop."}


# Runs once to produce the initial draft from the user's prompt.
initial_writer_agent = Agent(
    name="InitialWriterAgent",
    model="gemini-2.5-flash-lite",
    instruction=(
        "Based on the user's prompt, write the first draft of a short story "
        "(around 100-150 words). Output only the story text."
    ),
    output_key="current_story",
)

# Provides feedback or an approval signal; no tools required.
critic_agent = Agent(
    name="CriticAgent",
    model="gemini-2.5-flash-lite",
    instruction=(
        "You are a constructive story critic. Review the story provided below.\n"
        "Story: {current_story}\n\n"
        "Evaluate the story's plot, characters, and pacing.\n"
        "- If the story is well-written and complete, respond with EXACTLY: APPROVED\n"
        "- Otherwise, provide 2-3 actionable suggestions for improvement."
    ),
    output_key="critique",
)

# Rewrites the story or exits the loop based on the critic's feedback.
refiner_agent = Agent(
    name="RefinerAgent",
    model="gemini-2.5-flash-lite",
    instruction=(
        "You are a story refiner. You have a story draft and critique.\n\n"
        "Story Draft: {current_story}\n"
        "Critique: {critique}\n\n"
        "If the critique is EXACTLY 'APPROVED', you MUST call the `exit_loop` tool "
        "and do nothing else. Otherwise, rewrite the story to fully incorporate "
        "the critic's feedback."
    ),
    output_key="current_story",
    tools=[FunctionTool(exit_loop)],
)

# Loop alternates Critic -> Refiner up to a maximum number of iterations.
story_refinement_loop = LoopAgent(
    name="StoryRefinementLoop",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=2,
)

# Overall workflow: initial draft then iterative refinement.
root_agent = SequentialAgent(
    name="StoryPipeline",
    sub_agents=[initial_writer_agent, story_refinement_loop],
)
