# ell: The Language Model Programming Library

## Prompts are Programs, Not Strings

ell treats prompts as functions.

```py
import ell

@ell.simple(model="gpt-4o-mini")
def hello(world: str):
 """You are a helpful assistant""" # System prompt
 name = world.capitalize()
 return f"Say hello to {name}!" # User prompt

hello("sam altman") # just a str, "Hello Sam Altman! ..."
```

## Prompt Engineering is an Optimization Process

ell provides tools for iterative prompt engineering.

```py
import ell

ell.init(store='./logdir')  # Versions your LMPs and their calls

# ... define your lmps

hello("strawberry") # the source code of the LMP the call is saved to the store
```

## Tools for Monitoring, Versioning, and Visualization

Use Ell Studio for prompt management.

```bash
ell-studio --storage ./logdir
```

## Test-Time Compute is Important

Implement modular test-time compute with ell.

```py
import ell
from typing import List

@ell.simple(model="gpt-4o-mini", temperature=1.0, n=10)
def write_ten_drafts(idea: str):
   """You are an adept story writer. The story should only be 3 paragraphs"""
   return f"Write a story about {idea}."

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_the_best_draft(drafts: List[str]):
   """You are an expert fiction editor."""
   return f"Choose the best draft from the following list: {'\n'.join(drafts)}."

drafts = write_ten_drafts(idea)

best_draft = choose_the_best_draft(drafts) # Best of 10 sampling.
```

## Every Call to a Language Model is Valuable

ell records all LMP calls for analysis.

## Complexity When You Need It, Simplicity When You Don’t

Use @ell.simple for string outputs or @ell.complex for Message objects.

```py
import ell

@ell.tool()
def scrape_website(url: str):
   return requests.get(url).text

@ell.complex(model="gpt-5-omni", tools=[scrape_website])
def get_news_story(topic: str):
   return [
   ell.system("""Use the web to find a news story about the topic"""),
   ell.user(f"Find a news story about {topic}.")
   ]

message_response = get_news_story("stock market")
if message_response.tool_calls:
   for tool_call in message_response.tool_calls:
   #...
if message_response.text:
   print(message_response.text)
if message_response.audio:
   # message_response.play_audio() support for multimodal outputs will work as soon as the LLM supports it
   pass
```

## Multimodality Should Be First Class

Handle various data types easily with ell.

```py
from PIL import Image
import ell

@ell.simple(model="gpt-4o", temperature=0.1)
def describe_activity(image: Image.Image):
   return [
   ell.system("You are VisionGPT. Answer <5 words all lower case."),
   ell.user(["Describe what the person in the image is doing:", image])
   ]

# Capture an image from the webcam
describe_activity(capture_webcam_image()) # "they are holding a book"
```

## Prompt Engineering Libraries Shouldn’t Interfere with Your Workflow

Use ell seamlessly with regular Python code.

## Installation

Install `ell` and `ell-studio` via the `ell-ai` package and set up your API keys.

### Installing ell

Install using pip:

```bash
pip install -U ell-ai[all]
```

This installs `ell`, `ell-studio`, versioning and tracing with SQLite, and the default provider clients.

Verify installation:

```bash
python -c "import ell; print(ell.__version__)"
```

### Custom Installation

Customize the `ell` installation with the following options.

Install `ell` without storage or `ell-studio` and with the default OpenAI client:

```bash
pip install -U ell-ai
```

#### Supported options

##### anthropic

Adds the Anthropic client.

```bash
pip install -U ell-ai[anthropic]
```

##### groq

Adds the Groq client.

```bash
pip install -U ell-ai[groq]
```

##### studio

Adds `ell-studio`.

```bash
pip install -U ell-ai[studio]
```

##### sqlite

SQLite storage for versioning and tracing.

```bash
pip install -U ell-ai[sqlite]
```

##### postgres

Postgres storage for versioning and tracing. Include this option if you’d like to use `ell-studio` with Postgres.

```bash
pip install -U ell-ai[postgres]
```

#### Combining options

All options are additive and can be combined as needed.

Example: Install `ell` with `ell-studio`, Postgres, and the Anthropic client:

```bash
pip install -U ell-ai[studio, postgres, anthropic]
```

## API Key Setup

### OpenAI API Key

Get your API key from [OpenAI](https://platform.openai.com/account/api-keys).

Install the OpenAI Python package:

```bash
pip install openai
```

Set the environment variable:

**macOS/Linux:**

Add to your `.bashrc` or `.zshrc`:

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

### Anthropic API Key

Get your API key from [Anthropic](https://www.anthropic.com/).

Install the Anthropic Python package:

```bash
pip install anthropic
```

Set the environment variable:

**macOS/Linux:**

Add to your `.bashrc` or `.zshrc`:

```bash
export ANTHROPIC_API_KEY='your-anthropic-api-key'
```

## Troubleshooting

- Update pip:

  ```bash
  pip install --upgrade pip
  ```

- Use a virtual environment
- Try `pip3` instead of `pip`
- Use `sudo` (Unix) or run as administrator (Windows) if permission errors occur

## Getting Started

Welcome to **ell**, the Language Model Programming Library. This guide covers creating your first Language Model Program (LMP), exploring ell’s features, and utilizing its versioning and visualization capabilities.

## From Traditional API Calls to ell

### Traditional API Call

```py
import openai

openai.api_key = "your-api-key-here"

messages = [
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Say hello to Sam Altman!"}
]

response = openai.ChatCompletion.create(
 model="gpt-4o",
 messages=messages
)

print(response['choices'][0]['message']['content'])
```

### Using ell

```py
import ell

@ell.simple(model="gpt-4o")
def hello(name: str):
 """You are a helpful assistant."""
 return f"Say hello to {name}!"

greeting = hello("Sam Altman")
print(greeting)
```

**ell** simplifies prompting by defining prompts as functions, enhancing readability and reusability.

## Understanding @ell.simple

The `@ell.simple` decorator converts a Python function into an LMP:

- Docstring → system message
- Return value → user message
- Handles API calls and returns the response.

## Verbose Mode

Enable detailed logging:

```py
ell.init(verbose=True)
```

## Alternative Message Formats

Define messages explicitly for complex conversations:

```py
import ell

@ell.simple(model="gpt-4o")
def hello(name: str):
 return [
  ell.system("You are a helpful assistant."),
  ell.user(f"Say hello to {name}!"),
  ell.assistant("Hello! I'd be happy to greet Sam Altman."),
  ell.user("Great! Now do it more enthusiastically.")
 ]

greeting = hello("Sam Altman")
print(greeting)
```

## Prompting as Language Model Programming

Use Python to create dynamic prompts:

```py
import ell
import random

def get_random_adjective():
 adjectives = ["enthusiastic", "cheerful", "warm", "friendly"]
 return random.choice(adjectives)

@ell.simple(model="gpt-4o")
def hello(name: str):
 """You are a helpful assistant."""
 adjective = get_random_adjective()
 return f"Say a {adjective} hello to {name}!"

greeting = hello("Sam Altman")
print(greeting)
```

### Composing LMPs

Combine multiple LMPs for complex tasks:

```py
import ell
from typing import List

ell.init(verbose=True)

@ell.simple(model="gpt-4o-mini", temperature=1.0)
def generate_story_ideas(about: str):
 """You are an expert story ideator. Only answer in a single sentence."""
 return f"Generate a story idea about {about}."

@ell.simple(model="gpt-4o-mini", temperature=1.0)
def write_a_draft_of_a_story(idea: str):
 """You are an adept story writer. The story should only be 3 paragraphs."""
 return f"Write a story about {idea}."

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_the_best_draft(drafts: List[str]):
 """You are an expert fiction editor."""
 return f"Choose the best draft from the following list: {'\n'.join(drafts)}."

@ell.simple(model="gpt-4-turbo", temperature=0.2)
def write_a_really_good_story(about: str):
 """You are an expert novelist that writes in the style of Hemmingway. You write in lowercase."""
 ideas = generate_story_ideas(about, api_params=(dict(n=4)))
 drafts = [write_a_draft_of_a_story(idea) for idea in ideas]
 best_draft = choose_the_best_draft(drafts)
 return f"Make a final revision of this story in your voice: {best_draft}."

story = write_a_really_good_story("a dog")
```

## Storing and Versioning Your Prompts

Enable versioning:

```py
ell.init(store='./logdir', autocommit=True, verbose=True)
```

## Exploring Your Prompts with ell-studio

Visualize prompts:

```bash
ell-studio --storage ./logdir
```

## Iterating and Auto-Committing

Automatic version tracking:

### Version 1

```py
import ell
import random

ell.init(store='./logdir', autocommit=True)

def get_random_adjective():
 adjectives = ["enthusiastic", "cheerful", "warm", "friendly"]
 return random.choice(adjectives)

@ell.simple(model="gpt-4o")
def hello(name: str):
 """You are a helpful assistant."""
 adjective = get_random_adjective()
 return f"Say a {adjective} hello to {name}!"

greeting = hello("Sam Altman")
print(greeting)
```

*Commit:* “Initial version of hello LMP with random adjective selection.”

### Version 2

```py
import ell
import random

ell.init(store='./logdir', autocommit=True)

def get_random_adjective():
 adjectives = ["enthusiastic", "cheerful", "warm", "friendly", "heartfelt", "sincere"]
 return random.choice(adjectives)

def get_random_punctuation():
 return random.choice(["!", "!!", "!!!"])

@ell.simple(model="gpt-4o")
def hello(name: str):
 """You are a helpful and expressive assistant."""
 adjective = get_random_adjective()
 punctuation = get_random_punctuation()
 return f"Say a {adjective} hello to {name}{punctuation}"

greeting = hello("Sam Altman")
print(greeting)
```

*Commit:* “Updated hello LMP: Added more adjectives, introduced random punctuation, and modified system prompt.”

## Comparing Outputs Across Versions

Use ell-studio to compare LMP outputs:

```plaintext
Version 1 output: “Here’s a warm hello to Sam Altman!”
Version 2 output: “Here’s a heartfelt hello to Sam Altman!!!”
```

This helps assess the impact of changes on responses.

## @ell.simple

The `@ell.simple` decorator transforms a function with system and user prompts into a callable that sends prompts to a language model and returns the response. It aims to improve readability, promote reusable components, and enable prompt versioning and tracking.

## Usage

### Using the Docstring as the System Prompt

```py
@ell.simple(model="gpt-4")
def hello(name: str):
 """You are a helpful assistant."""
 return f"Say hello to {name}!"
```

### Explicitly Defining Messages

```py
@ell.simple(model="gpt-4")
def hello(name: str):
 return [
  ell.system("You are a helpful assistant."),
  ell.user(f"Say hello to {name}!")
 ]
```

**Note:** `ell`’s Message API is different from OpenAI’s and offers more flexibility.

## Invoking an ell.simple LMP

Call the function normally to get the model’s response as a string.

```py
hello("world")
```

`@ell.simple` returns a string for simplicity. Use `@ell.complex` for message objects with metadata.

## Variable System Prompts

For variable system prompts, return a list of messages instead of using the docstring.

```py
@ell.simple(model="gpt-4")
def my_func(name: str, var: int):
 return [
  ell.system(f"You are a helpful assistant. {var}"),
  ell.user(f"Say hello to {name}!")
 ]
```

## Passing Parameters to an LLM API

Specify API parameters in the decorator or at runtime.

```py
@ell.simple(model="gpt-4", temperature=0.5, max_tokens=100, stop=["."])
def hello(name: str):
 """You are a helpful assistant."""
 return f"Hey there {name}!"
```

Override parameters during the call:

```py
hello("world", api_params=dict(temperature=0.7))
```

## Multiple Outputs (n>1)

Return a list of strings when `n` is greater than one.

```py
@ell.simple(model="gpt-4", n=2)
def hello(name: str):
 """You are a helpful assistant."""
 return f"Say hello to {name}!"
```

```py
hello("world")
```

Override `n` at runtime:

```py
hello("world", api_params=dict(n=3))
```

**Note:** Future updates may change `api_params` handling based on user feedback.

## Multimodal Inputs

Handle text and images easily with `@ell.simple`.

```py
from PIL import Image
import ell
from ell.types.message import ImageContent

@ell.simple(model="gpt-4-vision-preview")
def describe_image(image: Image.Image):
 return [
  ell.system("You are a helpful assistant that describes images."),
  ell.user(["What's in this image?", image])
  # Or ell.user(["What's in this image?", ImageContent(url=image_url, detail="low")])
 ]

# Usage with PIL Image
image = Image.open("path/to/your/image.jpg")
description = describe_image(image)
print(description)  # This will print a text description of the image
```

**Note:** Not all providers support image URLs. Check your provider’s capabilities.

**Warning:** `@ell.simple` returns text-only outputs. Use `@ell.complex` for multimodal outputs.

## Advanced Features

For multiturn conversations, tools, or structured outputs, use `@ell.complex`.

## Reference

### `ell.simple(model: str, client: Any | None = None, exempt_from_tracking=False, **api_params)`

Creates Language Model Programs (LMPs) for text-only outputs with multimodal inputs.

**Parameters:**

- `model` (str): Language model identifier.
- `client` (Optional[openai.Client]): OpenAI client instance.
- `exempt_from_tracking` (bool): If True, usage isn’t tracked.
- `api_params` (Any): Additional API call parameters.

**Usage Examples:**

```py
@ell.simple(model="gpt-4", temperature=0.7)
def summarize_text(text: str) -> str:
 '''You are an expert at summarizing text.'''
 return f"Please summarize the following text:\n\n{text}"
```

```py
@ell.simple(model="gpt-4", temperature=0.7)
def describe_image(image: PIL.Image.Image) -> List[ell.Message]:
 '''Describe the contents of an image.'''
 return [
  ell.system("You are an AI trained to describe images."),
  ell.user(["Describe this image in detail.", image]),
 ]

image_description = describe_image(PIL.Image.open("https://example.com/image.jpg"))
print(image_description)
# Output: text description of the image

summary = summarize_text("Long text to summarize...")
print(summary)
# Output: text summary
```

**Notes:**

- Designed for text-only outputs, supports multimodal inputs.
- Use `@ell.complex` for preserving complex outputs.
- Returns a list of strings if `n > 1`.
- Pass API parameters in the decorator or function call, with call parameters overriding decorator settings.

**Example of Passing LM API Params:**

```py
@ell.simple(model="gpt-4", temperature=0.7)
def generate_story(prompt: str) -> str:
 return f"Write a short story based on this prompt: {prompt}"

# Using default parameters
story1 = generate_story("A day in the life of a time traveler")

# Overriding parameters during function call
story2 = generate_story("An AI's first day of consciousness", api_params={"temperature": 0.9, "max_tokens": 500})
```

## Versioning & Tracing

Prompt Engineering involves iterating on system, user, and assistant messages to optimize an objective function. This process can be unclear and error-prone without proper versioning and tracking.

### Checkpointing prompts

Analogous to machine learning training, prompt engineering can use checkpoints to save and evaluate prompt versions.

```py
from myother_module import CONSTANT
def other_code():
 print("hello")

def some_other_function():
 return "to bob"

@ell.simple(model="gpt-4o")
def hi():
 """You are a helpful assistant"""
 return f"say hi {some_other_function()} {CONSTANT} times."

def some_other_code():
 return "some other code"
```

### Serializing prompts via lexical closures

Prompts are treated as functions with their dependencies captured through lexical closures.

```py
@ell.simple(model="gpt-4o")
def hi():
 """You are a helpful assistant"""
 return f"say hi {some_other_function()} {CONSTANT} times."
```

### Constructing a dependency graph

Dependencies between prompts are tracked to visualize interactions.

```py
import ell
from typing import List


@ell.simple(model="gpt-4o-mini", temperature=1.0)
def generate_story_ideas(about: str):
 """You are an expert story ideator. Only answer in a single sentence."""
 return f"Generate a story idea about {about}."

@ell.simple(model="gpt-4o-mini", temperature=1.0)
def write_a_draft_of_a_story(idea: str):
 """You are an adept story writer. The story should only be 3 paragraphs."""
 return f"Write a story about {idea}."

@ell.simple(model="gpt-4o", temperature=0.1)
def choose_the_best_draft(drafts: List[str]):
 """You are an expert fiction editor."""
 return f"Choose the best draft from the following list: {'\n'.join(drafts)}."

@ell.simple(model="gpt-4-turbo", temperature=0.2)
def write_a_really_good_story(about: str):
 """You are an expert novelist that writes in the style of Hemmingway. You write in lowercase."""
 ideas = generate_story_ideas(about, api_params=(dict(n=4)))
 drafts = [write_a_draft_of_a_story(idea) for idea in ideas]
 best_draft = choose_the_best_draft(drafts)
 return f"Make a final revision of this story in your voice: {best_draft}."

story = write_a_really_good_story("a dog")
```

## Versioning

Automatic versioning is achieved by initializing ell with a storage parameter, capturing prompt versions and their invocations.

```py
import ell
from ell.stores.sql import SQLiteStore

ell.init(store='./logdir', autocommit=True)

@ell.simple(model="gpt-4o-mini")
def greet(name: str):
 """You are a friendly greeter."""
 return f"Generate a greeting for {name}."

result = greet("Alice")
print(result)  # Output: "Hello, Alice! It's wonderful to meet you."
```

After execution, entries are added to the `SerializedLMP` and `Invocation` tables with relevant details.

## Autocommitting

With `autocommit=True`, ell automatically generates commit messages for prompt versions using GPT-4-mini.

```py
ell.init(store='./logdir', autocommit=True)
```

## Tracing

ell tracks prompt usage by serializing Python code, capturing inputs and outputs without altering the developer workflow.

### Constructing a computation graph

Outputs of prompts are wrapped with tracing objects to build a computation graph of interactions.

```py
import ell

@ell.simple(model="gpt-4o") # version: ae8f32s664200e1
def hi():
 return "say hi"

x = hi() # invocation id: 4hdfjhe8ehf (version: ae8f32s664200e1)
```

Further operations preserve origin traces.

```py
x[0]

x[0].__origin_trace__

x + " there"

(x + " there").__origin_trace__
```

Combining objects merges their traces.

```py
x = hi() # invocation id: 4hdfjhe8ehf
y = hi() # invocation id: 345hef345h
z = x + y
z.__origin_trace__
```

This enables tracking data flow and interactions between prompts.

```py
@ell.simple(model="gpt-4o-2024-08-06", temperature=1.0)
def create_personality() -> str:
 """You are backstoryGPT. You come up with a backstory for a character including name. Choose a completely random name from the list. Format as follows.

Name: <name>
Backstory: <3 sentence backstory>'""" # System prompt

 return "Come up with a backstory about " + random.choice(names_list) # User prompt

def format_message_history(message_history: List[Tuple[str, str]]) -> str:
 return "\n".join([f"{name}: {message}" for name, message in message_history])

@ell.simple(model="gpt-4o-2024-08-06", temperature=0.3, max_tokens=20)
def chat(message_history: List[Tuple[str, str]], *, personality: str):
 return [
  ell.system(f"""Here is your description.
{personality}.

Your goal is to come up with a response to a chat. Only respond in one sentence (should be like a text message in informality.) Never use Emojis."""),
  ell.user(format_message_history(message_history)),
 ]
```

**Note:** Currently, origin tracing in ell works only on string primitives. Support for arbitrary object tracking is in development.

## Studio

Studio is an open-source tool that visualizes and analyzes your Language Model Programs (LMPs), complementing ell’s versioning and tracing capabilities. It runs locally, ensuring data privacy.

With Studio, you can:

- Visualize the evolution of your LMPs over time
- Analyze prompt performance and behavior
- Debug interactions between multiple LMPs
- Collaborate on prompt engineering tasks

## Launching Studio

To start Studio, run:

```bash
ell-studio --storage ./logdir
```

Then access Studio at [http://localhost:5555](http://localhost:5555).

Ensure the storage directory matches the one used with `ell.init(store='./logdir')`.

## Key Features of Studio

### LMP Visualization

Visualize your LMPs and their dependencies to understand interactions and identify optimization areas.

### Version History and Comparison

View the version history of each LMP, perform side-by-side comparisons, and see commit messages to track changes over time.

### Invocation Analysis

Analyze each LMP invocation with details on inputs, outputs, execution time, token usage, and data flow between LMPs.

### Performance Metrics

Monitor performance metrics such as token usage, execution time trends, and invocation frequency to optimize your LMPs.

### LMP Viewer

Examine the source code of your LMPs with the built-in viewer, compare different versions, and access full context easily.

## Messages

Messages are the primary interaction units with chat-based language models, comprising a role and content. Content can include text, images, audio, and other modalities.

## Challenges with LLM APIs

Message objects can be complex, leading to pedantic API specifications. Automatically generated APIs lack user-friendliness, making prompt construction and response handling cumbersome for developers.

```py
result : str = openai.chat.completions.create(
 model="gpt-4",
 messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "What is the capital of the moon?"}
 ]
)["choices"][0]["message"]["content"] # hughkguht this line

result : str my_prompt_engineering_library("prompt")
```

Specifying prompts with multiple content types requires verbosity, as shown below:

```py
result : str = openai.chat.completions.create(
 model="gpt-4",
 messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": [ # highlight these lines
   {"type": "text", "text": "What is the capital of the moon?"},
   {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
  ]}
 ]
)["choices"][0]["message"]["content"]
```

## The ell Message API

The ell API uses Messages and ContentBlocks with type coercion and implicit inference for a better developer experience.

### pydantic model ell.Message

**Fields:**

- `content (List[ell.types.message.ContentBlock])`
- `role (str)`

**Methods:**

- `model_validate(obj: Any) → Message`
- `model_validate_json(json_str: str) → Message`
- `serialize_content(content: List[ContentBlock])`

### pydantic model ell.ContentBlock

**Fields:**

- `audio (numpy.ndarray | List[float] | None)`
- `image (ell.types.message.ImageContent | None)`
- `parsed (pydantic.main.BaseModel | None)`
- `text (ell.types._lstr._lstr | str | None)`
- `tool_call (ell.types.message.ToolCall | None)`
- `tool_result (ell.types.message.ToolResult | None)`

**Methods:**

- `serialize_parsed(value: BaseModel | None, _info)`
- `content property`

## Solving the construction problem

Message and ContentBlock objects use type coercion in their constructors for simpler message creation.

```py
from ell import Message, ContentBlock

message = Message(
 role="user",
 content=[
  ContentBlock(text="What is the capital of the moon?"),
  ContentBlock(image=some_PIL_image_object)
 ]
)
```

Ell can infer content types for concise construction:

```py
message = Message(
 role="user",
 content=["What is the capital of the moon?", some_PIL_image_object]
)
```

For single content types:

```py
message = Message(
 role="user",
 content=some_PIL_image_object
)
```

## Common roles

Ell provides helper functions for common message roles, handling type coercion automatically.

```py
message = ell.user(["What is the capital of the moon?", some_PIL_image_object])
```

### ell.system

Creates a system message.

```py
ell.system(content)
```

### ell.user

Creates a user message.

```py
ell.user(content)
```

### ell.assistant

Creates an assistant message.

```py
ell.assistant(content)
```

## Solving the parsing problem

Ell simplifies parsing complex message structures with convenient functions.

Traditional OpenAI API parsing:

```py
from ell import Message, ContentBlock
import openai

response = openai.ChatCompletion.create(
 model="gpt-5-omni",
 messages=[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": [
   {"type": "text", "text": "Draw me a sketch version of this image"},
   {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
  ]}
 ]
)

message_content = response.choices[0].message.content

has_image = any(content.get('type') == 'image_url' for content in message_content if isinstance(content, dict))
has_text = any(content.get('type') == 'text' for content in message_content if isinstance(content, dict))
has_tool_call = 'function_call' in response.choices[0].message

if has_image:
 image_content = [content['image_url']['url'] for content in message_content if isinstance(content, dict) and content.get('type') == 'image_url']
 show(image_content[0])
if has_text:
 text_content = [content['text'] for content in message_content if isinstance(content, dict) and content.get('type') == 'text']
 print("".joitext_content[0])
if has_tool_call:
 print("The message contains a tool call.")
```

Ell API parsing:

```py
import ell

@ell.complex(model="gpt-5-omni")
def draw_sketch(image: PILImage.Image):
 return [
  ell.system("You are a helpful assistant."),
  ell.user(["Draw me a sketch version of this image", image]),
 ]

response = draw_sketch(some_PIL_image_object)

if response.images:
 show(response.images[0])
if response.text:
 print(response.text)
if response.tool_calls:
 print("The message contains a tool call.")
```

## Message Properties

### Message.text

Returns all text content, replacing non-text with representations.

```py
message = Message(role="user", content=["Hello", PILImage.new('RGB', (100, 100)), "World"])
message.text
'Hello\n<PilImage>\nWorld'
```

### Message.text_only

Returns only text content.

```py
message = Message(role="user", content=["Hello", PILImage.new('RGB', (100, 100)), "World"])
message.text_only
'Hello\nWorld'
```

### Message.tool_calls

Returns all tool calls.

```py
tool_call = ToolCall(tool=lambda x: x, params=BaseModel())
message = Message(role="user", content=["Text", tool_call])
len(message.tool_calls)
1
```

### Message.tool_results

Returns all tool results.

```py
tool_result = ToolResult(tool_call_id="123", result=[ContentBlock(text="Result")])
message = Message(role="user", content=["Text", tool_result])
len(message.tool_results)
1
```

### Message.parsed

Returns all parsed content.

```py
class CustomModel(BaseModel):
 value: int
parsed_content = CustomModel(value=42)
message = Message(role="user", content=["Text", ContentBlock(parsed=parsed_content)])
len(message.parsed)
1
```

### Message.images

Returns all image content.

```py
from PIL import Image as PILImage
image1 = Image(url="https://example.com/image.jpg")
image2 = Image(image=PILImage.new('RGB', (200, 200)))
message = Message(role="user", content=["Text", image1, "More text", image2])
len(message.images)
2
isinstance(message.images[0], Image)
True
message.images[0].url
'https://example.com/image.jpg'
isinstance(message.images[1].image, PILImage.Image)
True
```

### Message.audios

Returns all audio content.

```py
audio1 = np.array([0.1, 0.2, 0.3])
audio2 = np.array([0.4, 0.5, 0.6])
message = Message(role="user", content=["Text", audio1, "More text", audio2])
len(message.audios)
2
```

### Message.call_tools_and_collect_as_message

```py
Message.call_tools_and_collect_as_message(parallel=False, max_workers=None)
```

## @ell.complex

@ell.complex extends @ell.simple to handle multimodal content, structured data, tool usage, and complex interactions with language models. It returns rich `Message` objects for more powerful interactions.

### Note

ell’s `Message` API differs from OpenAI’s dictionary messages, offering a more flexible way to construct and manipulate messages. Learn more on the [Messages page](#).

### Usage

Basic usage is similar to @ell.simple but with enhanced capabilities:

```py
import ell
from pydantic import BaseModel, Field

class MovieReview(BaseModel):
 title: str = Field(description="The title of the movie")
 rating: int = Field(description="The rating of the movie out of 10")
 summary: str = Field(description="A brief summary of the movie")

@ell.complex(model="gpt-4o-2024-08-06", response_format=MovieReview)
def generate_movie_review(movie: str):
 """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
 return f"Generate a review for the movie {movie}"

review_message = generate_movie_review("The Matrix")
review = review_message.parsed
print(f"Movie: {review.title}, Rating: {review.rating}/10")
print(f"Summary: {review.summary}")
```

### Key Features

#### 1. Structured Outputs

Use Pydantic models for structured responses:

```py
@ell.complex(model="gpt-4o-2024-08-06", response_format=MovieReview)
def generate_movie_review(movie: str) -> MovieReview:
 """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
 return f"Generate a review for the movie {movie}"

review_message = generate_movie_review("Inception")
review = review_message.parsed
print(f"Rating: {review.rating}/10")
```

#### 2. Multimodal Interactions

Handle text and images:

```py
from PIL import Image

@ell.complex(model="gpt-5-omni")
def describe_and_generate(prompt: str):
 return [
  ell.system("You can describe images and generate new ones based on text prompts."),
  ell.user(prompt)
 ]

result = describe_and_generate("A serene lake at sunset")
print(result.text)  # Prints the description
if result.images:
 result.images[0].show()  # Displays the generated image
```

#### 3. Chat-based Use Cases

Maintain conversation history:

```py
from ell import Message

@ell.complex(model="gpt-4o", temperature=0.7)
def chat_bot(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("You are a friendly chatbot. Engage in casual conversation."),
 ] + message_history

message_history = []
while True:
 user_input = input("You: ")
 message_history.append(ell.user(user_input))
 response = chat_bot(message_history)
 print("Bot:", response.text)
 message_history.append(response)
```

#### 4. Tool Usage

Enable function calls within the LLM:

```py
@ell.tool()
def get_weather(location: str = Field(description="The full name of a city and country, e.g. San Francisco, CA, USA")):
 """Get the current weather for a given location."""
 # Simulated weather API call
 return f"The weather in {location} is sunny."

@ell.complex(model="gpt-4-turbo", tools=[get_weather])
def travel_planner(destination: str):
 """Plan a trip based on the destination and current weather."""
 return [
  ell.system("You are a travel planner. Use the weather tool to provide relevant advice."),
  ell.user(f"Plan a trip to {destination}")
 ]

result = travel_planner("Paris")
print(result.text)  # Prints travel advice
if result.tool_calls:
 # This is done so that we can pass the tool calls to the language model
 result_message = result.call_tools_and_collect_as_message()
 print("Weather info:", result_message.tool_results[0].text) # Raw text of the tool call.
 print("Message to be sent to the LLM:", result_message.text) # Representation of the message to be sent to the LLM.
```

### Reference

#### `ell.complex(model: str, client: Any | None = None, tools: List[Callable] | None = None, exempt_from_tracking=False, post_callback: Callable | None = None, **api_params)`

Transforms a function into a Language Model Program (LMP) supporting multi-turn conversations, tool usage, and various output formats.

**Parameters:**

- `model` (str): Language model identifier.
- `client` (Optional[openai.Client]): OpenAI client instance.
- `tools` (Optional[List[Callable]]): Tool functions for the LLM.
- `response_format` (Optional[Dict[str, Any]]): Response format.
- `n`, `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, `presence_penalty`, `stop`: LLM parameters.
- `exempt_from_tracking` (bool): Disable tracking if True.
- `post_callback` (Optional[Callable]): Process LLM output before returning.
- `api_params` (Any): Additional API arguments.

**Functionality:**

- Supports multi-turn conversations, tool usage, structured data, and various output formats.
- Handles single prompts, conversation histories, and multimodal inputs.
- Integrates with ell’s tracking system and supports multiple language models.
- Processes outputs through post-callback functions and supports multiple message types.

### Usage Modes and Examples

#### Basic Prompt

```py
@ell.complex(model="gpt-4")
def generate_story(prompt: str) -> List[Message]:
 '''You are a creative story writer''' # System prompt
 return [
  ell.user(f"Write a short story based on this prompt: {prompt}")
 ]

story : ell.Message = generate_story("A robot discovers emotions")
print(story.text)  # Access the text content of the last message
```

#### Multi-turn Conversation

```py
@ell.complex(model="gpt-4")
def chat_bot(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("You are a helpful assistant."),
 ] + message_history

conversation = [
 ell.user("Hello, who are you?"),
 ell.assistant("I'm an AI assistant. How can I help you today?"),
 ell.user("Can you explain quantum computing?")
]
response : ell.Message = chat_bot(conversation)
print(response.text)  # Print the assistant's response
```

#### Tool Usage

```py
@ell.tool()
def get_weather(location: str) -> str:
 # Implementation to fetch weather
 return f"The weather in {location} is sunny."

@ell.complex(model="gpt-4", tools=[get_weather])
def weather_assistant(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("You are a weather assistant. Use the get_weather tool when needed."),
 ] + message_history

conversation = [
 ell.user("What's the weather like in New York?")
]
response : ell.Message = weather_assistant(conversation)

if response.tool_calls:
 tool_results = response.call_tools_and_collect_as_message()
 print("Tool results:", tool_results.text)

 # Continue the conversation with tool results
 final_response = weather_assistant(conversation + [response, tool_results])
 print("Final response:", final_response.text)
```

#### Structured Output

```py
from pydantic import BaseModel

class PersonInfo(BaseModel):
 name: str
 age: int

@ell.complex(model="gpt-4", response_format=PersonInfo)
def extract_person_info(text: str) -> List[Message]:
 return [
  ell.system("Extract person information from the given text."),
  ell.user(text)
 ]

text = "John Doe is a 30-year-old software engineer."
result : ell.Message = extract_person_info(text)
person_info = result.parsed
print(f"Name: {person_info.name}, Age: {person_info.age}")
```

#### Multimodal Input

```py
@ell.complex(model="gpt-4-vision-preview")
def describe_image(image: PIL.Image.Image) -> List[Message]:
 return [
  ell.system("Describe the contents of the image in detail."),
  ell.user([
   ContentBlock(text="What do you see in this image?"),
   ContentBlock(image=image)
  ])
 ]

image = PIL.Image.open("example.jpg")
description = describe_image(image)
print(description.text)
```

#### Parallel Tool Execution

```py
@ell.complex(model="gpt-4", tools=[tool1, tool2, tool3])
def parallel_assistant(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("You can use multiple tools in parallel."),
 ] + message_history

response = parallel_assistant([ell.user("Perform tasks A, B, and C simultaneously.")])
if response.tool_calls:
 tool_results : ell.Message = response.call_tools_and_collect_as_message(parallel=True, max_workers=3)
 print("Parallel tool results:", tool_results.text)
```

### Helper Functions for Output Processing

- `response.text`: Full text content of the last message.
- `response.text_only`: Text content excluding non-text elements.
- `response.tool_calls`: List of tool calls.
- `response.tool_results`: List of tool results.
- `response.structured`: Structured data outputs.
- `response.call_tools_and_collect_as_message()`: Execute tool calls and collect results.
- `Message(role=”user”, content=[…]).to_openai_message()`: Convert to OpenAI API format.

### Notes

- Functions should return a list of `Message` objects.
- Decorate tools with `@ell.tool()`.
- Specify `response_format` for structured outputs.
- @ell.complex includes all features of @ell.simple.
- Use helper functions to access different output types.

## Tool Usage

### Warning

Tool usage in ell is a beta feature and may change. Use cautiously in production.

Tool usage allows language models to interact with external functions and services, enabling dynamic and interactive language model programs (LMPs) that perform actions, retrieve information, and make decisions based on real-time data.

## Defining Tools

Tools are defined using the `@ell.tool()` decorator, which converts a Python function into a tool for language models.

```py
@ell.tool()
def create_claim_draft(claim_details: str,
        claim_type: str,
        claim_amount: float,
        claim_date: str = Field(description="The date of the claim in the format YYYY-MM-DD.")):
 """Create a claim draft. Returns the claim id created."""
 print("Create claim draft", claim_details, claim_type, claim_amount, claim_date)
 return "claim_id-123234"
```

The decorator generates a schema based on the function's signature, annotations, and docstring for the language model.

## Schema Generation

ell uses function inspection and Pydantic models to create the tool schema, which is compatible with the OpenAI API.

```json
{
 "type": "function",
 "function": {
  "name": "create_claim_draft",
  "description": "Create a claim draft. Returns the claim id created.",
  "parameters": {
   "type": "object",
   "properties": {
    "claim_details": {"type": "string"},
    "claim_type": {"type": "string"},
    "claim_amount": {"type": "number"},
    "claim_date": {
     "type": "string",
     "description": "The date of the claim in the format YYYY-MM-DD."
    }
   },
   "required": ["claim_details", "claim_type", "claim_amount", "claim_date"]
  }
 }
}
```

## Using Tools in LMPs

Specify tools in the `@ell.complex` decorator to allow the language model to use them within the LMP.

```py
@ell.complex(model="gpt-4o", tools=[create_claim_draft], temperature=0.1)
def insurance_claim_chatbot(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("""You are an insurance adjuster AI. You are given a dialogue with a user and have access to various tools to effectuate the insurance claim adjustment process. Ask questions until you have enough information to create a claim draft. Then ask for approval."""),
 ] + message_history
```

## Single-Step Tool Usage

The language model uses a tool once during execution, typically involving a single tool call.

```py
@ell.tool()
def get_html_content(
 url: str = Field(description="The URL to get the HTML content of. Never include the protocol (like http:// or https://)"),
):
 """Get the HTML content of a URL."""
 response = requests.get("https://" + url)
 soup = BeautifulSoup(response.text, 'html.parser')
 return soup.get_text()[:100]

@ell.complex(model="gpt-4o", tools=[get_html_content])
def get_website_content(website: str) -> str:
 """You are an agent that can summarize the contents of a website."""
 return f"Tell me what's on {website}"
```

```py
output = get_website_content("new york times front page")

if output.tool_calls: print(output.tool_calls[0]())
```

```py
if output.text_only: print(output.text_only)
```

## Multi-Step Tool Usage

Involves multiple tool calls within a conversation or processing flow.

```py
@ell.complex(model="gpt-4o", tools=[create_claim_draft], temperature=0.1)
def insurance_claim_chatbot(message_history: List[Message]) -> List[Message]:
 return [
  ell.system("""You are an insurance adjuster AI. You are given a dialogue with a user and have access to various tools to effectuate the insurance claim adjustment process. Ask questions until you have enough information to create a claim draft. Then ask for approval."""),
 ] + message_history

message_history = []
user_messages = [
 "Hello, I'm a customer",
 'I broke my car',
 'smashed by someone else, today, $5k',
 'please file it.'
]
for user_message in user_messages:
 message_history.append(ell.user(user_message))
 response_message = insurance_claim_chatbot(message_history)
 message_history.append(response_message)

 if response_message.tool_calls:
  next_message = response_message.call_tools_and_collect_as_message()
  message_history.append(next_message)
  insurance_claim_chatbot(message_history)
```

## Parallel Tool Execution

Allows multiple tool calls to be executed simultaneously for efficiency.

```py
if response.tool_calls:
 tool_results = response.call_tools_and_collect_as_message(parallel=True, max_workers=3)
```

## Future Features: Eager Mode

Eager mode will automatically execute tool calls, streamlining multi-step interactions by handling tool execution behind the scenes.

## Future Features: Tool Spec Autogeneration

Automatically generates tool specifications from function source code using a language model.

```py
def search_twitter(query, n=7):
 # Query must be three words or less
 async def fetch_tweets():
  api = API()
  await api.pool.login_all()
  try:
   tweets = [tweet async for tweet in api.search(query, limit=n)]

   tweet_strings = [
    f"Search Query: {query}\n"
    f"Author: {tweet.user.username}\n"
    f"Tweet: {tweet.rawContent}\n"
    f"Created at: {tweet.date}\n"
    f"Favorites: {tweet.likeCount}\n"
    f"Retweets: {tweet.retweetCount}\n\n\n" for tweet in tweets
   ]
   if tweet_strings:
    print(tweet_strings[0])  # Print the first tweet
   return tweet_strings
  except Exception as e:
   print(f"Error fetching search tweets: {e}")
   return []

 tweets = asyncio.run(fetch_tweets())
 tweets = tweets[:n]
 tweets = "<twitter_results>" + "\n".join(tweets) + "</twitter_results>"
 return tweets
```

```py
@ell.tool(autogenerate=True)
def search_twitter(query, n=7):
 ...
```

```py
{
  "type": "function",
  "function": {
 "name": "search_twitter",
 "description": "Search Twitter for tweets",
 "parameters": {
   "type": "object",
   "properties": {
  "query": {
    "type": "string",
    "description": "The query to search for, this must be three words or less"
  },
  "n": {
    "type": "integer",
    "description": "The number of tweets to return"
  }
   },
   "required": ["query"]
 }
  }
}
```

The tool spec is generated by a language model program:

```py
@ell.simple(model="claude-3-5-sonnet-20241022", temperature=0.0)
def generate_tool_spec(tool_source: str):
 '''
 You are a helpful assistant that takes in source code for a python function and produces a JSON schema for the function.

 Here is an example schema
 {
  "type": "function",
  "function": {
   "name": "some_tool",
   "parameters": {
    "type": "object",
    "properties": {
     "some_arg": {
      "type": "string",
      "description": "This is a description of the argument"
     }
    },
    "required": ["some_arg"]
   }
  }
 }
 '''

 return f"Generate a tool spec for the following function: {tool_source}"
```

```py
auto_tool_spec = json.loads(generate_tool_spec(search_twitter))
```

To use a custom tool spec generator:

```py
@ell.simple
def my_custom_tool_spec_generator(tool_source: str):
 # User implements this once in their code base or repo
 ...

@ell.tool(autogenerate=my_custom_tool_spec_generator)
def search_twitter(query, n=7):
 ...

@ell.complex(model="gpt-4o", tools=[search_twitter])
def my_llm_program(message_history: List[Message]) -> List[Message]:
 ...
```

## Structured Outputs

Structured outputs ensure language model responses are controlled and predictable by adhering to a defined schema. This enhances reliability and simplifies integration into larger systems.

### Defining Structured Outputs with Pydantic

```py
from pydantic import BaseModel, Field

class MovieReview(BaseModel):
 title: str = Field(description="The title of the movie")
 rating: int = Field(description="The rating of the movie out of 10")
 summary: str = Field(description="A brief summary of the movie")

@ell.complex(model="gpt-4o-2024-08-06", response_format=MovieReview)
def generate_movie_review(movie: str) -> MovieReview:
 """You are a movie review generator. Given the name of a movie, you need to return a structured review."""
 return f"generate a review for the movie {movie}"
```

### Using Structured Outputs

```py
# Generate a movie review
message = generate_movie_review("The Matrix")
review = message.parsed

# Access individual fields
print(f"Movie Title: {review.title}")
print(f"Rating: {review.rating}/10")
print(f"Summary: {review.summary}")
```

### Notes

Structured outputs with Pydantic models are available only for the `gpt-4o-2024-08-06` model. For other models, use manual prompting and enable JSON mode.

### Manual Prompting for Other Models

```py
class MovieReview(BaseModel):
 title: str = Field(description="The title of the movie")
 rating: int = Field(description="The rating of the movie out of 10")
 summary: str = Field(description="A brief summary of the movie")

@ell.simple(model="gpt-3.5-turbo")
def generate_movie_review_manual(movie: str):
 return [
  ell.system(f"""You are a movie review generator. Given the name of a movie, you need to return a structured review in JSON format.

You must absolutely respond in this format with no exceptions.
{MovieReview.model_json_schema()}
"""),
  ell.user("Review the movie: {movie}"),
 ]

# parser support coming soon!
unparsed = generate_movie_review_manual("The Matrix")
parsed = MovieReview.model_validate_json(unparsed)
```

## Multimodality

ell supports multimodal interactions, enabling developers to work with text, images, audio, and more within a unified framework.

## The Evolution of Multimodal Interactions

Language models are expanding beyond text. Models like GPT-4 with vision and DALL-E for image generation enable multimodal applications, presenting new opportunities and challenges.

### Example of Traditional API for Multimodal Input

```py
result = openai.ChatCompletion.create(
 model="gpt-4-vision-preview",
 messages=[
  {
   "role": "user",
   "content": [
    {"type": "text", "text": "What's in this image?"},
    {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
   ]
  }
 ]
)
```

## ell’s Approach to Multimodality

ell treats multimodal inputs and outputs as first-class citizens, simplifying their use.

### Simplified Input Construction

ell’s `Message` and `ContentBlock` objects allow intuitive prompt construction.

```py
from PIL import Image
import ell

@ell.simple(model="gpt-4-vision-preview")
def describe_image(image: Image.Image):
 return [
  ell.system("You are a helpful assistant that describes images."),
  ell.user(["What's in this image?", image])
 ]

result = describe_image(some_pil_image) # 'There's a cat in the image'
```

ell handles image conversion automatically, supporting both local images and URLs.

```py
from ell.types.message import ImageContent

@ell.simple(model="gpt-4o-2024-08-06")
def describe_image_from_url(image_url: str):
 return [
  ell.system("You are a helpful assistant that describes images."),
  ell.user(["What's in this image?", ImageContent(url=image_url, detail="low")])
 ]

result = describe_image_from_url("https://example.com/cat.jpg")
```

### Flexible Output Handling

ell provides easy access to different output types.

```py
@ell.complex(model="gpt-5-omni")
def generate_audiovisual_novel(topic: str):
 return [
  ell.system("You are a helpful assistant that can generate audiovisual novels. Output images, text, and audio simultaneously."),
  ell.user("Generate a novel on the topic of {topic}")
 ]

result = generate_audiovisual_novel("A pirate adventure")

if result.images:
 for img in result.images:
  display(img)

if result.text:
 print(result.text)

if result.audios:
 for audio in result.audios:
  play(audio)
```

### Seamless Integration with Python Ecosystem

ell integrates with Python libraries like PIL for image processing.

```py
from PIL import Image, ImageEnhance

def enhance_image(image: Image.Image) -> Image.Image:
 enhancer = ImageEnhance.Contrast(image)
 return enhancer.enhance(1.5)

@ell.complex(model="gpt-4-vision-preview")
def analyze_enhanced_image(image: Image.Image):
 enhanced = enhance_image(image)
 return [
  ell.system("Analyze the enhanced image and describe any notable features."),
  ell.user(enhanced)
 ]
```

### The Power of Multimodal Composition

ell allows composing workflows with multiple modalities seamlessly.

```py
@ell.simple(model="gpt-4o")
def generate_image_caption(image: Image.Image):
 return [
  ell.system("Generate a concise, engaging caption for the image."),
  ell.user(image)
 ]

@ell.complex(model="gpt-4-audio")
def text_to_speech(text: str):
 return [
  ell.system("Convert the following text to speech."),
  ell.user(text)
 ]

@ell.complex(model="gpt-4")
def create_social_media_post(image: Image.Image):
 caption = generate_image_caption(image)
 audio = text_to_speech(caption)

 return [
  ell.system("Create a social media post using the provided image, caption, and audio."),
  ell.user([
   "Image:", image,
   "Caption:", caption,
   "Audio:", audio.audios[0]
  ])
 ]

post = create_social_media_post(some_image)
```

## Conclusion

Multimodality in ell is a core design principle, enabling the creation of sophisticated, multimodal applications effortlessly.

## Models & API Clients

ell manages the relationship between models and API clients, allowing client specification, custom model registration, and default configurations.

### Model Registration and Default Clients

ell auto-registers models from providers like OpenAI, Anthropic, Cohere, and Groq upon initialization, enabling their use without specifying a client.

If no client is found, ell defaults to the OpenAI client, supporting new models without updates. If the model isn't available in the OpenAI API, register your own client using `ell.config.register_model` or specify a client when calling the language model program.

### Specifying Clients for Models

ell offers multiple methods to specify clients for models:

#### Decorator-level Client Specification

```py
import ell
import openai

client = openai.Client(api_key="your-api-key")

@ell.simple(model="gpt-next", client=client)
def my_lmp(prompt: str):
 return f"Respond to: {prompt}"
```

#### Function Call-level Client Specification

```py
result = my_lmp("Hello, world!", client=another_client)
```

#### Global Client Registration

```py
ell.config.register_model("gpt-next", my_custom_client)
```

### Custom Model Registration

For custom or newer models, register them as follows:

```py
import ell
import my_custom_client

ell.config.register_model("my-custom-model", my_custom_client)
```

## Configuration

Customize ELL behavior with various configuration options.

### Initialization

```py
ell.init(
 store: None | str = None,
 verbose: bool = False,
 autocommit: bool = True,
 lazy_versioning: bool = True,
 default_api_params: Dict[str, Any] | None = None,
 default_client: Any | None = None,
 autocommit_model: str = 'gpt-4o-mini'
) → None
```

Initialize ELL with settings.

**Parameters:**

- `store` (Union[Store, str], optional): Store instance or SQLite path.
- `verbose` (bool): Enable verbose logging.
- `autocommit` (bool): Enable autocommit.
- `lazy_versioning` (bool): Enable lazy versioning.
- `default_api_params` (Dict[str, Any], optional): Default API parameters.
- `default_client` (Any | None, optional): Default OpenAI client.
- `autocommit_model` (str): Model for autocommitting.

### Global Configuration

Modify global settings using `ell.config`.

```py
ell.config
```

### Config Class

Pydantic model for configuration.

**Fields:**

- `autocommit` (bool): Enable automatic commits.
- `autocommit_model` (str): Default autocommit model.
- `default_api_params` (Dict[str, Any], optional): Default API parameters.
- `default_client` (openai.OpenAI | None): Default OpenAI client.
- `lazy_versioning` (bool): Enable lazy versioning.
- `override_wrapped_logging_width` (int | None): Override logging width.
- `verbose` (bool): Enable verbose logging.
- `wrapped_logging` (bool): Enable wrapped logging.

### Functions

#### Get Client for Model

```py
get_client_for(model_name: str) → Tuple[Optional[openai.Client], bool]
```

Retrieve the OpenAI client for a specific model.

**Parameters:**

- `model_name` (str): Model name.

**Returns:**

- Tuple containing the client or `None`, and a fallback flag.

#### Get Provider for Client

```py
get_provider_for(client: Type[Any] | Any) → Optional[Provider]
```

Retrieve the provider for a specific client.

**Parameters:**

- `client` (Any): Client instance.

**Returns:**

- Provider instance or `None`.

#### Override Model Registry

```py
model_registry_override(overrides: Dict[str, _Model])
```

Temporarily override the model registry.

**Parameters:**

- `overrides` (Dict[str, ModelConfig]): Model configurations to override.

#### Register Model

```py
register_model(
 name: str,
 default_client: OpenAI | Any | None = None,
 supports_streaming: bool | None = None
) → None
```

Register a new model.

**Parameters:**

- `name` (str): Model name.
- `default_client` (OpenAI | Any | None, optional): Default client.
- `supports_streaming` (bool | None, optional): Streaming support.

#### Register Provider

```py
register_provider(provider: Provider, client_type: Type[Any]) → None
```

Register a provider for a client type.

**Parameters:**

- `provider` (Provider): Provider instance.
- `client_type` (Type[Any]): Client type.
