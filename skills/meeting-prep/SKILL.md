---
name: meeting-prep
description: Set up MagicInterview live help for job interviews, client calls, sales conversations, and other meetings. Connect the right CV, job description, client brief, and notes; reconcile existing projects and conversations; return the exact live-conversation link. Also use for same-day meeting preparation, context management, coaching, and debug-log investigation.
---

# MagicInterview live conversation copilot

MagicInterview suggests what to say next while an interview or meeting unfolds. Use its projects and sources to ground those suggestions in the user's real background and the specific role, client, or topic. Make the smallest complete change that leaves every relevant conversation accurate, current, reusable, and directly openable.

For a job interview, connect the user's CV and the actual job description. For a prospective client, connect the client brief, prior discussion, offer, and likely objections. For another meeting, use the documents and notes that matter to that conversation. Return the direct link so the user can open MagicInterview on a computer or phone and follow live suggestions as the other person speaks. The web app works on a phone, and Mac and Android apps are available. Do not promise perfect answers or that listening starts remotely through MCP.

## First use, connection and Pro

For a new user asking how to begin, follow [the focused get-started guide](../get-started/SKILL.md); keep urgent questions on the short workflow below.

A user may have installed this plugin without knowing MagicInterview or having an account. Explain only what they need for the next step: it saves their CV, job or meeting brief and conversation context so they can prepare with an assistant and continue in the full app. The account, assistant connection and saved workspace are free; cloud coaching and AI tools require Pro. Live audio capture runs in the full MagicInterview app.

| Current state | Next useful action | Evidence to continue |
| --- | --- | --- |
| Not connected, or authentication required | Use the host's supported connect/reconnect flow. In the browser the user can create a free account or sign in, approve access and return. If no connection control is available, give the host's setup instructions and the endpoint `https://magicinterview.ai/mcp`; do not invent an authentication tool. | A successful account-scoped read, not plugin installation or a sign-in link alone. |
| Connected with no projects or conversations | Ask for the interview, role or meeting context needed for the requested task. Check for an existing matching conversation, then create the first relevant project/conversation only within the user's request and attach the supplied context. No pre-existing CV, calendar or CRM connection is required. | Read back the created conversation and return its exact URL. |
| Free workspace ready | Show what was saved and the next useful action. Preparation and workspace management do not require a coaching call. For a preview before registering, offer `https://magicinterview.ai/interview-tomorrow`. | Distinguish saved context from an AI-generated coaching answer. |
| Coaching returns `PRO_REQUIRED` | Preserve the user's question and selected conversation. Explain that cloud coaching requires Pro and offer the canonical `upgradeUrl` returned by the server. If that field is absent, use `https://magicinterview.ai/app?auth=sign-up&returnTo=pro`. Let the user choose; do not repeatedly call the gated tool or require Pro for free workspace work. | After the user says they upgraded, retry the requested coaching call once; only a successful server response proves access. A checkout visit or return does not. |

Keep the first-use path proportional. For an urgent live question, use existing context immediately when available; do not force a new onboarding tour, account explanation, research sweep or purchase flow. If authentication or Pro blocks the request, state the exact next step while retaining the question. Never claim account creation, authorization, a saved change or paid access without its corresponding result. Never ask for a password or token in chat.

## Help with the question in front of the user

When the user needs an answer now, keep the workflow short. Use the selected or clearly identified conversation and its relevant saved context. If several conversations match, ask one concise question to identify the right one; do not create a duplicate. Request coaching for the interview question, coding question, client objection or meeting turn the user supplies. Present the proposed answer first, then a useful next question or action when supported by the result. Keep suggestions separate from the actual transcript.

Do not start a calendar, inbox, CRM or company-research sweep for a live-question request. Use those sources only when the user requests preparation or supplies a specific missing fact that changes the answer. Save through the coaching tool only within the requested workflow, and read back the selected conversation after a saved change. Provide the exact conversation link for continuing live audio in the full app. Never imply that ChatGPT is listening to the call or can remotely start microphone capture.

## Use the live connection

Use the tools and schemas the current MagicInterview connection exposes. The ChatGPT directory connection exposes named operations directly, such as `list_projects`, `get_conversation`, `request_coaching`, and `get_conversation_url`; call the named tool for each action. Never guess arguments or invoke an operation that is not exposed.

Other MagicInterview clients may use the compact `/mcp` connection. On that connection, browse the operation catalog, learn the needed schemas in one batch, then use `read_tool` for read-only operations and `execute_tool` for changes. Never assume that the two connection shapes have the same callable tool names.

When the host exposes `show_magicinterview`, use it to open the compact interactive workspace, optionally with the exact `conversationId`. Its data comes from the same connected account. The workspace covers answers, coding, transcript and speaker corrections, context and files, projects and conversations, research and CRM handoffs, recap and follow-up drafts, preferences, account status, and debug logs. Device-based audio, screenshots, focus controls, and voice practice open the selected conversation in the full app. Do not call the app's private helpers from the agent or imply that every host renders MCP Apps. Keep direct conversation links available as well.

## Notion context and optional meeting sync

When the user keeps preparation in Notion, discover the exposed Notion operations and read connection and sync status first. An authorized individual import saves a reusable source; importing the same page updates it. Attach only the relevant source to the intended project or conversation. Do not infer ongoing sync from a successful import.

Optional meeting sync is a separate configuration: it creates a MagicInterview home with Projects and Meetings inside the selected shared parent page. Notion Brief edits become conversation context; MagicInterview sends managed meeting details, transcripts and saved coaching back to Notion. Use the requested all-project or selected-project scope, preserve other notes, and read back the resulting status. If page access or read/insert/update permissions are missing, link to [Workspace → Notion](https://magicinterview.ai/app/workspace/notion) to connect or reconnect in the browser. Never ask for Notion tokens in chat or claim the integration connected without a successful result.

## Prepare meetings when requested

Use this section and the following research/reconciliation steps only when the user explicitly requests meeting preparation, a meeting queue or context updates. For a live question, use the short workflow above and only the sources needed for that question.

1. Establish the current time and the user's calendar time zone.
2. Inspect all relevant events today and enough recent days to resolve cancellations, moved meetings, follow-ups, or imported duplicates.
3. Start with the most immediate upcoming meeting that is not completed or cancelled, then continue chronologically. Do not miss an earlier same-day event merely because its nominal start time passed.
4. Exclude clearly unrelated personal reminders. Keep interviews, recruiter calls, customer or sales calls, technical meetings, AI interviews, assessments, and other professional conversations in scope.
5. Classify each event precisely: upcoming, in progress, completed, cancelled, declined, or reschedule pending. Never turn an old invitation into a current commitment.

## Reconstruct current state before writing

For each relevant meeting, reconcile these sources when available:

- The current calendar event, including time zone, latest start and end, participants, organizer, join details, status, and recurrence.
- The complete email, recruiter, messaging, or scheduling thread, including later replies that supersede the original invitation.
- Twenty CRM people, companies, opportunities, notes, tasks, and previous interactions.
- Existing MagicInterview conversations, attached reusable context, saved original files, turns, drafts, and coaching history.
- Current authoritative online information about the company, participants, role, job description, product, meeting topic, or use case.
- The user's current profile, CV, portfolio, relevant experience, and other truthful supporting context.

Calendar is authoritative for current timing and join logistics when stale CRM notes or imported text disagree. The latest complete thread controls cancellation, acceptance, and rescheduling state. Prefer official and current online sources. Treat snippets or partial job descriptions as leads, not complete evidence.

Adapt the research to the event rather than assuming every conversation is a job interview:

- For an interview, recover the exact current role and job description, interview stage, interviewer, expectations, and strongest truthful fit.
- For a sales or customer call, recover the company, people, commercial history, pain points, product relevance, likely objections, and desired next step.
- For a technical, AI, assessment, or general meeting, recover the concrete topic, participants, prior decisions, working materials, and success criteria.

Do not prescribe particular web-search tools. Use the best current research capabilities available to the calling agent.

## Reconcile MagicInterview

Search projects and conversations before creating. Match by the real company, role or topic, event time, and existing membership—not by a similar title alone. Update a matching project and conversation when they represent the same work; create only when no reliable match exists. Do not duplicate projects, conversations, or reusable context.

Use projects for related interviews or meetings that share a purpose, brief, and sources. Learn the current project operations from the catalog. Keep the reusable brief and shared sources on the project, put event-specific logistics and notes on the conversation, and assign each conversation to the correct project. Inspect existing project membership and individual overrides before moving a conversation or changing shared material. Shared project changes should reach member conversations without replacing accurate individual notes or history. For requested merges or deletions, identify the exact project IDs and reconcile their current membership before applying the change.

For every in-scope conversation:

- Set the correct purpose: interview, meeting, sales, or practice.
- Correct the title, company, role or topic, language, notes, and active status.
- Preserve accurate turns, coaching, drafts, and conversation history.
- Attach only the relevant reusable profile, CV, job description, meeting brief, or source material.
- Update stale reusable sources when the same source should remain canonical; create a new source when the subject or evidence is materially different.
- Detach demonstrably wrong or superseded attachments. Do not delete conversations, turns, files, or context by default.
- Make the next actionable conversation active when the user is preparing for it now.

When a meeting is cancelled or awaiting rescheduling, retain the useful history and label the state accurately. Do not present it as an active upcoming meeting.

## Build useful context

The saved brief should be practical during the conversation and should normally include:

- Exact logistics: local date and time, time zone, duration, join route, participants, and current status.
- Purpose, stage, desired outcome, and who owes the next action.
- Exact role or topic requirements and verified company or participant context.
- The user's strongest relevant evidence, examples, and truthful positioning.
- A concise opening, likely questions with answer points, questions to ask, risks, uncertainties, and points to listen for.
- Compensation, contract, eligibility, or commercial facts only when supported by current evidence.
- Separate preparation notes from the candidate's spoken answer.

Keep public or spoken-ready wording free of internal investigation notes, tool narration, unsupported claims, and stale assumptions.

## Verify and return direct links

After every write, read back the exact project or conversation and its attached context. Confirm project membership, shared sources, effective notes, and individual overrides are correct. After making changes, retrieve the conversation again to confirm that its metadata and relevant context are available.

Fetch and return the direct MagicInterview URL for every prepared conversation. The URL must open the exact conversation on the current MagicInterview domain. For a batch, report results in chronological priority order with status, what changed, and the direct URL. Clearly distinguish confirmed conversation details from information that still needs clarification.

## Debugging

When asked why MagicInterview failed or to retrieve logs:

1. Read current service, database, account, and feature status.
2. Retrieve persisted debug events newest-first and use filters for level, source, event, and time when they narrow the incident.
3. Continue pagination until the relevant time window is covered; do not stop at the first page when the incident may be older.
4. Correlate events to the exact conversation, operation, timestamp, and correlation identifier.
5. Report the exact failure, supporting events, affected scope, and smallest corrective action.

When diagnosing an issue, correlate relevant service and conversation events with the affected conversation and time window. For microphone, audio sharing, or coaching-display issues, also check the affected user-facing feature.

## Execution

Complete the requested preparation, MagicInterview data updates, diagnostics, and expressly requested follow-up actions using the available tools. Reuse the user's authorization without repeated confirmation. Ground facts in current evidence and use exact record IDs when reconciling similarly named meetings, companies, people, roles, or conversations. Continue independent work while resolving any concrete missing information.
