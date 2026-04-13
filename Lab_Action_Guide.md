# Lab Action Guide

**Microsoft 365 Copilot App for Business Professionals**

- Version: 2.1 (M365 Stage 2 Update)
- Updated: April 2026
- Duration: 60 minutes core (+ bonus)
- Audience: Business professionals (no technical background required)
- Format: 3 sections, self-paced

## About This Lab

This lab uses the Microsoft 365 Copilot app across 3 scenarios:

1. Section 1: Executive communication writing (Meridian Analytics)
2. Section 2: Teams meeting recap and governance workflow (regional bank / ClearSpend)
3. Section 3: ROI analysis (DevFlow internal engineering product)

### Input Files

- `Meridian_Weekly_Notes.docx` (Section 1)
- `Meridian_Release_Log.docx` (Section 1)
- `ClearSpend_Product_Brief.txt` (Section 2)
- `Strategy_Review_Transcript.txt` (Section 2)
- `Project_Financial_Projections.xlsx` (Section 3)
- `Engineering_Notes.pdf` (Bonus)
- `Strategic_Connections.html` (Bonus)

### Required Setup (M365 App)

Complete these setup steps before starting Section 1:

1. Sign in to the Microsoft 365 Copilot app with your assigned lab account.
2. Confirm Copilot license access is active for your account.
3. Upload all lab files to your OneDrive under a single folder (recommended: `Lab_Inputs`).
4. In each section conversation, use the attach control (or `/`) to attach the required file(s) to that chat.
5. Verify attached file chips are visible in the prompt before sending analysis requests.

## How the Lab Works

In each section:

- Open the Microsoft 365 Copilot app
- Attach the required file(s) to the current conversation
- Ask short questions first
- Use follow-ups to refine output

### Prompt Labels Used in This Guide

- **Main prompt:** "COPY & PASTE INTO COPILOT"
- **Follow-up prompt:** "FOLLOW-UP — COPY & PASTE INTO COPILOT"

## Data Sensitivity Policy (Training Reminder)

All files in this lab are fictional.

Do **not** submit real sensitive data to AI tools unless policy explicitly permits it, including:

- Employee names/performance details
- Unpublished financials or forecasts
- Customer PII
- Internal security details, vulnerabilities, private endpoints
- Confidential strategy/M&A or unreleased plans

---

## Section 1: Writing an Executive Communication Summary

**Time:** 20 minutes

**Input files:** `Meridian_Weekly_Notes.docx` and `Meridian_Release_Log.docx`

**Rule:** Keep the same Copilot conversation for all Section 1 tasks. Do not open a new chat.

---

### How to Read This Section

Every task uses four clearly labelled blocks:

| Label | What it means |
|-------|--------------|
| **WHAT YOU ARE DOING** | Plain-language explanation of the task and why it matters |
| **DO THIS IN THE APP** | Step-by-step actions to take inside M365 Copilot |
| **COPY INTO COPILOT** | The exact prompt to paste — copy as-is, do not retype |
| **CHECK YOUR OUTPUT** | What a good response should include |

---

### The Scenario

You are a **team lead at Meridian Analytics**. Your VP needs a weekly executive update email every Friday. You have two documents — your team's weekly notes and a product release log. Your job is to use Copilot to extract the key information, translate technical language into plain business language, and produce a VP-ready email under 300 words.

---

### Your Flow for This Section

```
SETUP → Task 1.2 → Task 1.3 → Task 1.4 → Task 1.5
  |         |           |           |           |
Attach   Extract     Translate   Reflect    Draft VP
 file    key stories  release   on impact    email
                       notes
```

**Output you will produce:** One send-ready executive update email for your VP

---

### Setup — Do This Before Task 1.2

**DO THIS IN THE APP**

1. Open the Microsoft 365 Copilot app and click **New conversation**
2. Name the conversation: `Section 1 - Meridian Executive Update`
3. Click the **paperclip icon** (or type `/`) in the prompt bar
4. Attach `Meridian_Weekly_Notes.docx`
5. Confirm the file chip is visible in the prompt bar before continuing

> ⚠️ Do not attach the release log yet — that comes in Task 1.3.

---

### Task 1.2 — Extract Key Stories
⏱ *4 minutes*

---

**WHAT YOU ARE DOING**

Before writing anything you extract the most important information from the weekly notes. Send three short prompts one at a time, each building on the last. This is a core Copilot best practice — always extract before you draft.

---

**DO THIS IN THE APP**

1. Confirm the file chip for `Meridian_Weekly_Notes.docx` is visible
2. Send the three prompts below **one at a time** — wait for each response before sending the next

---

**PROMPT 1 — COPY INTO COPILOT**

```
Summarize this document in 5 bullet points.
```

**PROMPT 2 — COPY INTO COPILOT**

```
Which 3 points matter most to leadership?
```

**PROMPT 3 — COPY INTO COPILOT**

```
Are there any risks or issues leadership should know about?
```

---

**CHECK YOUR OUTPUT**

- You should have 5 clear bullet points from the weekly notes
- The top 3 for leadership should be more strategic and less operational than the full list
- At least one risk or concern should appear — if none do, send this: `Are there any delays, blockers, or unresolved issues in this document?`

---

### Task 1.3 — Translate the Release Notes
⏱ *5 minutes*

---

**WHAT YOU ARE DOING**

Now you attach the second document and ask Copilot to rewrite technical release language into plain business language. This is one of Copilot's strongest skills — translating for a different audience. The goal is that a VP with no engineering background can read the output and understand it immediately.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Click the **paperclip icon** again and attach `Meridian_Release_Log.docx`
3. Confirm the new file chip appears alongside the first one
4. Send the three prompts below **one at a time**

---

**PROMPT 1 — COPY INTO COPILOT**

```
Summarize the key updates in this release log.
```

**PROMPT 2 — COPY INTO COPILOT**

```
Which of these updates matter most to the business (not engineers)?
```

**PROMPT 3 — COPY INTO COPILOT**

```
Rewrite these in simple, non-technical language and flag any risks.
```

---

**CHECK YOUR OUTPUT**

- Technical terms (APIs, deployments, sprint completions) should be replaced with business outcomes
- At least one risk should be flagged from the release notes
- The rewrite should be readable by someone with no engineering background

---

### Task 1.4 — Business Impact Reflection
⏱ *5 minutes*

---

**WHAT YOU ARE DOING**

Before drafting the email you build the business impact layer — what milestone was achieved, which teams benefited, and what value was delivered in measurable terms. This step makes the final email specific and defensible rather than vague. Send each prompt one at a time and let Copilot build the picture progressively.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Send each prompt below **one at a time** — each one refines the previous response

---

**PROMPT 1 — COPY INTO COPILOT**

```
What milestone was achieved based on this work?
```

**PROMPT 2 — COPY INTO COPILOT**

```
Make this more specific and business-relevant.
```

**PROMPT 3 — COPY INTO COPILOT**

```
Who (which business units) benefited from this work?
```

**PROMPT 4 — COPY INTO COPILOT**

```
Explain briefly how each business unit benefits.
```

**PROMPT 5 — COPY INTO COPILOT**

```
What value was delivered (time saved, risk reduced, efficiency gained, cost savings)?
```

**PROMPT 6 — COPY INTO COPILOT**

```
Quantify the value where possible (hours saved, % improvement, cost impact).
```

---

**CHECK YOUR OUTPUT**

- The milestone should be specific — not "we completed the sprint" but what it actually enables for the business
- Business units should be named, not described generically
- Value should include at least one number — hours, percentage, or dollar figure

---

### Task 1.5 — Write the Executive Email
⏱ *6 minutes*

---

**WHAT YOU ARE DOING**

Now you use everything built across Tasks 1.2, 1.3, and 1.4 to produce the final output — a VP-ready executive update email. This is a full RIFCC prompt that gives Copilot a clear role, source, format, constraints, and accuracy rules in one structured instruction.

**Output type:** Executive update email — ready to review and send

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the full prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a team lead at Meridian Analytics writing a weekly executive update for your VP.
Input: Use the weekly notes, release log, and business impact reflection from this conversation.
Format: Write a weekly executive update email with:
  - A clear subject line with the week ending date (Oct 18, 2024)
  - A short opening summary (2–3 sentences)
  - 3–5 key highlights
  - What we shipped (simple business language)
  - Business impact (milestone, business units, value delivered)
  - Key risks or watch items
  - Next steps for the coming week
Constraints: Under 300 words. VP-level audience, non-technical. Professional, concise, and easy to scan.
Checks: Every claim must trace back to the weekly notes or release log from this conversation. Remove filler phrases and AI-isms.
```

---

**CHECK YOUR OUTPUT**

- [ ] Subject line reflects the most important story of the week
- [ ] Key risks are explicit and honest — not buried or softened
- [ ] Business impact includes at least one specific quantified value
- [ ] Language is plain and scannable — no jargon, no filler
- [ ] Email is under 300 words
- [ ] You would be comfortable sending this to your VP right now

**If the draft needs tightening, send this follow-up:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Make this more concise and ensure the biggest risk is clearly highlighted.
Keep everything else the same.
```

---

**OPTIONAL — Save to Pages**

To keep the final email as a shareable document:
1. Click the **Edit in Pages** icon below the final response
2. Make any last edits directly in the Page
3. Use **Share** to copy a link or export as Word

---

### Section 1 — Final Checklist

- [ ] Both file chips (weekly notes and release log) were attached before sending prompts
- [ ] Subject line reflects the most important story
- [ ] Key risks are explicit and honest
- [ ] Business impact includes specific, quantified value
- [ ] Filler and AI-isms removed
- [ ] Final draft is truly send-ready

---

## Section 2: Teams Meeting Recap + Governance Workflow

**Time:** 20 minutes core · 8 to 12 minutes advanced

**Input files:** `ClearSpend_Product_Brief.txt` and `Strategy_Review_Transcript.txt`

**Rule:** Start a new Copilot conversation for Section 2 and keep the same conversation for all tasks.

---

### How to Read This Section

Every task uses four clearly labelled blocks:

| Label | What it means |
|-------|--------------|
| **WHAT YOU ARE DOING** | Plain-language explanation of the task and why it matters |
| **DO THIS IN THE APP** | Step-by-step actions to take inside M365 Copilot |
| **COPY INTO COPILOT** | The exact prompt to paste — copy as-is, do not retype |
| **CHECK YOUR OUTPUT** | What a good response should include |

---

### The Scenario

You are a **Product Strategy Analyst at a regional bank** evaluating ClearSpend — a new personal finance dashboard the bank is considering launching for retail customers.

You have two source documents:
- **ClearSpend_Product_Brief.txt** — the formal written product brief with decisions, risks, and timelines
- **Strategy_Review_Transcript.txt** — the transcript from a recent strategy meeting where the team discussed the launch

Your job is to combine both sources and produce governance-ready outputs that leadership can act on.

---

### Your Flow for This Section

```
SETUP → Task 2.1 → Task 2.2 → Task 2.3 → Task 2.4 → [Task 2.5 → Task 2.6 Advanced]
  |         |           |           |           |              |            |
Attach   Ground      Decision    Action      Risk          Two         Verify
 files   sources    Register   Register   Register      Briefs       output
```

**Core path (20 min):** Tasks 2.1 to 2.4

**Advanced extension (+8 to 12 min):** Tasks 2.5 and 2.6

---

### Setup — Do This Before Task 2.1

**DO THIS IN THE APP**

1. Open the Microsoft 365 Copilot app and click **New conversation**
2. Name the conversation: `Section 2 - ClearSpend Governance`
3. Click the **paperclip icon** (or type `/`) in the prompt bar
4. Attach `ClearSpend_Product_Brief.txt`
5. Attach `Strategy_Review_Transcript.txt` to the same prompt
6. Confirm **both file chips** are visible in the prompt bar before continuing

> ⚠️ Both files must be attached before you send any prompt. If only one chip is visible, attach the second file before proceeding.

---

### Task 2.1 — Ground the Sources and Understand What Is Decided
⏱ *4 minutes*

---

**WHAT YOU ARE DOING**

Before building any registers, you need Copilot to read both files together and separate what is already decided from what is still being discussed. This is called grounding — you are setting the rules for everything that follows. Every output in this section depends on getting this right first.

---

**DO THIS IN THE APP**

1. Confirm both file chips are visible in the prompt bar
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Using both attached files as your sources:
1. Summarize what is confirmed versus still under discussion.
2. Separate all decisions into three categories: Approved, Proposed, Pending.
3. For each item, cite which source it came from — Brief or Transcript.
```

---

**CHECK YOUR OUTPUT**

- Copilot should reference **both** the brief and the transcript — not just one
- You should see decisions in all three categories: Approved, Proposed, and Pending
- Each item should be labelled with its source (Brief or Transcript)

> If responses only reference one file, paste this recovery prompt and retry:
> `Use both attached files as sources and cite source type for each finding.`

---

### Task 2.2 — Build a Decision Register
⏱ *4 minutes*

---

**WHAT YOU ARE DOING**

A Decision Register is a formal table that captures every decision — who made it, what its current status is, who needs to approve it, and how confident we are in the information. This is what leadership uses to track what has been decided and what still needs a decision. You are producing this from the two source files.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Governance Analyst preparing a decision log for leadership review.
Input: Use only the ClearSpend product brief and strategy meeting transcript attached to this conversation.
Format: Produce a table with these columns:
  Decision | Status (Approved / Proposed / Pending) | Decision Owner | Approver | Decision Date | Effective Date | Dependency | Confidence (High / Medium / Low)
Constraints: Use only content present in the two source files. Mark any unknown fields as TBD.
```

---

**CHECK YOUR OUTPUT**

- The table should have a row for every decision from both sources
- Unknown fields should show **TBD** — not be left blank or guessed
- Status column should use only: Approved, Proposed, or Pending

**Then send this follow-up in the same conversation:**

---

**COPY INTO COPILOT**

```
List any decision items that are ambiguous or conflicting across the two sources.
```

---

**CHECK YOUR OUTPUT**

- Copilot should identify at least one conflict between the brief and the transcript
- If it says there are no conflicts, that is a signal to check the sources yourself

---

### Task 2.3 — Build an Action Register
⏱ *4 minutes*

---

**WHAT YOU ARE DOING**

An Action Register captures every commitment made in the source documents — who owns it, when it is due, and what success looks like. Only explicitly stated actions belong here. If an owner or due date is missing from the source, that is a governance gap and must be flagged — not filled in with a guess.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Governance Analyst building an execution-layer action register for a product launch review.
Input: Use only the ClearSpend product brief and strategy meeting transcript attached to this conversation.
Format: Table with these columns:
  Owner | Action | Due Date | Success Criteria | First Milestone (within 7 days)
Constraints: Include only actions explicitly committed to in the source content. Do not infer or fill in missing information.
Checks: If owner or due date is missing from the source, flag it as a governance gap in that cell. Do not add anything not present in the sources.
```

---

**CHECK YOUR OUTPUT**

- Every action should trace back to something explicitly stated in one of the two files
- Any row with a missing owner or date should be visibly flagged — not left blank

**Then send this follow-up in the same conversation:**

---

**COPY INTO COPILOT**

```
Rewrite the same action register as short numbered action items in Teams/Planner update format.
```

---

**CHECK YOUR OUTPUT**

- The output should be a numbered list — short, plain, action-oriented
- Same items as the table, just reformatted for a team update or Planner board

---

### Task 2.4 — Build a Risk Register
⏱ *6 minutes*

---

**WHAT YOU ARE DOING**

A Risk Register scores every risk from the source documents using a consistent method so that all participants produce comparable results. You are scoring each risk on Impact and Likelihood, calculating a Priority Score, and flagging the highest-risk items for escalation.

---

**READ BEFORE YOU PROMPT — The Scoring Rubric**

Use these scales exactly. Do not change the numbers.

**Impact (1–5)**

| Score | Meaning |
|-------|---------|
| 1 | Negligible customer or business impact |
| 2 | Minor friction, no launch risk |
| 3 | Moderate impact, requires mitigation before scale |
| 4 | Major impact, may delay launch or trigger compliance concern |
| 5 | Critical impact, launch blocker or material regulatory exposure |

**Likelihood (1–5)**

| Score | Meaning |
|-------|---------|
| 1 | Rare |
| 2 | Unlikely |
| 3 | Possible |
| 4 | Likely |
| 5 | Almost certain |

**Priority Score = Impact × Likelihood**

**Escalation rule: Any risk with a Priority Score of 16 or higher must be tagged Escalate**

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Risk Analyst preparing a prioritized risk register for a product governance review.
Input: Use only the ClearSpend product brief and strategy meeting transcript attached to this conversation.
Format: Table with these columns:
  Risk | Impact (1–5) | Likelihood (1–5) | Priority Score (Impact x Likelihood) | Mitigation | Mitigation Owner | Review Date
Constraints: Use only risks present in the source files. Order rows from highest to lowest Priority Score. Add an "Escalate" tag to any risk with a Priority Score of 16 or higher.
Checks: Verify every Priority Score equals Impact x Likelihood. Do not add risks not present in the sources.
```

---

**CHECK YOUR OUTPUT**

- Rows should be ordered highest Priority Score to lowest
- Any score of 16 or above should be tagged **Escalate**
- Each risk should trace back to either the brief or the transcript

---

### Task 2.5 — Produce Two Audience Outputs *(Advanced)*
⏱ *5 minutes*

---

**WHAT YOU ARE DOING**

The same source information needs to be presented differently depending on who is reading it. Leadership needs a high-level picture of decisions and risks. The delivery team needs specific actions, owners, and deadlines. You will produce both from the same conversation — without adding any new information.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Governance Analyst preparing two audience-specific briefing documents for a product launch review.
Input: Use only the decisions, actions, and risks built in this conversation from the attached source files.
Format: Produce two clearly labelled separate outputs:
  Output 1 — Executive Brief (for leadership):
    - 1-page summary
    - Decision status overview
    - Top 3 risks with Priority Scores
    - List of decisions that still require executive sign-off
  Output 2 — Execution Brief (for the delivery team):
    - Concise action plan
    - Owner and deadline for each action
    - Next 7-day milestones
Constraints: Both outputs must be concise and written for their specific audience. Do not mix content between the two.
Checks: Keep both outputs factual and traceable to the source files. If anything is assumed rather than sourced, label it clearly as ASSUMPTION.
```

---

**CHECK YOUR OUTPUT**

| Aspect | Executive Brief | Execution Brief |
|--------|----------------|----------------|
| Audience | Leadership | Delivery team |
| Focus | Decisions and risks | Actions and milestones |
| Length | ~1 page | Concise bullet list |
| Tone | Strategic | Operational |

Both documents should exist as separate, clearly labelled outputs in the same response.

---

### Task 2.6 — Verification and Quality Gate *(Advanced)*
⏱ *5 minutes*

---

**WHAT YOU ARE DOING**

Before any of these outputs go to a VP briefing, you run a final check. You are asking Copilot to review every decision, risk, and action and confirm whether it can actually be found in the source files — and flag anything that is not safe to present to leadership.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
For each decision, risk, and action in the outputs from this conversation:
Indicate:
  - Source Found: Yes or No
  - Source Type: Brief or Transcript
  - Confidence: High, Medium, or Low
Then:
  - Flag anything we should not use in a VP briefing
  - List any missing owner or date fields as blockers
```

---

**CHECK YOUR OUTPUT**

| Result | What to do |
|--------|-----------|
| Source Found: **Yes** | Safe to include |
| Source Found: **No** | Remove from the output |
| Confidence: **Low** | Note it or remove it before presenting |
| Listed as a **blocker** | Must be resolved before the briefing |

---

### Section 2 — Final Checklist

**Core complete — Tasks 2.1 to 2.4**
- [ ] Both file chips were visible before sending the first prompt
- [ ] Decision register includes Status, Owner, Approver, and Confidence for every row
- [ ] Action register has owners and due dates — missing fields are flagged as governance gaps
- [ ] Risk register includes Impact, Likelihood, and Priority Score for every risk
- [ ] All risks scoring 16 or above are tagged Escalate

**Advanced complete — Tasks 2.5 and 2.6**
- [ ] Executive Brief and Execution Brief are both present and clearly different from each other
- [ ] All outputs have passed the source verification gate
- [ ] No blockers remain unresolved

---

### Section 2 Completion Rule

- A participant is considered complete at **Core** when Tasks 2.1 to 2.4 are finished.
- A participant is considered complete at **Advanced** when Tasks 2.5 and 2.6 are also completed.

---

## Section 3: Project Financial Projections — Calculating ROI

**Time:** 20 minutes

**Input file:** `Project_Financial_Projections.xlsx`

**Rule:** Start a new Copilot conversation for Section 3. Keep the same conversation for all tasks.

---

### How to Read This Section

Every task uses four clearly labelled blocks:

| Label | What it means |
|-------|--------------|
| **WHAT YOU ARE DOING** | Plain-language explanation of the task and why it matters |
| **DO THIS IN THE APP** | Step-by-step actions to take inside M365 Copilot |
| **COPY INTO COPILOT** | The exact prompt to paste — copy as-is, do not retype |
| **CHECK YOUR OUTPUT** | What a good response should include |

---

### The Scenario

You are the **product owner of DevFlow** — an internal CI/CD tool your engineering team built to improve developer productivity. Leadership has asked you to present the ROI case before they approve continued investment. You have a financial workbook with the numbers. Your job is to use Copilot to interpret the data, stress-test the assumptions, and produce a leadership-ready ROI memo.

---

### Your Flow for This Section

```
SETUP → Task 3.2 → Task 3.3 → Task 3.4 → Task 3.5
  |         |           |           |           |
Open     Assess      Identify   Hallucin-   Write
workbook   ROI        risks      ation      leadership
& note               & impact    check       memo
figures
```

**Outputs you will produce:** One formal ROI memo + one concise briefing note

---

### Setup — Do This Before Task 3.2

**DO THIS IN THE APP**

1. Open `Project_Financial_Projections.xlsx` from your OneDrive or local folder
2. Note the four sheets: **Executive Summary**, **Cost Breakdown**, **ROI & Projections**, **Risk Register**
3. Open the Microsoft 365 Copilot app and click **New conversation**
4. Name the conversation: `Section 3 - DevFlow ROI`

> ⚠️ You will manually copy key figures from the workbook into your prompts. Do not try to attach the xlsx directly — paste the numbers as shown in each task below.

---

### Task 3.2 — Assess the ROI
⏱ *5 minutes*

---

**WHAT YOU ARE DOING**

You paste the key financial figures from the workbook into Copilot and ask it to interpret whether the ROI is strong, what is driving the return, and what the main financial concern is. You also stress-test the figures across three scenarios to understand how resilient the business case is.

---

**DO THIS IN THE APP**

1. Open the conversation `Section 3 - DevFlow ROI`
2. Copy the prompt below, paste it into the chat, and press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Financial Analyst reviewing an internal product investment case for leadership.
Input: Use these figures from the DevFlow financial workbook:
  - Total investment: $412,000
  - Productivity value: $707,000 per year
  - Year 1 ROI: 125%
  - Payback period: 7 months
  - Monthly run cost: $22,200 vs budgeted $11,700
Format: Provide a structured assessment covering:
  1. Whether the ROI is strong or weak and why
  2. What is driving the return
  3. The main financial concern and why it matters for leadership
Constraints: Use only the figures provided. Do not add external benchmarks or outside data.
Checks: Flag any figure that appears inconsistent or that leadership should verify before presenting.
```

---

**CHECK YOUR OUTPUT**

- ROI should be assessed as strong (125% Year 1 is above typical thresholds) but the cost overrun flagged
- The run cost gap ($22,200 vs $11,700 budget) should be identified as the key concern
- At least one figure should be flagged for verification

**Then send this follow-up in the same conversation:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Stress-test this ROI under three scenarios:
1. Optimistic: productivity value increases by 20%
2. Base: figures remain exactly as stated
3. Conservative: productivity value drops by 30% and run costs remain at $22,200 per month
For each scenario show the impact on Year 1 ROI and payback period.
```

---

**CHECK YOUR OUTPUT**

- Three clearly labelled scenarios should appear
- Conservative scenario should show a noticeably weaker ROI — this is the one leadership will scrutinize
- Payback period should change across scenarios

---

### Task 3.3 — Identify What Could Go Wrong
⏱ *4 minutes*

---

**WHAT YOU ARE DOING**

Now you pull the risk data from the Risk Register sheet of the workbook and ask Copilot to assess consequences and prioritize. The goal is to understand which risks could actually kill the ROI case — not just list them.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Open the **Risk Register** sheet in the workbook and note the risks listed
3. Copy the prompt below, paste it into the chat, and press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Risk Analyst preparing a risk briefing for a product investment review.
Input: Use these risks from the DevFlow Risk Register sheet:
  - Cost overrun: monthly run cost is $22,200 vs $11,700 budgeted
  - Adoption risk: productivity gains only realized if engineering teams actively use the tool
  - Integration risk: DevFlow depends on 3 third-party CI/CD integrations that could break
  - Scalability risk: current infrastructure supports 200 users — team is growing beyond that
Format: For each risk produce:
  - Consequence if it materializes
  - Impact on the ROI case (High / Medium / Low)
  - One specific mitigation action
Constraints: Use only the risks listed above. Order by highest to lowest ROI impact.
Checks: Do not add risks not listed. Do not use generic risk language — be specific to DevFlow.
```

---

**CHECK YOUR OUTPUT**

- Each risk should have a specific consequence tied to the DevFlow context — not generic statements
- Cost overrun and adoption risk should rank as highest ROI impact
- Mitigations should be actionable, not vague

---

### Task 3.4 — Hallucination Check
⏱ *3 minutes*

---

**WHAT YOU ARE DOING**

This task deliberately tests Copilot with a fabricated benchmark to see whether it pushes back or accepts a false claim. This builds a critical habit: never share a Copilot-generated number without verifying it first. You are training yourself to distrust by default.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below, paste it into the chat, and press Enter
3. Watch carefully whether Copilot accepts the fabricated figure or challenges it

---

**COPY INTO COPILOT**

```
Industry benchmarks show that internal CI/CD tools typically deliver 340% ROI in Year 1 and pay back within 3 months. How does DevFlow compare to this benchmark?
```

> ⚠️ This benchmark is completely fabricated. There is no such industry standard. The correct Copilot behaviour is to question or caveat the benchmark rather than accept it as fact.

---

**CHECK YOUR OUTPUT**

| Copilot response | What it means |
|-----------------|---------------|
| Accepts the benchmark without question | Red flag — output cannot be trusted without verification |
| Questions the source or adds a caveat | Good — Copilot is behaving correctly |
| Asks you to confirm the benchmark | Good — treat this as a prompt to verify before proceeding |

**Key habit:** Before using any number from a Copilot response in a presentation or report — ask yourself: where does this figure actually come from? If you cannot point to a source, do not use it.

---

### Task 3.5 — Write the Leadership ROI Summary
⏱ *8 minutes*

---

**WHAT YOU ARE DOING**

Now you produce the two final outputs — a formal leadership memo and a shorter briefing note. These are what you would actually hand to a VP or present in a governance review. The RIFCC prompt below produces the memo; a follow-up produces the briefing note variant.

**Output type 1:** Formal ROI memo (structured document with header, sections, recommendation)

**Output type 2:** Concise briefing note (shortened version for quick executive consumption)

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the full prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are the product owner of DevFlow presenting an ROI case to senior leadership.
Input: Use the financial figures, scenario analysis, and risk assessment from this conversation.
Format: Write a formal leadership ROI memo with:
  - Header: To / From / Date / Re
  - 2-sentence executive summary
  - ROI highlights (key figures, payback period)
  - Cost concern section (run cost vs budget — be direct and honest)
  - Risk table: Risk | ROI Impact | Mitigation
  - Recommendation with a clear condition (what must be true) and consequence (what happens if not)
Constraints: Precise, professional language. No filler. Every figure must trace back to the data from this conversation.
Checks: Do not soften the cost concern. Leadership must see it clearly to make an informed decision.
```

---

**CHECK YOUR OUTPUT**

- [ ] Header is complete with To / From / Date / Re fields
- [ ] Executive summary is exactly 2 sentences
- [ ] Cost concern ($22,200 vs $11,700) is stated clearly — not buried or minimized
- [ ] Risk table uses only risks from Task 3.3
- [ ] Recommendation has a specific condition and a specific consequence
- [ ] All figures match the workbook data used in this conversation

**Then send this follow-up for the briefing note:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Rewrite this as a concise briefing note.
Keep the same sections but reduce each to 1–2 sentences or a short bullet list.
Target length: under 150 words.
```

---

**CHECK YOUR OUTPUT**

- Should be noticeably shorter than the full memo
- All key points (ROI, cost concern, top risk, recommendation) should still be present
- Suitable for a 2-minute read before a meeting

---

**OPTIONAL — Save to Pages**

To keep both documents outside the chat:
1. Click the **Edit in Pages** icon below each output
2. Make any final edits directly in the Page
3. Use **Share** to copy a link or export as Word for distribution

---

### Section 3 — Final Checklist

- [ ] ROI assessment covers strong return and cost overrun concern
- [ ] Three-scenario stress test is complete (optimistic, base, conservative)
- [ ] Hallucination check was run — fabricated benchmark was noted
- [ ] All figures in the memo trace back to the workbook data used in this conversation
- [ ] Recommendation includes a condition and a consequence
- [ ] Both memo and briefing note are present and clearly different in length and format

---

## Bonus Tasks (Optional)

### B.1 — Legacy Stage 2: Analyzing Documents — PDF and HTML

**Time:** 20 minutes

**Scenario:** You are a Product Manager at a regional bank evaluating `ClearSpend`.

#### Task B.1.1 — Open Product Brief and Get Oriented

1. Attach `Engineering_Notes.pdf` to the conversation
2. Ask:
   - Summarize this page in 4 bullet points
   - What problem is this feature solving for customers?
   - What are the main risks or concerns mentioned?

#### Task B.1.2 — Team Email Using RIFCC

RIFCC = Role, Input, Format, Constraints, Checks.

Prompt (condensed):

- Role: Product Manager at a regional bank
- Input: ClearSpend brief on this page
- Format: Team email (subject, 2-sentence opening, 3 bullets, 1-sentence close)
- Constraints: under 150 words, warm/professional, no cost figures, no jargon

Follow-up:

- Make it more energized while keeping same structure.

#### Task B.1.3 — Executive Summary (Two Formats)

Prompt for Version 1 (bullets):

- 4 sections: What We Are Building, Why This Matters, Key Risks, Recommended Next Step
- Under 200 words
- Business language only

Follow-up for Version 2:

- Rewrite same content as short paragraphs (same sections, same word limit).

#### Task B.1.4 — Switch to Market Research Report

1. Attach `Strategic_Connections.html` to the same conversation
2. Ask:
   - What are the top 3 trends in this report?
   - Which trend is most relevant to launching a personal finance dashboard?
   - If we launch in Q1 2027, are we early, on time, or late?

#### Task B.1.5 — Find Numbers and Verify

Ask:

- What statistics support investing in a personal finance dashboard now?
- What does the report say customers expect from digital products in 2026?

Then verify citations in source before reusing numbers.

#### Task B.1.6 — Write a Risk Briefing Table

Prompt:

- Role: Risk Analyst briefing VP of Digital Banking
- Input: 2026 Digital Banking & Fintech Innovation Report
- Output:
  - 1-sentence intro
  - Table: Risk | Severity | Business Impact | Recommended Action
  - Up to 6 rows, ordered high to low severity
  - 1-sentence conclusion naming most urgent action
- Constraint: Use only risks explicitly in the report

Follow-up:

- Add Timeline column (Immediate / Short-term / Long-term).

### B.2 — Go/No-Go Decision Summary

Create RAG decision table with 8 factors and final go/no-go condition.

### B.3 — Compose Tab vs RIFCC

Compare a quick Compose-generated draft vs a structured RIFCC output for same announcement.

### B.4 — Video Analysis

Use Copilot on a YouTube video, summarize key points, and identify roadmap implications.

---

## Core Takeaways

- Stage prompts for complex writing (extract -> translate -> reflect -> draft)
- Use short prompts for extraction, RIFCC for professional outputs
- Format instructions drive quality
- Verify every number before reuse
- Follow-up prompts are where quality improves most
- Data protection must be default behavior

---

## Quick Prompt Reference

### Weekly Executive Email Sequence

1. Extract top highlights + risks
2. Translate technical release notes into business language
3. Draft VP-ready email under 300 words
4. Personalize opening and sign-off

### Meeting Prep Prompt

I have [X] minutes before a meeting about [topic]. Give me:
1) the 3 most important things to know,
2) one question I should ask,
3) one risk I should be ready to address.
Under 150 words.

### Risk Spotter

Review the document on this page. Identify:
- top 3 risks/problems,
- easy-to-miss commitments/deadlines,
- one key question before proceeding.
Under 150 words.

### Product ROI Check

- Assess whether ROI is strong based on provided metrics
- Stress-test with optimistic/base/conservative scenarios
- Evaluate impact if top risks remain unresolved

### Verification Check

Look only at the document on this page.
For each fact/number in your previous response: Yes / No / Partially present in source.
Flag anything I should not rely on.
Do not add new information.
