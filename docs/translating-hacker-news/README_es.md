<img src="https://aidoge.ai/resource/TranslatingHackerNewsIcon.jpg" width="64" height="auto" />

# Translating Hacker News

Configuración y demostración en vivo: [https://aidoge.ai/es/translating_hacker_news_intro.html](https://aidoge.ai/es/translating_hacker_news_intro.html)

**Translating Hacker News** es un lector de Hacker News para iOS que traduce historias, comentarios y artículos enlazados en el mismo flujo de lectura. Usa la **API oficial de DeepSeek** (BYOK) porque es rápida, económica y permite editar el prompt de traducción para adaptarlo a las discusiones de HN.

## Interfaz

<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/5e/82/ea/5e82ea84-ad70-6785-8e6e-e56ea962df2d/iPhone_16_Pro_Max-01-app-launched.png/686x1024bb.jpg" width="280" alt="Traducción in situ del feed" />
<img src="https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/d5/5b/7a/d55b7a61-80de-7f23-5e2d-265b55a3feb0/iPhone_16_Pro_Max-04-agent-configuration.png/686x1024bb.jpg" width="280" alt="Configuración del agente DeepSeek" />

## Por qué DeepSeek

- **Rápido**: `deepseek-v4-flash` por defecto traduce títulos e hilos de comentarios mientras haces scroll.
- **Bajo coste**: Con tu propia clave, traducir el feed y los hilos de forma continua sigue siendo económico.
- **Prompts personalizables**: Edita el prompt de traducción (y temperature / Top P) para que el tono encaje con las discusiones técnicas de HN.

## Integración con la API de DeepSeek

Abre **Ajustes → AI Agent**, elige DeepSeek y guarda tu clave de [DeepSeek Open Platform](https://platform.deepseek.com/api_keys).
