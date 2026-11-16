# DSChat

DSChat is an open-source DeepSeek API chat client for Android and the web, built on
DeepSeek's official open-source `chat-demo` framework (MIT).

- **Platforms:** Android (APK), installable PWA, and desktop/mobile web.
- **API:** DeepSeek Messages API (`deepseek-flash`), with deep thinking, web search, link
  reading, file attachments, ASR, and TTS.
- **Conversation forking:** create a new conversation from any assistant reply, or before
  any user question, while keeping the original chat unchanged.
- **Pinned conversations:** pin chats to a dedicated group at the top of the sidebar.
- **Message search:** search across all conversations; each matching message is a separate
  result, and a conversation can appear multiple times.
- **Persona presets:** create, edit, and activate named system prompts.
- **Cross-session branch graph:** visualize forked conversations and open a session by
  clicking its node.
- **Interactive drawer:** the mobile sidebar follows the finger with a proportional mask
  and a settle animation.
- **Local-first:** chats and attachments stay in IndexedDB; the API key stays in local
  storage and is never bundled with the app.
- **Open source:** MIT licensed, with English and Chinese documentation.

DSChat is an independent community project built on DeepSeek's openly published framework.
It is not an official DeepSeek product and does not imply DeepSeek endorsement.

- Repository: `https://github.com/ADE150/deepseek-api-chat`
- Android APK: `https://github.com/ADE150/deepseek-api-chat/releases`
- License: MIT
