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

**Scenario:** You are a team lead at Meridian Analytics. Your VP needs a weekly executive update email.

**Important:** Keep the same Copilot conversation across all Section 1 tasks.

### Task 1.1 — Set Up Input Files

1. Start a new Copilot conversation for Section 1.
2. Attach `Meridian_Weekly_Notes.docx` to the conversation.

### Task 1.2 — Extract Key Stories

Use these prompts:

- Summarize this document in 5 bullet points.
- Which 3 points matter most to leadership?
- Are there any risks or issues leadership should know about?

### Task 1.3 — Translate the Release Notes

1. Attach `Meridian_Release_Log.docx` in the same conversation
2. Continue in the same conversation

Prompts:

- Summarize the key updates in this release log.
- Which of these updates matter most to the business (not engineers)?
- Rewrite these in simple, non-technical language and flag any risks.

### Task 1.4 — Business Impact Reflection

Continue in the same conversation.

Prompts:

- What milestone was achieved based on this work?
- Make this more specific and business-relevant.
- Who (which business units) benefited from this work?
- Explain briefly how each business unit benefits.
- What value was delivered (time saved, risk reduced, efficiency gained, cost savings)?
- Quantify the value where possible (hours saved, % improvement, cost impact).

### Task 1.5 — Write the Executive Email

Prompt:

Using the insights from the weekly notes, release log, and the business impact reflection we just completed, write a weekly executive update email.
Include:
- A clear subject line with the week ending date (Oct 18, 2024)
- A short opening summary (2-3 sentences)
- 3-5 key highlights
- What we shipped (simple business language)
- Business impact (milestone, business units, value delivered)
- Key risks or watch items
- Next steps for the coming week
Audience: VP-level, non-technical
Tone: Professional, concise, easy to scan
Length: Under 300 words

Optional follow-up:

- Make this more concise and ensure the biggest risk is clearly highlighted.

### Section 1 Checks

- Subject line reflects the most important story
- Key risks are explicit and honest
- Business impact includes specific, quantified value
- Filler/AI-isms removed
- Final draft is truly send-ready

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

**Scenario:** You own DevFlow (internal CI/CD product) and must present ROI to leadership.

**Important:** Start a **new Copilot conversation** for Section 3.

### Task 3.1 — Open ROI Workbook

Open `Project_Financial_Projections.xlsx` and copy the key figures into Copilot prompts for analysis.

Sheets:

- Executive Summary
- Cost Breakdown
- ROI & Projections
- Risk Register

### Task 3.2 — Assess ROI

Use provided figures to ask Copilot for interpretation, risk impact, and scenario reasoning.

Key sample values in guide:

- Total investment: $412,000
- Productivity value: $707,000/year
- Year 1 ROI: 125%
- Payback: 7 months
- Monthly run cost: $22,200 vs $11,700 budget

### Task 3.3 — Identify What Could Go Wrong

Use risk data and ask Copilot for consequence analysis and prioritization.

### Task 3.4 — Verification Test (Hallucination Check)

Run a deliberate fabricated benchmark prompt to test if Copilot pushes back.

Goal: build a verification habit before sharing any Copilot-generated number.

### Task 3.5 — Write Engineering ROI Summary

Generate a formal leadership summary including:

- Header (To/From/Date/Re)
- 2-sentence executive summary
- ROI highlights
- Cost concerns
- Risk table
- Recommendation with condition and consequence

Then produce a concise briefing-note variant.

### Section 3 Checks

- All figures trace to source data
- Recommendation matches risk reality
- Wording is precise and defensible

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
