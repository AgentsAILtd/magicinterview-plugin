# MagicInterview — know what to say next, live

![MagicInterview logo](assets/icon-192.png)

Know what to say next, even when the question catches you off guard. MagicInterview listens to your interview or meeting and shows suggested responses as the conversation happens. Add your CV and the job description, or bring a client brief and notes. Read a suggestion, adapt it, and keep the conversation moving.

## Live help when the conversation matters

**Interviewing for your next job?** Add your CV and the job description. Get live suggestions that connect your experience to the role when the interviewer asks a question.

**Finally meeting that potential client?** Bring your client brief, offer, and past notes. Get help answering questions, responding to objections, and explaining the value of your offer as the call unfolds.

**Keep your next answer in view.** Open MagicInterview on your phone beside your computer, or use it on the same computer as your call. Start listening in MagicInterview and follow the suggestions as the conversation happens.

![MagicInterview live answer on a phone](assets/iphone-answer.webp)

## What the plugin connects

This plugin connects your AI assistant to your MagicInterview workspace so it can:

- Find, create, and update projects and conversations, then open the exact meeting in MagicInterview.
- Add relevant CVs, job descriptions, client briefs, and documents to your conversations.
- Keep shared project sources consistent across related meetings while preserving individual notes and history.
- Help set up today's professional meetings in time order. When your assistant has calendar or CRM access, it can use that context too.
- Request coaching and retrieve saved debug logs to investigate a session problem.

Your assistant sets up the context and opens the right conversation. Start listening in the MagicInterview app when you are ready for live suggestions.

## A compact workspace inside your assistant

In compatible MCP App hosts, ask to open MagicInterview. The interactive workspace uses your connected account's real projects, conversations, sources, preferences, and saved history—not a separate copy.

One compact feature menu covers:

- **What to say next and coding help:** submit a question, get a context-aware answer, and read formatted prose or code.
- **Transcript & speakers:** inspect saved turns, add transcript text, and correct speaker labels.
- **Context & files and projects & conversations:** preview Markdown and original files, attach relevant sources, and manage shared project context and individual conversation notes.
- **Research & CRM and recap & follow-up:** ask your assistant to use its connected services and current sources, refresh relevant context, or draft a recap and follow-up without sending it.
- **Languages & models, apps/account/sync, and MCP/debug logs:** manage preferences, inspect connection status, and retrieve saved diagnostics.
- **Audio/text/screenshots, focus/reading, and voice practice:** paste text in the workspace or open the same conversation in the full app for device-based audio, screenshots, focus controls, and voice practice.

Live listening does not start remotely through MCP. Use the web app on your computer or phone, or the Mac and Android apps. On iPhone, add MagicInterview to your Home Screen for quick access. Links preserve the selected conversation.

## Connect through your assistant

Install the plugin and sign in to your MagicInterview account when your AI assistant asks to connect. Authentication uses the standard OAuth flow; no API key needs to be copied into the plugin.

### Technical MCP endpoint

For clients configured manually, the remote Streamable HTTP endpoint is:

```text
https://magicinterview.ai/mcp
```

The compact connection exposes six agent-facing tools: `get_profile`, `get_tool_catalog`, `learn_tools`, `read_tool`, `execute_tool`, and `show_magicinterview`. The catalog provides 34 operations; two private helpers handle interactions inside the app. Older `https://magicinterview.app/mcp` connections remain supported.

## Suggested prompts

- I have a job interview. Use my CV and the job description to set up live help, then open that MagicInterview conversation.
- I have a meeting with a potential client. Use our brief and past notes to set up live suggestions for the call.
- Prepare today's meetings from my available calendar context and give me MagicInterview links I can open on my phone.

## Troubleshooting for connected users

If something goes wrong, ask your assistant to check the affected MagicInterview conversation and any saved debug information available in your workspace.

## Links

- [MagicInterview](https://magicinterview.ai)
- [Privacy policy](https://magicinterview.ai/privacy)
- [Terms of service](https://magicinterview.ai/terms)
- [Support](https://magicinterview.ai/contact)

## License

MIT
