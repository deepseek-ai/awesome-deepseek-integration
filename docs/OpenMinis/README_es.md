# OpenMinis

<div align="center">
<img src="assets/logo.png" alt="OpenMinis" width="96" height="auto" />

**Tu agente de IA privado en el dispositivo — no solo conversa, actúa de verdad**

</div>

[GitHub](https://github.com/OpenMinis/OpenMinis) · [Sitio web](https://openminis.app) · [App Store](https://apps.apple.com/) · [Comunidad Telegram](https://t.me/openminis)

---

## Qué es

OpenMinis es una aplicación de agente de IA multiplataforma, **gratuita y totalmente de código abierto (GPL-3.0)**, para **iOS, iPadOS, macOS, Android** (y visionOS), con **+3.3k estrellas** en GitHub.

Su filosofía es fundamentalmente distinta a la de las apps de chat de IA convencionales: en lugar de encerrar un modelo en una ventana de chat, le da al modelo **un ordenador real** — un entorno Linux completo que se ejecuta localmente en tu dispositivo, donde el modelo puede instalar paquetes, ejecutar scripts, leer y escribir archivos, manejar un navegador y llamar a capacidades nativas del sistema para hacer las cosas por ti.

## Características principales

| Característica | Descripción |
|----------------|-------------|
| 🤖 Trae tu propio modelo | Conéctate a Anthropic Claude, OpenAI GPT, Google Gemini, OpenRouter y **DeepSeek o cualquier API compatible con OpenAI**, con cambio de modelo por conversación |
| 🐚 Shell Linux integrado | Alpine Linux en sandbox se ejecuta en el dispositivo (iSH en iOS / PRoot en Android) — instala paquetes con `apk add`, ejecuta scripts, procesa archivos reales, sin servidor |
| 📱 Integración profunda con el sistema | HealthKit, Calendario, Recordatorios, Contactos, HomeKit, Bluetooth, Portapapeles, Multimedia, Alarmas y más, expuestos al agente como herramientas |
| 🌐 Automatización de navegador | El agente navega por la web, rellena formularios, extrae contenido y toma capturas por ti |
| 🛠️ Sistema de skills | Formato abierto SKILL.md — importa o crea skills; compatible con los ecosistemas de Claude, Codex, OpenClaw y otros |
| 🧠 Memoria persistente | Memoria entre sesiones que te conoce cada vez mejor |
| 📂 Workspaces | Organiza el trabajo en contextos separados, accesibles vía `minis://workspace/` |
| 🔒 Privacidad por diseño | Claves API guardadas en el Keychain del sistema. Sin recopilación de datos. Sin análisis de terceros. Tus conversaciones son tuyas |

## Arquitectura técnica

Estructura del repositorio (Swift 51% / Kotlin 41% / Objective-C 6%):

```
src/ios/          App iOS (Swift/SwiftUI) + extensiones de compartir, widget y proveedor de archivos
src/android/      App Android (Kotlin/Compose) + código nativo JNI
src/shared/       Recursos compartidos por ambas plataformas
deps/             Scripts de compilación de dependencias nativas (iSH, PRoot, FFmpeg, LAME)
docs/specs/       Especificaciones de arquitectura e interfaces
scripts/          Preparación del rootfs y herramientas de desarrollo
```

Dependencias clave: **iSH** (emulación de Linux en modo usuario para iOS, fork ARM64), **PRoot** (chroot en espacio de usuario para el sandbox de Android), **Alpine Linux** (el minirootfs que arranca el sandbox), FFmpeg, LAME — todas compiladas desde el código fuente, no incluidas como binarios.

## Casos de uso reales

- 📸 Fotografía una comida y registra la nutrición — identifica los platos, estima calorías y macros, y los escribe en Apple Health
- ⏰ Despierta con tu timeline — Shortcuts hace que Minis obtenga tu timeline de X, lo resuma, sintetice voz y lo reproduzca como alarma
- 💬 Convierte el ruido del grupo en tareas — extrae mensajes de un grupo de Telegram, detecta bugs y tareas, los deduplica y los archiva en Apple Reminders
- 📓 Monta tu bóveda de Obsidian — investiga, limpia y escribe notas Markdown de vuelta a la bóveda
- 📅 Convierte cualquier cosa en un evento de calendario — desde la hoja de compartir de iOS, con hora y lugar incluidos

## Cobertura de prensa

> "the most impressive indie app I've seen in a while"
> —— Federico Viticci, MacStories (julio de 2026)

> "在很大程度上实现甚至局部超越了 Apple Intelligence"
> —— Zhihu (junio de 2026)

> "可能是 iOS 端最强 AI Agent"
> —— Appinn (marzo de 2026)

## Ecosistema de código abierto

Bajo la organización OpenMinis (github.com/OpenMinis):

- **[MinisSkills](https://github.com/OpenMinis/MinisSkills)** (354⭐) — colección oficial de skills, más de 40 skills SKILL.md: GitHub Trending, Twitter/X, Bilibili, análisis de sueño, generación de PPT, qBittorrent, billetes 12306, TTS de Doubao y más
- **[AwesomeMinis](https://github.com/OpenMinis/AwesomeMinis)** (190⭐) — colección de casos de uso reales aportados por la comunidad (salud, productividad, investigación, finanzas, herramientas de desarrollo)
- **ish-arm64 / proot** — forks personalizados de iSH y PRoot

## Licencia

GPL-3.0. La app enlaza componentes con licencia GPL (iSH, PRoot), por lo que el trabajo combinado se distribuye bajo GPLv3. El repositorio es un espejo de un árbol de desarrollo privado — no acepta pull requests; los Issues son la vía para dar forma al producto.
