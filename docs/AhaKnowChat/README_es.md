<img src="./assets/logo.png" width="64" height="auto" />

# [AhaKnow Chat](https://github.com/IHKYoung/AhaKnowChat)

AhaKnow Chat es un espacio de trabajo de chat con IA local-first que puede usar DeepSeek a través de cualquier API compatible con OpenAI. Soporta hilos por tema, roles reutilizables, lluvia de ideas con múltiples roles y almacenamiento local en el navegador.

## UI

<img src="./assets/home.png" />

## En uso

<img src="./assets/usage.png" />

## Ajustes

<img src="./assets/settings.png" />

## Integración con la API de DeepSeek

Como AhaKnow Chat usa una superficie de API compatible con OpenAI, DeepSeek puede integrarse directamente sin código backend adicional.

### Paso a paso

1. Abre `Settings` y entra en la pestaña `AI Provider`.
2. Configura `Base URL` como `https://api.deepseek.com`.
3. Pega tu propia API key de DeepSeek en el campo `API Key`.
4. Haz clic en `Test Connection` para verificar el endpoint y cargar los modelos disponibles.
5. Elige un modelo por defecto:
   - `deepseek-chat` para uso general
   - `deepseek-reasoner` para tareas de razonamiento más intensivas
6. Guarda la configuración, crea un tema y luego inicia un hilo para chatear con DeepSeek.

### Notas

- La versión web guarda la configuración localmente en el navegador.
- Si despliegas el cliente web en Vercel, el endpoint de DeepSeek debe permitir solicitudes desde el navegador y CORS.
- También puedes usar DeepSeek mediante gateways o proxies compatibles, siempre que expongan una API compatible con OpenAI.
