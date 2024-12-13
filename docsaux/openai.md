# OpenAI API Documentation

## Models

### Flagship models

- GPT-4o
  - High-intelligence flagship for complex tasks
  - Text and image input, text output
  - 128k context
  - Smarter, higher price per token

- GPT-4o mini
  - Affordable small model for lightweight tasks
  - Text and image input, text output
  - 128k context
  - Faster, lower price per token

- o1-preview & o1-mini
  - **Beta**
  - Reasoning models for hard problems
  - Text input, text output
  - 128k context
  - Higher latency, uses tokens to think

### Models overview

The API offers diverse models with varying capabilities and prices.

| Model | Description |
| --- | --- |
| GPT-4o | High-intelligence flagship for complex tasks |
| GPT-4o mini | Affordable small model for lightweight tasks |
| o1-preview and o1-mini | Reinforcement learning for complex reasoning |
| GPT-4 Turbo and GPT-4 | Previous high-intelligence models |
| GPT-3.5 Turbo | Fast, inexpensive for simple tasks |
| DALL·E | Generates and edits images from text |
| TTS | Converts text to spoken audio |
| Whisper | Converts audio to text |
| Embeddings | Converts text to numerical form |
| Moderation | Detects sensitive or unsafe text |
| Deprecated | List of deprecated models with replacements |

For GPT-series, the context window is the max tokens per request, including input and output.

### Continuous model upgrades

`gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `gpt-4`, and `gpt-3.5-turbo` point to the latest versions.

### GPT-4o

GPT-4o is advanced and multimodal, supporting text and image inputs with text output. It has a 128k context and supports up to 16,384 tokens. Cheaper and faster than GPT-4 Turbo with superior vision and non-English performance. Available to paying API customers.

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| gpt-4o | 128k | 16,384 | Oct 2023 |
| gpt-4o-2024-11-20 | 128k | 16,384 | Oct 2023 |
| gpt-4o-2024-08-06 | 128k | 16,384 | Oct 2023 |
| gpt-4o-2024-05-13 | 128k | 4,096 | Oct 2023 |
| chatgpt-4o-latest | 128k | 16,384 | Oct 2023 |

### GPT-4o mini

GPT-4o mini is the advanced small, affordable model. It is multimodal, more intelligent than `gpt-3.5-turbo`, and as fast. Suitable for small and vision tasks. Recommended over `gpt-3.5-turbo`.

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| gpt-4o-mini | 128k | 16,384 | Oct 2023 |
| gpt-4o-mini-2024-07-18 | 128k | 16,384 | Oct 2023 |

### GPT-4o Realtime + Audio

Preview of GPT-4o Realtime and Audio models. `gpt-4o-realtime-*` handle audio and text via WebSocket.

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| gpt-4o-realtime-preview | 128k | 4,096 | Oct 2023 |
| gpt-4o-realtime-preview-2024-10-01 | 128k | 4,096 | Oct 2023 |
| gpt-4o-audio-preview | 128k | 16,384 | Oct 2023 |
| gpt-4o-audio-preview-2024-10-01 | 128k | 16,384 | Oct 2023 |

### o1-preview and o1-mini

o1 series trained with reinforcement learning for complex reasoning, producing internal chains of thought.

Types:

- **o1-preview**: Solves hard problems across domains.
- **o1-mini**: Faster, cheaper, excels in coding, math, and science.

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| o1-preview | 128k | 32,768 | Oct 2023 |
| o1-preview-2024-09-12 | 128k | 32,768 | Oct 2023 |
| o1-mini | 128k | 65,536 | Oct 2023 |
| o1-mini-2024-09-12 | 128k | 65,536 | Oct 2023 |

### GPT-4 Turbo and GPT-4

GPT-4 is a large multimodal model with text and image inputs and text output.

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| gpt-4-turbo | 128k | 4,096 | Dec 2023 |
| gpt-4-turbo-2024-04-09 | 128k | 4,096 | Dec 2023 |
| gpt-4-turbo-preview | 128k | 4,096 | Dec 2023 |
| gpt-4-0125-preview | 128k | 4,096 | Dec 2023 |
| gpt-4-1106-preview | 128k | 4,096 | Apr 2023 |
| gpt-4 | 8,192 | 8,192 | Sep 2021 |
| gpt-4-0613 | 8,192 | 8,192 | Sep 2021 |
| gpt-4-0314 | 8,192 | 8,192 | Sep 2021 |

GPT-4 outperforms GPT-3.5 in complex reasoning.

#### Multilingual capabilities

GPT-4 excels on the MMLU benchmark in English and other languages, outperforming previous models and most state-of-the-art systems.

### GPT-3.5 Turbo

| Model | Context window | Max output tokens | Knowledge cutoff |
| --- | --- | --- | --- |
| gpt-3.5-turbo-0125 | 16,385 | 4,096 | Sep 2021 |
| gpt-3.5-turbo | 16,385 | 4,096 | Sep 2021 |
| gpt-3.5-turbo-1106 | 16,385 | 4,096 | Sep 2021 |
| gpt-3.5-turbo-instruct | 4,096 | 4,096 | Sep 2021 |

### DALL·E

DALL·E creates realistic images and art from text. DALL·E 3 generates new images with specific sizes. DALL·E 2 edits or varies existing images.

| Model | Description |
| --- | --- |
| dall-e-3 | Latest model as of Nov 2023 |
| dall-e-2 | Previous model, Nov 2022, higher resolution |

### TTS

TTS converts text to natural-sounding speech. Two variants:

- `tts-1`: Optimized for speed.
- `tts-1-hd`: Optimized for quality.

| Model | Description |
| --- | --- |
| tts-1 | Latest TTS model, speed-focused |
| tts-1-hd | Latest TTS model, quality-focused |

### Whisper

Whisper is a speech recognition model supporting multilingual transcription, translation, and language identification. Available as `whisper-1` via the API.

### Embeddings

Embeddings convert text into numerical representations for similarity tasks like search and clustering.

| Model | Output Dimension |
| --- | --- |
| text-embedding-3-large | 3,072 |
| text-embedding-3-small | 1,536 |
| text-embedding-ada-002 | 1,536 |

---

### Moderation

Moderation models ensure content complies with usage policies

| Model | Max tokens |
| --- | --- |
| omni-moderation-latest | 32,768 |
| omni-moderation-2024-09-26 | 32,768 |
| text-moderation-latest | 32,768 |
| text-moderation-stable | 32,768 |
| text-moderation-007 | 32,768 |

### GPT base

GPT base models handle language or code without instruction following. They replace GPT-3 base models and use the legacy Completions API. Prefer GPT-3.5 or GPT-4.

| Model | Max tokens | Knowledge cutoff |
| --- | --- | --- |
| babbage-002 | 16,384 | Sep 2021 |
| davinci-002 | 16,384 | Sep 2021 |

### How we use your data

#### Your data is your data

From March 1, 2023, API data isn't used to train models unless you opt-in. Opting in can improve models for your use case.

API data is retained for up to 30 days for abuse detection, then deleted unless required by law. Zero data retention is available for sensitive applications, meaning no logging and data exists only in memory.

#### Default usage policies by endpoint

| Endpoint | Data used for training | Default retention | Eligible for zero retention |
| --- | --- | --- | --- |
| /v1/chat/completions | No | 30 days | Yes, except for image inputs, certain schemas, audio outputs |
| /v1/assistants | No | 30 days | No |
| /v1/threads | No | 30 days | No |
| /v1/threads/messages | No | 30 days | No |
| /v1/threads/runs | No | 30 days | No |
| /v1/vector_stores | No | 30 days | No |
| /v1/threads/runs/steps | No | 30 days | No |
| /v1/images/generations | No | 30 days | No |
| /v1/images/edits | No | 30 days | No |
| /v1/images/variations | No | 30 days | No |
| /v1/embeddings | No | 30 days | Yes |
| /v1/audio/transcriptions | No | Zero | - |
| /v1/audio/translations | No | Zero | - |
| /v1/audio/speech | No | 30 days | Yes |
| /v1/files | No | Until deleted by customer | No |
| /v1/fine_tuning/jobs | No | Until deleted by customer | No |
| /v1/batches | No | Until deleted by customer | No |
| /v1/moderations | No | Zero | - |
| /v1/completions | No | 30 days | Yes |
| /v1/realtime (beta) | No | 30 days | Yes |

**Notes:**

- **Chat Completions:**
  - Image inputs via certain models are not eligible for zero retention.
  - Audio outputs are stored for 1 hour.
  - Structured Outputs schemas are not eligible for zero retention.
  - Stored Completions with `store: true` are kept for 30 days.

- **Assistants API:**
  - Objects deleted via API or dashboard are removed after 30 days; otherwise, retained indefinitely.

- **Evaluations:**
  - Evaluation data deleted 30 days after dashboard deletion; otherwise, retained indefinitely.

### Model endpoint compatibility

| Endpoint | Latest models |
| --- | --- |
| /v1/assistants | GPT-4o (except chatgpt-4o-latest), GPT-4o-mini, GPT-4, GPT-3.5 Turbo. Retrieval tool requires gpt-4-turbo-preview or gpt-3.5-turbo-1106 |
| /v1/audio/transcriptions | whisper-1 |
| /v1/audio/translations | whisper-1 |
| /v1/audio/speech | tts-1, tts-1-hd |
| /v1/chat/completions | GPT-4o, GPT-4o-mini, GPT-4, GPT-3.5 Turbo and dated versions. chatgpt-4o-latest dynamic. Fine-tuned versions available. |
| /v1/completions (Legacy) | gpt-3.5-turbo-instruct, babbage-002, davinci-002 |
| /v1/embeddings | text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002 |
| /v1/fine_tuning/jobs | gpt-4o, GPT-4o-mini, GPT-4, GPT-3.5-turbo |
| /v1/moderations | text-moderation-stable, text-moderation-latest |
| /v1/images/generations | dall-e-2, dall-e-3 |
| /v1/realtime (beta) | gpt-4o-realtime-preview, gpt-4o-realtime-preview-2024-10-01 |

## Text generation

Generate text from prompts using OpenAI's APIs and large language models.

Create a human-like response to a prompt.

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```

```bash
curl "https://api.openai.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    }'
```

### Analyze an image

Describe the contents of an image.

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    }
                },
            ],
        }
    ],
)

print(completion.choices[0].message)
```

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
        ]
      }
    ]
  }'
```

#### Generate JSON data

Create JSON based on a JSON Schema.

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[
        {
            "role": "system", 
            "content": "You extract email addresses into JSON data."
        },
        {
            "role": "user", 
            "content": "Feeling stuck? Send a message to help@mycompany.com."
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "email_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "email": {
                        "description": "The email address that appears in the input",
                        "type": "string"
                    }
                },
                "additionalProperties": false
            }
        }
    }
)

print(response.choices[0].message.content);
```

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-2024-08-06",
    "messages": [
      {
        "role": "system",
        "content": "You extract email addresses into JSON data."
      },
      {
        "role": "user",
        "content": "Feeling stuck? Send a message to help@mycompany.com."
      }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "email_schema",
        "schema": {
            "type": "object",
            "properties": {
                "email": {
                    "description": "The email address that appears in the input",
                    "type": "string"
                }
            },
            "additionalProperties": false
        }
      }
    }
  }'
```

### Choosing a model

Select a [model](/docs/models) to influence output quality and cost.

- **Large models** (`gpt-4o`): High performance, higher cost.
- **Small models** (`gpt-4o-mini`): Faster, cheaper.
- **Reasoning models** (`o1` family): Advanced reasoning, higher token usage.

## Vision

Understand images using OpenAI's vision-capable models.

### Quickstart

Provide images via URL or base64 in `user` messages.

#### What's in this image?

The model answers general questions about images.

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
  {
    "role": "user",
    "content": [
      {"type": "text", "text": "What’s in this image?"},
      {
        "type": "image_url",
        "image_url": {
          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        },
      },
    ],
  }
],
max_tokens=300,
)

print(response.choices[0])
```

```bash
curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}'
```

#### Uploading Base64 encoded images

Provide local images in base64 format.

```python
import base64
from openai import OpenAI

client = OpenAI()

## Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

## Path to your image
image_path = "path_to_your_image.jpg"

## Getting the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)

print(response.choices[0])
```

#### Multiple image inputs

Process multiple images to answer questions.

```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
  {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "What are in these images? Is there any difference between them?",
      },
      {
        "type": "image_url",
        "image_url": {
          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        },
      },
      {
        "type": "image_url",
        "image_url": {
          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        },
      },
    ],
  }
],
max_tokens=300,
)
print(response.choices[0])
```

```bash
curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are in these images? Is there any difference between them?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}'
```

#### Low or high fidelity image understanding

Control image processing detail with the `detail` parameter.

- `low`: 512x512px, 85 tokens.
- `high`: Detailed crops, 170 tokens per 512px tile.
- `auto`: Default based on image size.

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
  {
    "role": "user",
    "content": [
      {"type": "text", "text": "What’s in this image?"},
      {
        "type": "image_url",
        "image_url": {
          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          "detail": "high"
        },
      },
    ],
  }
],
max_tokens=300,
)

print(response.choices[0].message.content)
```

```bash
curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            "detail": "high"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}'
```

### Managing images

The Chat Completions API is stateless. Manage `messages` and image data yourself. Use URLs for efficiency and downsizing for optimal performance. Images are deleted after processing and not used for training.

### Limitations

- Not for medical images.
- Limited with non-Latin text.
- Issues with small or rotated text.
- Struggles with complex visuals and spatial tasks.
- Does not process metadata.
- Approximate object counting.
- CAPTCHAs are blocked.

### Calculating costs

Image token costs depend on size and `detail`:

- `low`: 85 tokens.
- `high`: 170 tokens per 512px tile + 85 tokens.

**Examples:**

- 1024x1024 `high`: 765 tokens.
- 2048x4096 `high`: 1105 tokens.
- 4096x8192 `low`: 85 tokens.

#### What type of files can I upload?

PNG, JPEG, WEBP, non-animated GIF.

#### Is there a limit to the size of the image I can upload?

20MB per image.

#### Can I delete an image I uploaded?

No, images are deleted after processing.
