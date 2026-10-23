---
name: magicinterview-get-started
description: Guide a new MagicInterview user from a free preview or assistant connection to their first saved interview or meeting. Use when starting the plugin, connecting an account, or asking how to begin.
---

# Your first useful conversation

Use the user's language and the context they already gave. Lead with the next useful action: MagicInterview helps them know what to say next using their CV, job details or meeting brief. Their account, assistant connection and saved workspace are free; cloud coaching and AI tools require Pro. Live audio capture runs in the full MagicInterview app.

1. **No connection or tools yet:** offer the [free preparation preview](https://magicinterview.ai/interview-tomorrow), which needs no account. For saved context, offer [a free account](https://magicinterview.ai/app?auth=sign-up) and the host's existing Connect action. The user signs in or creates their account in the browser, approves access and returns here. Creating an account alone does not connect the assistant. Do not request an API key, token or password in chat, invent an authentication tool, or change the host's authorization flow. If the host has no Connect action, link to [connection setup](https://magicinterview.ai/app/settings/mcp).
2. **Connected:** make the smallest account-scoped read using exposed tools to find the relevant existing project or conversation. Installation or browser sign-in alone does not prove access. Follow the exposed schemas; compact clients may first expose a catalog rather than named operations.
3. **New or empty workspace:** if the purpose is unknown, ask one question: “Is this for a job interview, a client call or another meeting?” Reuse any supplied CV, job description, brief or question. When the user requests preparation or supplies context to save, create or update the first relevant conversation and attach that context; otherwise offer to save it. Do not fabricate sample records or require a CV, calendar connection or tour before useful help.
4. **First value:** read back the saved context, say briefly what is ready and return the exact conversation URL supplied by the tools. Suggest one relevant next action, such as adding the job description or opening the conversation in the full app for live audio. If `magicinterview_open_workspace` is available and useful, offer the interactive workspace; do not imply that every host supports it.
5. **When coaching is requested:** call the available coaching operation for the actual question. If it returns `PRO_REQUIRED`, retain that question and conversation, explain the boundary once and offer the returned `upgradeUrl` (fallback: https://magicinterview.ai/app?auth=sign-up&returnTo=pro). Free workspace work remains available. Retry the coaching request when the user says they upgraded; only a successful response proves access.

For an urgent question, use available context immediately. Do not delay the answer with onboarding, unrelated research or a purchase tour. Without connected tools, help draft from text the user supplies and distinguish that draft from saved MagicInterview context or Pro coaching. Never claim that an account, connection, save or upgrade succeeded without its corresponding result.

## Bring preparation from Notion when relevant

If the user’s brief or notes are in Notion, use exposed Notion status and search/import operations rather than asking them to retype the material. If Notion is not connected, open [Workspace → Notion](https://magicinterview.ai/app/workspace/notion) for browser authorization and page selection. No API key is needed. Offer import for a one-off source, or optional meeting sync only when the user wants ongoing updates. For sync, use the exposed schemas, confirm the intended parent page and project scope from the request, and read back status after a change. An imported page alone does not prove ongoing sync. Keep an urgent question moving with the context already available.
