import httpx
import base64
from typing import Optional, Dict, Any
from app.models.ai import AIProvider

async def analyze_image_with_llm(
    provider: AIProvider, 
    image_data: bytes, 
    prompt: str = "Analyze this plant leaf for diseases and provide a detailed report in Arabic."
) -> Dict[str, Any]:
    """
    Generic function to analyze an image using the configured LLM provider.
    """
    if provider.provider_type == "openai":
        return await _analyze_openai(provider, image_data, prompt)
    elif provider.provider_type == "google":
        return await _analyze_google(provider, image_data, prompt)
    else:
        raise ValueError(f"Provider type {provider.provider_type} not supported for vision yet.")

async def _analyze_openai(provider: AIProvider, image_data: bytes, prompt: str) -> Dict[str, Any]:
    base64_image = base64.b64encode(image_data).decode('utf-8')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {provider.api_key}"
    }
    payload = {
        "model": provider.model_id,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    }
                ]
            }
        ],
        "max_tokens": 1000
    }
    
    url = provider.base_url or "https://api.openai.com/v1/chat/completions"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload, timeout=60.0)
        response.raise_for_status()
        data = response.json()
        return {
            "analysis": data["choices"][0]["message"]["content"],
            "provider": provider.name,
            "model": provider.model_id
        }

async def _analyze_google(provider: AIProvider, image_data: bytes, prompt: str) -> Dict[str, Any]:
    # Gemini 1.5 Pro/Flash Vision API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{provider.model_id}:generateContent?key={provider.api_key}"
    
    base64_image = base64.b64encode(image_data).decode('utf-8')
    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": base64_image
                    }
                }
            ]
        }]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=60.0)
        response.raise_for_status()
        data = response.json()
        return {
            "analysis": data["candidates"][0]["content"]["parts"][0]["text"],
            "provider": provider.name,
            "model": provider.model_id
        }
