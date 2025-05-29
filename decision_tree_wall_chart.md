 # AI Chatbot Decision Tree for HNW Banking

 This one-page ASCII chart guides senior leaders through key decisions when implementing an AI chatbot for high-net-worth (HNW) client agents. Print it out and refer to it in workshops and planning sessions.

```
START -> 1) Org & Business Readiness? -> 2) Compliance & Security? -> 3) Known & Predictable Questions? -> 4) Harm/Off-limits? -> 5) Tone/Persona? -> 6) Multi-step/Stateful? -> 7) Human-in-the-Loop? -> 8) Pilot & Continuous Improvement
```

Step Details:

1) Org & Business Readiness? (true gate)
   - No: Workshop to define business case, KPIs & org-change plan
   - Yes: Proceed to step 2

2) Compliance & Security? (true gate)
   - No: Conduct privacy/security impact, regulatory & legal reviews
   - Yes: Proceed to step 3

<techstack>

Steps 3–7 (the “tech stack” and guardrail design) can overlap heavily:

  - While you’re defining your Known vs. Unknown flows (3), you can already be working on alert-word lists and moderation policies (4).
  - Designing your persona prompts (5) can happen in parallel with sketching out your memory/state model (6).
  - Confidence thresholds and handover SLAs (7) can be drafted alongside your fallback-to-human logic for free-form responses.

3) Known & Predictable Questions?
   - Yes:
     a) Sensitive/Brand-Critical?
        - Yes: Intent Tables + Preset Topics + RAG
        - No: Buttons / Suggestion Chips
   - No:
     b) Absolute Factual Accuracy Required?
        - Yes: RAG (Retrieve + ground answers in internal docs)
        - No: Free-form GPT responses + human fallback

4) Harm/Off-limits?
   - Yes: Alert Words + Moderation layer
   - No: Light guardrails & tone guidance

5) Tone/Persona?
   - Yes: Custom prompts with persona & examples
   - No: Neutral tone + standard guardrails

6) Multi-step/Stateful?
   - Yes: Memory handling or scripted chaining
   - No: Stateless Q&A
</techstack>


7) Human-in-the-Loop?
   - Define confidence thresholds & handover SLAs
   - Agent handover training & escalation path


Step 8 (Pilot & CI) is both an “end” and a new “beginning”: once you launch a pilot you’ll immediately collect data that may send you back into Steps 3–7 to adjust intents, guardrails, persona tone or handover thresholds.
    
8) Pilot & Continuous Improvement
   - Launch pilot cohort
   - Dashboards (CSAT, fallback rates, error trends)
   - Regular review cadence, retraining & scaling

Legend:
- Intent Tables: Maps user intents (e.g. “update address”) to approved scripts.
- Preset Topics: Fixed menu items (e.g. “Wealth Review,” “Tax Planning”).
- RAG: Retrieval-Augmented Generation – grounds answers in your internal knowledge base.
- Buttons / Suggestion Chips: Quick UI replies steering conversation.
- Alert Words / Moderation: Filters for harmful or sensitive content.
- Guardrails: Confidence thresholds & fallback rules for human handover.
- Memory Handling: Session state for multi-step flows.
- Pilot & CI: Dashboards, regular reviews, retraining, and scale.