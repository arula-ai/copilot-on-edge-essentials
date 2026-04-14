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

Each section follows the same four-step pattern:

1. **Attach** the required file(s) to the Copilot conversation
2. **Read** the task — understand what you are producing and why
3. **Copy** the structured prompt and paste it into Copilot as-is
4. **Check** your output against the criteria listed

Every prompt in this lab uses the **RIFCC framework** — Role, Input, Format, Constraints, Checks. You do not need to learn the framework to use this lab; just copy and paste the prompts as written. The framework is explained wherever it first appears.

### Prompt Labels Used in This Guide

- **Main prompt:** "COPY INTO COPILOT"
- **Follow-up prompt:** "FOLLOW-UP — COPY INTO COPILOT"

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

| Step | Task | What You Do |
|------|------|-------------|
| Setup | — | Attach `Meridian_Weekly_Notes.docx` |
| 1 | Task 1.1 | Extract key stories from weekly notes |
| 2 | Task 1.2 | Attach release log and translate to business language |
| 3 | Task 1.3 | Reflect on business impact and quantify value |
| 4 | Task 1.4 | Draft VP-ready executive email |
| 5 | Task 1.5 | Save output to Pages and export as Word |

**Output you will produce:** One send-ready executive update email for your VP

---

### Setup — Do This Before Task 1.1

**DO THIS IN THE APP**

1. Open the Microsoft 365 Copilot app and click **New conversation**
2. Name the conversation: `Section 1 - Meridian Executive Update`
3. Click the **paperclip icon** (or type `/`) in the prompt bar
4. Attach `Meridian_Weekly_Notes.docx`
5. Confirm the file chip is visible in the prompt bar before continuing

> **IMPORTANT:** Do not attach the release log yet — that comes in Task 1.2.

---

### Task 1.1 — Extract Key Stories
*Time: 4 minutes*

---

**WHAT YOU ARE DOING**

Before writing anything you extract the most important information from the weekly notes. One structured prompt asks Copilot for all three things at once — a full summary, the leadership priorities, and any risks — returned in clearly labelled sections you can use directly in the email draft.

---

**DO THIS IN THE APP**

1. Confirm the file chip for `Meridian_Weekly_Notes.docx` is visible
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a team lead at Meridian Analytics preparing a weekly executive update.
Input: Use only the attached Meridian_Weekly_Notes.docx.
Format: Respond in three clearly labelled sections:
  Section 1 — Full Summary: Summarize the document in 5 bullet points
  Section 2 — Leadership Priorities: List the 3 points that matter most to leadership, with one sentence explaining why each matters
  Section 3 — Risks and Issues: List any risks, blockers, or concerns leadership should know about
Constraints: Use only content present in the document. Do not add assumptions or outside context.
Checks: If no risks are found, explicitly state "No risks identified in this document" in Section 3.
```

---

**CHECK YOUR OUTPUT**

- Section 1 should have exactly 5 bullet points
- Section 2 priorities should be more strategic than the full summary — not just the first 3 bullets repeated
- Section 3 should surface at least one risk or concern — if it states none, check the document yourself before moving on

---

### Task 1.2 — Translate the Release Notes
*Time: 5 minutes*

---

**WHAT YOU ARE DOING**

Now you attach the second document and ask Copilot to summarize, assess business relevance, and rewrite the release notes into plain business language — all in one structured prompt. One send gives you three clearly labelled sections you can use directly when drafting the email.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Click the **paperclip icon** again and attach `Meridian_Release_Log.docx`
3. Confirm the new file chip appears alongside the first one
4. Copy the prompt below and paste it into the chat
5. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a team lead at Meridian Analytics reviewing a product release log for a VP executive update.
Input: Use only the attached Meridian_Release_Log.docx.
Format: Respond in three clearly labelled sections:
  Section 1 — Release Summary: List the key updates from this release log
  Section 2 — Business Relevance: Identify which updates matter most to the business (not engineers) and briefly explain the business impact of each
  Section 3 — Plain Language Rewrite: Rewrite the key updates in simple, non-technical language. Flag any risks at the end of this section.
Constraints: No technical jargon in Section 3. Use only content present in the release log.
Checks: Every item in Sections 2 and 3 must trace back to Section 1. If no risks are found, state "No risks identified" — do not leave Section 3 incomplete.
```

---

**CHECK YOUR OUTPUT**

- Section 1 should list all key updates from the log — nothing invented
- Section 2 should explain business impact in terms a VP would care about — not engineering outcomes
- Section 3 language should be readable by someone with no technical background
- At least one risk should be flagged — if none appear, check the release log yourself before moving on

---

### Task 1.3 — Business Impact Reflection
*Time: 5 minutes*

---

**WHAT YOU ARE DOING**

Before drafting the email you build the business impact layer — what milestone was achieved, which teams benefited, and what value was delivered in measurable terms. One structured prompt asks for all three things at once, returning a ready-to-use impact summary that feeds directly into Task 1.5.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a team lead at Meridian Analytics building the business impact section of a VP executive update.
Input: Use the weekly notes and release log from this conversation.
Format: Respond in three clearly labelled sections:
  Section 1 — Milestone: What milestone was achieved? Be specific about what was delivered and what it enables for the business — not just "we completed the sprint."
  Section 2 — Business Units: Which business units benefited from this work? For each one, explain in one sentence how they specifically benefit.
  Section 3 — Value Delivered: What value was delivered in terms of time saved, risk reduced, efficiency gained, or cost savings? Quantify each item where possible using hours, percentages, or dollar figures.
Constraints: Use only content from the weekly notes and release log in this conversation. Do not estimate or assume figures not present in the sources.
Checks: Section 3 must include at least one quantified value. If a figure cannot be sourced from the documents, state that explicitly rather than inventing a number.
```

---

**CHECK YOUR OUTPUT**

- Section 1 milestone should be specific and business-relevant — tied to a real outcome, not a process step
- Section 2 should name actual business units — not "stakeholders" or "teams" generically
- Section 3 should include at least one number — if Copilot cannot find one, that is a gap to note before drafting the email

---

### Task 1.4 — Write the Executive Email
*Time: 6 minutes*

---

**WHAT YOU ARE DOING**

Now you use everything built across Tasks 1.1, 1.2, and 1.3 to produce the final output — a VP-ready executive update email. This is a full RIFCC prompt that gives Copilot a clear role, source, format, constraints, and accuracy rules in one structured instruction.

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
Format: Write a weekly executive update email with clearly labelled sections:
  - Subject: [subject line with week ending date Oct 18, 2024]
  - Opening: short summary (2–3 sentences)
  - Key Highlights: 3–5 bullet points
  - What We Shipped: simple business language
  - Business Impact: milestone, business units, value delivered
  - Risks and Watch Items: key concerns for the VP
  - Next Steps: actions for the coming week
Constraints: Under 300 words. VP-level audience, non-technical. Professional, concise, and easy to scan. Use the section labels above as headings so the output is structured and document-ready.
Checks: Every claim must trace back to the weekly notes or release log from this conversation. Remove filler phrases and AI-isms. This output will be saved as a Word document — ensure it is clean and well-formatted.
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

### Task 1.5 — Save Your Output as a Document
*Time: 2 minutes*

---

**WHAT YOU ARE DOING**

You are saving the final executive email out of the chat window and into a permanent document. Copilot chat responses disappear when the session closes — Pages keeps the output as a real shareable file. You will then export it as a Word document so it can be emailed, stored, or edited in Word.

**Output document:** `Meridian_Executive_Update_Week_Oct18.docx`

---

**DO THIS IN THE APP**

1. Find the final version of the executive email in your conversation
2. Click the **Edit in Pages** icon below the response (small document icon)
3. The email opens as an editable Page — make any final wording adjustments here
4. Rename the Page: type `Meridian Executive Update — Week Ending Oct 18 2024` at the top
5. Click the **three-dot menu (...)** in the top right of the Page
6. Select **Export to Word**
7. Save the downloaded `.docx` file to your OneDrive `Lab_Inputs` folder

---

**CHECK YOUR OUTPUT**

- [ ] The Page opened correctly and the email text is fully editable
- [ ] The Page title reflects the week ending date
- [ ] The Word export downloaded successfully
- [ ] The `.docx` file opens cleanly with the full email content

---

### Section 1 — Final Checklist

- [ ] Both file chips (weekly notes and release log) were attached before sending prompts
- [ ] Subject line reflects the most important story
- [ ] Key risks are explicit and honest
- [ ] Business impact includes specific, quantified value
- [ ] Filler and AI-isms removed
- [ ] Final draft is truly send-ready
- [ ] Output saved to Pages and exported as Word (.docx)

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

| Step | Task | What You Do |
|------|------|-------------|
| Setup | — | Attach both source files |
| 1 | Task 2.1 | Ground sources — confirmed vs pending decisions |
| 2 | Task 2.2 | Build Decision Register |
| 3 | Task 2.3 | Build Action Register |
| 4 | Task 2.4 | Build Risk Register with priority scores |
| 5 *(Advanced)* | Task 2.5 | Produce Executive Brief and Execution Brief |
| 6 *(Advanced)* | Task 2.6 | Run verification and quality gate |
| 7 | Task 2.7 | Compile all outputs and save as Word document |

**Core path (20 min):** Tasks 2.1 to 2.4 and Task 2.7

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

> **IMPORTANT:** Both files must be attached before you send any prompt. If only one chip is visible, attach the second file before proceeding.

---

### Task 2.1 — Ground the Sources and Understand What Is Decided
*Time: 4 minutes*

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
Role: You are a Product Strategy Analyst at a regional bank preparing for a governance review of the ClearSpend product launch.
Input: Use both attached files — ClearSpend_Product_Brief.txt and Strategy_Review_Transcript.txt.
Format: Respond in three clearly labelled sections:
  Section 1 — Confirmed: Items that are fully decided and agreed across both sources
  Section 2 — Under Discussion: Items that are proposed, debated, or not yet resolved
  Section 3 — Decision Status: A categorized list of all decisions as Approved, Proposed, or Pending — with the source cited (Brief or Transcript) for each item
Constraints: Use only content present in the two attached files. Do not infer or assume anything not stated.
Checks: Every item must be attributed to its source. If an item appears in both sources, cite both.
```

---

**CHECK YOUR OUTPUT**

- Copilot should reference **both** files — not just one
- All three decision categories should appear: Approved, Proposed, and Pending
- Every item should show its source — Brief, Transcript, or Both

> If Copilot only references one file, paste this and retry:
> `Use both attached files as sources and cite source type for each finding.`

---

### Task 2.2 — Build a Decision Register
*Time: 4 minutes*

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
*Time: 4 minutes*

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
*Time: 6 minutes*

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
*Time: 5 minutes*

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
*Time: 5 minutes*

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
Role: You are a Product Governance Analyst running a final quality check before a VP briefing.
Input: Use all decisions, risks, and actions produced in this conversation.
Format: Produce a verification table with these columns:
  Item | Source Found (Yes / No) | Source Type (Brief / Transcript / Both) | Confidence (High / Medium / Low)
Then provide two clearly labelled lists below the table:
  VP Briefing Flags: anything that should not be presented without further verification
  Blockers: missing owner or date fields that must be resolved before the briefing
Constraints: Review only outputs from this conversation. Do not add new information.
Checks: Every item must have all four columns completed. No field should be left blank.
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

### Task 2.7 — Compile and Save Your Governance Package
*Time: 4 minutes*

---

**WHAT YOU ARE DOING**

Across Tasks 2.1 to 2.6 you have built multiple separate outputs — registers, briefs, and a verification report. Before saving, you ask Copilot to compile all of them into one structured governance document. You then save that single document to Pages and export it as a Word file that can be shared with leadership or stored on SharePoint.

**Output document:** One complete governance package containing all registers and briefs

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Compile all outputs from this conversation into a single governance package document.
Structure it as follows:

Title: ClearSpend Governance Package
Prepared: [today's date]
Sources: ClearSpend Product Brief + Strategy Review Transcript

Use these clearly labelled bold headings for each section in this order:
  1. Decision Register
  2. Action Register
  3. Risk Register
  4. Executive Brief (include only if produced in this conversation)
  5. Execution Brief (include only if produced in this conversation)
  6. Verification Summary (include only if produced in this conversation)

Rules:
- Do not add any new information — use only what was produced in this conversation
- Use proper headings, tables, and spacing so the document is clean and readable when exported to Word
- This will be saved as a Word document and shared with leadership — format it accordingly
```

---

**CHECK YOUR OUTPUT**

- All sections should be present and clearly labelled
- No new information should appear — only what was built in Tasks 2.1–2.6
- The cover line should be at the top with the correct sources cited

**Then save it:**

---

**DO THIS IN THE APP**

1. Click the **Edit in Pages** icon below the compiled governance package response
2. The full package opens as an editable Page
3. Rename the Page at the top: `ClearSpend Governance Package — April 2026`
4. Make any final edits or formatting adjustments directly in the Page
5. Click the **three-dot menu (...)** in the top right of the Page
6. Select **Export to Word**
7. Save the downloaded `.docx` file to your OneDrive `Lab_Inputs` folder

---

**CHECK YOUR OUTPUT**

- [ ] The Page contains all registers and briefs in clearly labelled sections
- [ ] Page title shows `ClearSpend Governance Package — April 2026`
- [ ] Word export downloaded successfully
- [ ] The `.docx` opens cleanly with all sections intact

---

### Section 2 Completion Rule

- A participant is considered complete at **Core** when Tasks 2.1 to 2.4 and Task 2.7 are finished.
- A participant is considered complete at **Advanced** when Tasks 2.5, 2.6, and 2.7 are also completed.

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

| Step | Task | What You Do |
|------|------|-------------|
| Setup | — | Open workbook and note key figures |
| 1 | Task 3.1 | Assess ROI and stress-test with three scenarios |
| 2 | Task 3.2 | Identify risks and consequence impact |
| 3 | Task 3.3 | Run hallucination check with fabricated benchmark |
| 4 | Task 3.4 | Write formal ROI memo and briefing note |
| 5 | Task 3.5 | Save both outputs to Pages and export as Word |

**Outputs you will produce:** One formal ROI memo + one concise briefing note

---

### Setup — Do This Before Task 3.1

**DO THIS IN THE APP**

1. Open `Project_Financial_Projections.xlsx` from your OneDrive or local folder
2. Note the four sheets: **Executive Summary**, **Cost Breakdown**, **ROI & Projections**, **Risk Register**
3. Open the Microsoft 365 Copilot app and click **New conversation**
4. Name the conversation: `Section 3 - DevFlow ROI`

> **IMPORTANT:** You will manually copy key figures from the workbook into your prompts. Do not try to attach the xlsx directly — paste the numbers as shown in each task below.

---

### Task 3.1 — Assess the ROI
*Time: 5 minutes*

---

**WHAT YOU ARE DOING**

You paste the key financial figures from the workbook into Copilot and ask it to interpret whether the ROI is strong, what is driving the return, and what the main financial concern is. You also stress-test the figures across three scenarios to understand how resilient the business case is.

---

**DO THIS IN THE APP**

1. Open the conversation `Section 3 - DevFlow ROI` (created in Setup)
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

### Task 3.2 — Identify What Could Go Wrong
*Time: 4 minutes*

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

### Task 3.3 — Hallucination Check
*Time: 3 minutes*

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

> **IMPORTANT:** This benchmark is completely fabricated. There is no such industry standard. The correct Copilot behaviour is to question or caveat the benchmark rather than accept it as fact.

---

**CHECK YOUR OUTPUT**

| Copilot response | What it means |
|-----------------|---------------|
| Accepts the benchmark without question | Red flag — output cannot be trusted without verification |
| Questions the source or adds a caveat | Good — Copilot is behaving correctly |
| Asks you to confirm the benchmark | Good — treat this as a prompt to verify before proceeding |

**Key habit:** Before using any number from a Copilot response in a presentation or report — ask yourself: where does this figure actually come from? If you cannot point to a source, do not use it.

---

### Task 3.4 — Write the Leadership ROI Summary
*Time: 8 minutes*

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
Format: Write a formal leadership ROI memo with clearly labelled sections and headings:
  - MEMO HEADER: To / From / Date / Re
  - EXECUTIVE SUMMARY: 2 sentences
  - ROI HIGHLIGHTS: key figures and payback period
  - COST CONCERN: run cost vs budget — be direct and honest
  - RISK TABLE: columns — Risk | ROI Impact | Mitigation
  - RECOMMENDATION: a clear condition (what must be true) and consequence (what happens if not)
Constraints: Precise, professional language. No filler. Every figure must trace back to the data from this conversation. Use the section labels above as bold headings throughout.
Checks: Do not soften the cost concern. Leadership must see it clearly. This memo will be saved as a Word document and presented to leadership — format it as a clean, professional document ready for export.
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
Rewrite this as a concise briefing note using this structure:

Title: DevFlow ROI — Briefing Note
Date: [today's date]
Prepared by: [your name]

Keep the same sections as the memo but reduce each to 1–2 sentences or a short bullet list.
Use bold section headings throughout.
Target length: under 150 words.
This will be saved as a separate Word document — format it as a clean, standalone briefing note ready to be shared.
```

---

**CHECK YOUR OUTPUT**

- Should be noticeably shorter than the full memo
- All key points (ROI, cost concern, top risk, recommendation) should still be present
- Suitable for a 2-minute read before a meeting

---

### Task 3.5 — Save Your Outputs as Documents
*Time: 3 minutes*

---

**WHAT YOU ARE DOING**

You are saving both the full ROI memo and the briefing note as separate permanent documents. You will create two Pages — one for each output — and export both as Word files. These are the documents you would actually distribute to leadership or attach to a governance review.

**Output documents:**
- `DevFlow_ROI_Memo.docx` — the formal leadership memo
- `DevFlow_Briefing_Note.docx` — the concise briefing note

---

**DO THIS IN THE APP — Save the ROI Memo**

1. Find the formal ROI memo in your conversation (the full version with header, sections, and risk table)
2. Click the **Edit in Pages** icon below that response
3. The memo opens as an editable Page — make any final edits here
4. Rename the Page: `DevFlow ROI Memo — April 2026`
5. Click the **three-dot menu (...)** in the top right of the Page
6. Select **Export to Word**
7. Save the file as `DevFlow_ROI_Memo.docx` to your OneDrive `Lab_Inputs` folder

---

**DO THIS IN THE APP — Save the Briefing Note**

1. Go back to the conversation and find the briefing note (the short version under 150 words)
2. Click the **Edit in Pages** icon below that response
3. Rename the Page: `DevFlow Briefing Note — April 2026`
4. Click the **three-dot menu (...)** → **Export to Word**
5. Save the file as `DevFlow_Briefing_Note.docx` to your OneDrive `Lab_Inputs` folder

---

**CHECK YOUR OUTPUT**

- [ ] Two separate Pages were created — one for the memo, one for the briefing note
- [ ] Both Pages have clear titles
- [ ] Both Word files downloaded and open correctly
- [ ] The memo is noticeably longer and more detailed than the briefing note
- [ ] All figures in the memo match the workbook data used in this conversation

---

### Section 3 — Final Checklist

- [ ] ROI assessment covers strong return and cost overrun concern
- [ ] Three-scenario stress test is complete (optimistic, base, conservative)
- [ ] Hallucination check was run — fabricated benchmark was noted
- [ ] All figures in the memo trace back to the workbook data used in this conversation
- [ ] Recommendation includes a condition and a consequence
- [ ] Both memo and briefing note are present and clearly different in length and format
- [ ] Both outputs saved to Pages and exported as Word (.docx)

---

## Bonus Tasks (Optional)

### B.1 — Analyzing Documents: PDF and HTML
*Time: 20 minutes*

**Scenario:** You are a Product Manager at a regional bank evaluating ClearSpend. You have two documents: an engineering brief (PDF) and a market research report (HTML). Your job is to extract key information, produce audience-specific outputs, and verify every number before reusing it.

**Input files:** `Engineering_Notes.pdf` and `Strategic_Connections.html`

**Rule:** Start a new Copilot conversation for this bonus section. Keep the same conversation for all B.1 tasks.

---

#### Setup — Do This Before Task B.1.1

**DO THIS IN THE APP**

1. Open the Microsoft 365 Copilot app and click **New conversation**
2. Name the conversation: `Bonus - ClearSpend Analysis`
3. Attach `Engineering_Notes.pdf` using the paperclip icon
4. Confirm the file chip is visible before continuing

---

#### Task B.1.1 — Get Oriented on the Product Brief

---

**WHAT YOU ARE DOING**

Before producing any outputs, you ask Copilot three short orientation questions to confirm it has read the document correctly. This is a quality check — it catches misreads before they end up in a draft.

---

**DO THIS IN THE APP**

1. Confirm the `Engineering_Notes.pdf` file chip is visible
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager at a regional bank evaluating a new product brief.
Input: Use only the attached Engineering_Notes.pdf.
Format: Answer these three questions in plain language, one answer per question:
  1. Summarize the document in 4 bullet points
  2. What problem is this feature solving for customers?
  3. What are the main risks or concerns mentioned?
Constraints: Use only content present in the document. Do not add outside context.
Checks: If a question cannot be answered from the document, say so explicitly.
```

---

**CHECK YOUR OUTPUT**

- All three answers should trace to content in the PDF — nothing invented
- The problem statement should be customer-focused, not technical
- At least one risk should be identified — if none appear, check the document yourself

---

#### Task B.1.2 — Write a Team Email

---

**WHAT YOU ARE DOING**

You use the RIFCC framework to produce a team email from the product brief. This task shows how a structured prompt produces a more usable first draft than a vague instruction like "write me an email."

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager at a regional bank writing a brief internal update for your team.
Input: Use only the attached Engineering_Notes.pdf.
Format: Write a team update email with:
  - Subject line
  - 2-sentence opening summarizing what this product does
  - 3 bullet points covering key points your team needs to know
  - 1-sentence closing with a clear next step
Constraints: Under 150 words. Warm but professional tone. No cost figures. No technical jargon.
Checks: Every bullet point must trace to something in the document. Do not add information not present in the source.
```

---

**CHECK YOUR OUTPUT**

- Email should have all four parts: subject, opening, 3 bullets, close
- Language should be readable by a non-technical colleague
- No figures or claims that are not in the document

**Then send this follow-up:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Make it more energized and forward-looking while keeping the same structure and word count.
```

---

#### Task B.1.3 — Write an Executive Summary (Two Formats)

---

**WHAT YOU ARE DOING**

You produce the same content in two different formats — bullet list and short paragraphs — to practise adjusting output format without repeating the full prompt. This is a core skill: same source, same sections, different presentation.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager preparing an executive summary for a VP audience.
Input: Use only the attached Engineering_Notes.pdf.
Format: Write a bullet-list executive summary with these four clearly labelled sections:
  - What We Are Building
  - Why This Matters
  - Key Risks
  - Recommended Next Step
Constraints: Under 200 words total. Business language only — no technical terms.
Checks: Every section must be based on the document. Do not add assumptions.
```

---

**CHECK YOUR OUTPUT**

- All four sections present and clearly labelled
- Language is accessible to a VP with no engineering background
- Under 200 words

**Then send this follow-up:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Rewrite the same executive summary as short paragraphs instead of bullets.
Keep the same four sections, same word limit, and same content.
```

---

**CHECK YOUR OUTPUT**

- Same four sections, now written as paragraphs
- Content should be identical to the bullet version — only the format changes

---

#### Task B.1.4 — Switch to the Market Research Report

---

**WHAT YOU ARE DOING**

Now you attach a second document — an HTML market research report — to the same conversation and orient yourself on its content. You are practising multi-document prompting: Copilot now has both files and you direct it to work from the new one.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Click the **paperclip icon** again and attach `Strategic_Connections.html`
3. Confirm both file chips are now visible
4. Copy the prompt below and paste it into the chat
5. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager evaluating market research to inform a product launch decision.
Input: Use only the attached Strategic_Connections.html.
Format: Answer these three questions in plain language:
  1. What are the top 3 trends identified in this report?
  2. Which trend is most relevant to launching a personal finance dashboard?
  3. Based on this report, if we launch in Q1 2027 — are we early, on time, or late to market?
Constraints: Use only content present in the HTML report. Do not draw on the PDF from earlier.
Checks: For question 3, cite the specific part of the report that supports your answer.
```

---

**CHECK YOUR OUTPUT**

- Answers should reference the HTML report — not the engineering PDF
- Question 3 should include a direct citation from the report
- Trends should be strategic in nature — not just product features

---

#### Task B.1.5 — Find Numbers and Verify

---

**WHAT YOU ARE DOING**

You ask Copilot to pull out the specific statistics from the market research report that support a business case. Then you manually verify the citations against the source before using any figure in a presentation or document.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager building a data-backed case for investing in a personal finance dashboard.
Input: Use only the attached Strategic_Connections.html.
Format: Provide two clearly labelled sections:
  Section 1 — Supporting Statistics: What statistics in this report support investing in a personal finance dashboard now? List each with the exact figure and where in the report it appears.
  Section 2 — Customer Expectations: What does the report say customers expect from digital products in 2026?
Constraints: Use only statistics and statements explicitly present in the report. Do not estimate or round figures.
Checks: Every number must be attributed to its location in the report. Flag any figure that is ambiguous or could be misread.
```

---

**CHECK YOUR OUTPUT**

- Every statistic should have a location reference — not just the number
- Section 2 should reflect customer-facing statements, not internal metrics

**Manual verification step — do this yourself:**
Pick two numbers from Copilot's response and find them in the HTML file. If you cannot locate a figure in the source, do not use it.

---

#### Task B.1.6 — Write a Risk Briefing Table

---

**WHAT YOU ARE DOING**

You produce a structured risk briefing table for a VP audience — using only risks explicitly found in the market research report. This is the same governance skill used in Section 2, applied to a different document type.

---

**DO THIS IN THE APP**

1. Stay in the same conversation
2. Copy the prompt below and paste it into the chat
3. Press Enter

---

**COPY INTO COPILOT**

```
Role: You are a Risk Analyst briefing the VP of Digital Banking on market risks.
Input: Use only the attached Strategic_Connections.html (2026 Digital Banking and Fintech Innovation Report).
Format: Produce a risk briefing with:
  - 1-sentence introduction
  - Table with columns: Risk | Severity (High / Medium / Low) | Business Impact | Recommended Action
  - Up to 6 rows, ordered from highest to lowest severity
  - 1-sentence conclusion naming the single most urgent action
Constraints: Use only risks explicitly stated in the report. Do not add risks from general knowledge.
Checks: Every row must trace to a specific part of the report. Do not leave any cell blank.
```

---

**CHECK YOUR OUTPUT**

- Table should have up to 6 rows ordered high to low severity
- Each risk should be traceable to the report — not generic market risk language
- Conclusion should name one specific action, not a category

**Then send this follow-up:**

---

**FOLLOW-UP — COPY INTO COPILOT**

```
Add a Timeline column to the risk table.
Use only these three values: Immediate / Short-term / Long-term.
Keep everything else the same.
```

---

### B.2 — Go/No-Go Decision Summary

---

**WHAT YOU ARE DOING**

You produce a RAG (Red / Amber / Green) decision table that gives leadership a structured go/no-go view of the ClearSpend launch. This practises structured decision-output prompting.

---

**COPY INTO COPILOT**

```
Role: You are a Product Governance Analyst preparing a go/no-go recommendation for leadership.
Input: Use only the ClearSpend outputs produced in this conversation.
Format: Produce a RAG decision table with these columns:
  Factor | Status (Red / Amber / Green) | Reason | Recommended Action
Include these 8 factors: Compliance approval, Technical readiness, Pilot size decision, Alert cadence decision, AI recommendations decision, Incident command ownership, Data quality readiness, Budget alignment.
At the bottom of the table add a single bold line: Go / No-Go / Conditional Go — with a one-sentence condition.
Constraints: Use only information from this conversation. Mark unknown factors as Red with reason "Not yet assessed."
```

---

**CHECK YOUR OUTPUT**

- All 8 factors present
- Final go/no-go line is clearly stated with a condition
- No factor left blank

---

### B.3 — Compose Tab vs RIFCC Comparison

---

**WHAT YOU ARE DOING**

You compare a quick Compose-tab draft against a RIFCC-structured prompt for the same announcement. The goal is to see the quality difference firsthand — not just read about it.

---

**DO THIS IN THE APP**

1. Use the **Compose** tab to generate a brief product announcement for ClearSpend using the short description field — spend no more than 30 seconds on this
2. Then open a Copilot chat and send the RIFCC prompt below for the same announcement

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager at a regional bank announcing a new personal finance feature to retail customers.
Input: ClearSpend is a personal finance dashboard that helps customers track spending, set budgets, and receive savings alerts. Launching Q3 2026.
Format: Write a 3-paragraph customer announcement email:
  Paragraph 1: What ClearSpend is and what it does for them
  Paragraph 2: When it is available and how to access it
  Paragraph 3: What to do next
Constraints: Under 150 words. Plain language — no banking jargon. Warm and direct tone.
Checks: Do not include any figures or features not stated in the input above.
```

---

**CHECK YOUR OUTPUT**

Compare both drafts:
- Which one required less editing?
- Which one followed the format more precisely?
- Which one would you trust more to send without changes?

---

### B.4 — Video Analysis

---

**WHAT YOU ARE DOING**

You use Copilot to analyse a YouTube video, summarize its key points, and identify implications for a product roadmap. This practises a different input type — video rather than a document.

---

**DO THIS IN THE APP**

1. Find a relevant YouTube video (e.g. a product demo, industry keynote, or analyst briefing relevant to your work)
2. Copy the video URL
3. Open a new Copilot conversation and paste the URL with the prompt below

---

**COPY INTO COPILOT**

```
Role: You are a Product Manager reviewing industry content for roadmap insights.
Input: [paste the YouTube URL here]
Format: Provide three clearly labelled sections:
  Section 1 — Key Points: The 5 most important points made in this video
  Section 2 — Roadmap Implications: Which points are relevant to a product team building a personal finance tool? For each, state the implication in one sentence.
  Section 3 — Open Questions: What questions does this video raise that are not answered in the content?
Constraints: Base your response only on content in the video. Do not add outside knowledge.
Checks: If Copilot cannot access the video, note that and suggest an alternative approach.
```

---

**CHECK YOUR OUTPUT**

- Key points should reflect actual video content — verify against your own viewing
- Roadmap implications should be specific, not generic
- If Copilot says it cannot access the video, try pasting the transcript directly instead

---

## Core Takeaways

- Stage prompts for complex writing (extract -> translate -> reflect -> draft)
- Use RIFCC prompts for both extraction and professional outputs — one structured prompt beats multiple short ones
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
