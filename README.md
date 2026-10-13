# MagicInterview — know what to say next, live

![MagicInterview logo](assets/icon-192.png)

MagicInterview helps you know what to say next in interviews and meetings. In the full MagicInterview app, start live listening to receive suggested responses as the conversation happens. Through the connected AI workspace, add your CV, job description, client brief and notes, then get context-grounded answers and prepare the conversation.

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
- Request coaching and review saved guidance for a conversation.

Your assistant sets up the context and opens the right conversation. Start listening in the MagicInterview app when you are ready for live suggestions.

## A compact workspace inside your assistant

In compatible MCP App hosts, ask to open MagicInterview. The interactive workspace uses your connected account's real projects, conversations, sources, preferences, and saved history—not a separate copy.

One compact feature menu covers:

- **What to say next and coding help:** submit a question, get a context-aware answer, and read formatted prose or code.
- **Transcript & speakers:** inspect saved turns, add transcript text, and correct speaker labels.
- **Context & files and projects & conversations:** preview Markdown and original files, attach relevant sources, and manage shared project context and individual conversation notes.
- **Research & CRM and recap & follow-up:** ask your assistant to use its connected services and current sources, refresh relevant context, or draft a recap and follow-up without sending it.
- **Languages & models and account settings:** manage preferences and inspect connection status.
- **Audio/text/screenshots, focus/reading, and voice practice:** paste text in the workspace or open the same conversation in the full app for device-based audio, screenshots, focus controls, and voice practice.

Live listening does not start remotely through MCP. Use the web app on your computer or phone, or the Mac and Android apps. On iPhone, add MagicInterview to your Home Screen for quick access. Links preserve the selected conversation.

## Connect through your assistant

Install the plugin and sign in to your MagicInterview account when your AI assistant asks to connect. Authentication uses the standard OAuth flow; no API key needs to be copied into the plugin.

### Technical MCP endpoint

For clients configured manually, the remote Streamable HTTP endpoint is:

```text
https://magicinterview.ai/mcp
```

For the public ChatGPT directory, use `https://magicinterview.ai/mcp?toolset=directory` to expose each supported operation directly. The default endpoint uses a compact operation catalog for other clients.

## Suggested prompts

- Help me answer this interview question now. Use my CV and job description to suggest a clear response I can say aloud.
- A client just raised an objection. Use my meeting brief to suggest what to say next and one useful follow-up question.
- Open my MagicInterview workspace and prepare my next meeting with a concise brief and context for live answers.

## Troubleshooting for connected users

If something goes wrong, ask your assistant to check the affected MagicInterview conversation and any saved debug information available in your workspace.

## Links

- [MagicInterview](https://magicinterview.ai)
- [Privacy policy](https://magicinterview.ai/privacy)
- [Terms of service](https://magicinterview.ai/terms)
- [Support](https://magicinterview.ai/contact)

## License

MIT
