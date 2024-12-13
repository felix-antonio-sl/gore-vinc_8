## ell package

### _pydantic model_ `ell.Config`

**Bases:** `BaseModel`

Configuration class for `ell`.

**Show JSON schema**

```json
{
	"title": "Config",
	"type": "object",
	"properties": {
		"registry": {
			"additionalProperties": {
				"$ref": "#/$defs/_Model"
			},
			"description": "A dictionary mapping model names to their configurations.",
			"title": "Registry",
			"type": "object"
		},
		"verbose": {
			"default": false,
			"description": "If True, enables verbose logging.",
			"title": "Verbose",
			"type": "boolean"
		},
		"wrapped_logging": {
			"default": true,
			"description": "If True, enables wrapped logging for better readability.",
			"title": "Wrapped Logging",
			"type": "boolean"
		},
		"override_wrapped_logging_width": {
			"anyOf": [
				{ "type": "integer" },
				{ "type": "null" }
			],
			"default": null,
			"description": "If set, overrides the default width for wrapped logging.",
			"title": "Override Wrapped Logging Width"
		},
		"store": {
			"default": null,
			"description": "An optional Store instance for persistence.",
			"title": "Store",
			"type": "null"
		},
		"autocommit": {
			"default": false,
			"description": "If True, enables automatic committing of changes to the store.",
			"title": "Autocommit",
			"type": "boolean"
		},
		"lazy_versioning": {
			"default": true,
			"description": "If True, enables lazy versioning for improved performance.",
			"title": "Lazy Versioning",
			"type": "boolean"
		},
		"default_api_params": {
			"description": "Default parameters for language models.",
			"title": "Default Api Params",
			"type": "object"
		},
		"default_client": {
			"default": null,
			"title": "Default Client"
		},
		"autocommit_model": {
			"default": "gpt-4o-mini",
			"description": "When set, changes the default autocommit model from GPT 4o mini.",
			"title": "Autocommit Model",
			"type": "string"
		},
		"providers": {
			"default": null,
			"title": "Providers"
		}
	},
	"$defs": {
		"_Model": {
			"properties": {
				"name": {
					"title": "Name",
					"type": "string"
				},
				"default_client": {
					"anyOf": [
						{},
						{ "type": "null" }
					],
					"default": null,
					"title": "Default Client"
				},
				"supports_streaming": {
					"anyOf": [
						{ "type": "boolean" },
						{ "type": "null" }
					],
					"default": null,
					"title": "Supports Streaming"
				}
			},
			"required": ["name"],
			"title": "_Model",
			"type": "object"
		}
	}
}
```

#### Config

- `arbitrary_types_allowed`: `bool = True`
- `protected_namespaces`: `tuple = ('protect_',)`

#### Fields

| Field| Type| Default| Description|
|-|-|-|-|
| `autocommit`| `bool`| `False`| Enables automatic committing to the store.|
| `autocommit_model`| `str`| `'gpt-4o-mini'`| Changes the default autocommit model.|
| `default_api_params`| `Dict[str, Any]`, optional| `None`| Default parameters for language models.|
| `default_client`| `OpenAI| None`| `None`| Default OpenAI client.|
| `lazy_versioning`| `bool`| `True`| Enables lazy versioning.|
| `override_wrapped_logging_width`| `int| None`| `None`| Overrides default width for wrapped logging.|
| `providers`| `Dict[Type, Provider]`, optional| `None`| Maps client types to providers.|
| `registry`| `Dict[str, _Model]`, optional| `None`| Maps model names to configurations.|
| `store`| `None`| `None`| Optional Store instance.|
| `verbose`| `bool`| `False`| Enables verbose logging.|
| `wrapped_logging`| `bool`| `True`| Enables wrapped logging.|

#### Methods

- `get_client_for(model_name: str) → Tuple[Optional[openai.Client], bool]`	
	Get the OpenAI client for a model.

	Parameters:
	- `model_name` (`str`)

	Returns:
	- `Tuple[Optional[openai.Client], bool]`

- `get_provider_for(client: Type[Any]| Any) → Provider| None`	
	Get the provider for a client.

	Parameters:
	- `client` (`Any`)

	Returns:
	- `Optional[Provider]`

- `model_registry_override(overrides: Dict[str, _Model])`	
	Override the model registry.

	Parameters:
	- `overrides` (`Dict[str, ModelConfig]`)

- `register_model(name: str, default_client: OpenAI| Any| None = None, supports_streaming: bool| None = None) → None`	
	Register a model.

- `register_provider(provider: Provider, client_type: Type[Any]) → None`	
	Register a provider for a client type.

	Parameters:
	- `provider_class` (`Type[Provider]`)

### _pydantic model_ `ell.ContentBlock`

**Bases:** `BaseModel`

**Show JSON schema**

```json
{
	"title": "ContentBlock",
	"type": "object",
	"properties": {
		"text": {
			"anyOf": [
				{
					"properties": {
						"content": {
							"title": "Content",
							"type": "string"
						},
						"__origin_trace__": {
							"title": "Origin Trace",
							"type": "string"
						},
						"__lstr": {
							"title": "Lstr",
							"type": "boolean"
						}
					},
					"required": ["content", "__origin_trace__", "__lstr"],
					"type": "object"
				},
				{ "type": "string" },
				{ "type": "null" }
			],
			"default": null,
			"title": "Text"
		},
		"image": {
			"default": null,
			"title": "Image"
		},
		"audio": {
			"anyOf": [
				{ "items": { "type": "number" }, "type": "array" },
				{ "type": "null" }
			],
			"default": null,
			"title": "Audio"
		},
		"tool_call": {
			"default": null,
			"title": "Tool Call"
		},
		"parsed": {
			"anyOf": [
				{ "$ref": "#/$defs/BaseModel" },
				{ "type": "null" }
			],
			"default": null
		},
		"tool_result": {
			"default": null,
			"title": "Tool Result"
		}
	},
	"$defs": {
		"BaseModel": {
			"properties": {},
			"title": "BaseModel",
			"type": "object"
		}
	}
}
```

#### Config

- `arbitrary_types_allowed`: `bool = True`

#### Fields

| Field| Type| Default| Description|
|-|-|-|-|
| `audio`| `numpy.ndarray| List[float]| None`| Validated by `check_single_non_null`|
| `image`| `ImageContent| None`| `None`| Validated by `check_single_non_null`|
| `parsed`| `BaseModel| None`| `None`| Validated by `check_single_non_null`|
| `text`| `lstr| str| None`| Validated by `check_single_non_null`|
| `tool_call`| `ToolCall| None`| `None`| Validated by `check_single_non_null`|
| `tool_result`| `ToolResult| None`| `None`| Validated by `check_single_non_null`|

#### Validators

- `check_single_non_null` » `all fields`

#### Class Methods

- `coerce(content: ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel) → ContentBlock`	
	Convert various types into a `ContentBlock`.

	Args:
	- `content`: Content to convert.

	Returns:
	- `ContentBlock`

	Raises:
	- `ValueError`

	Examples:

	```py
	>>> ContentBlock.coerce("Hello, world!")
	ContentBlock(text="Hello, world!")
	```

	```py
	>>> tool_call = ToolCall(...)
	>>> ContentBlock.coerce(tool_call)
	ContentBlock(tool_call=tool_call)
	```

	```py
	>>> tool_result = ToolResult(...)
	>>> ContentBlock.coerce(tool_result)
	ContentBlock(tool_result=tool_result)
	```

	```py
	>>> class MyModel(BaseModel):
	...		 field: str
	>>> model_instance = MyModel(field="value")
	>>> ContentBlock.coerce(model_instance)
	ContentBlock(parsed=model_instance)
	```

	```py
	>>> from PIL import Image as PILImage
	>>> img = PILImage.new('RGB', (100, 100))
	>>> ContentBlock.coerce(img)
	ContentBlock(image=ImageContent(image=<PIL.Image.Image object>))
	```

	```py
	>>> import numpy as np
	>>> arr = np.random.rand(100, 100, 3)
	>>> ContentBlock.coerce(arr)
	ContentBlock(image=ImageContent(image=<PIL.Image.Image object>))
	```

	```py
	>>> image = Image(url="https://example.com/image.jpg")
	>>> ContentBlock.coerce(image)
	ContentBlock(image=ImageContent(url="https://example.com/image.jpg"))
	```

- `serialize_parsed(value: BaseModel| None, info)`
- `_property_ content`
- `_property_ type`

### _pydantic model_ `ell.Message`

**Bases:** `BaseModel`

**Show JSON schema**

```json
{
	"title": "Message",
	"type": "object",
	"properties": {
		"role": {
			"title": "Role",
			"type": "string"
		},
		"content": {
			"default": null,
			"title": "Content"
		}
	},
	"required": ["role"]
}
```

#### Fields

| Field| Type| Required| Description|
|-|-|-|-|
| `content`| `List[ContentBlock]`| Yes||
| `role`| `str`| Yes||

#### Class Methods

- `model_validate(obj: Any) → Message`	
	Validate deserialization.

- `model_validate_json(json_str: str) → Message`	
	Validate from JSON string.

- `serialize_content(content: List[ContentBlock])`	
	Serialize content blocks for JSON.

#### Properties

- `audios: List[ndarray| List[float]]`	
	List of audio content.

	Example:

	```py
	>>> audio1 = np.array([0.1, 0.2, 0.3])
	>>> audio2 = np.array([0.4, 0.5, 0.6])
	>>> message = Message(role="user", content=["Text", audio1, "More text", audio2])
	>>> len(message.audios)
	2
	```

- `images: List[ImageContent]`	
	List of image content.

	Example:

	```py
	>>> from PIL import Image as PILImage
	>>> image1 = Image(url="https://example.com/image.jpg")
	>>> image2 = Image(image=PILImage.new('RGB', (200, 200)))
	>>> message = Message(role="user", content=["Text", image1, "More text", image2])
	>>> len(message.images)
	2
	>>> isinstance(message.images[0], Image)
	True
	>>> message.images[0].url
	'https://example.com/image.jpg'
	>>> isinstance(message.images[1].image, PILImage.Image)
	True
	```

- `parsed: BaseModel| List[BaseModel]`	
	List of parsed content.

	Example:

	```py
	>>> class CustomModel(BaseModel):
	...		 value: int
	>>> parsed_content = CustomModel(value=42)
	>>> message = Message(role="user", content=["Text", ContentBlock(parsed=parsed_content)])
	>>> len(message.parsed)
	1
	```

- `text: str`	
	All text content with representations for non-text.

	Example:

	```py
	>>> message = Message(role="user", content=["Hello", PILImage.new('RGB', (100, 100)), "World"])
	>>> message.text
	'Hello\n<PilImage>\nWorld'
	```

- `text_only: str`	
	Only text content.

	Example:

	```py
	>>> message = Message(role="user", content=["Hello", PILImage.new('RGB', (100, 100)), "World"])
	>>> message.text_only
	'Hello\nWorld'
	```

- `tool_calls: List[ToolCall]`	
	List of tool calls.

	Example:

	```py
	>>> tool_call = ToolCall(tool=lambda x: x, params=BaseModel())
	>>> message = Message(role="user", content=["Text", tool_call])
	>>> len(message.tool_calls)
	1
	```

- `tool_results: List[ToolResult]`	
	List of tool results.

	Example:

	```py
	>>> tool_result = ToolResult(tool_call_id="123", result=[ContentBlock(text="Result")])
	>>> message = Message(role="user", content=["Text", tool_result])
	>>> len(message.tool_results)
	1
	```

### `ell.assistant(content: ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel| List[ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel]) → Message`

Create an assistant message.

**Args:**
- `content` (`str`)

**Returns:**
- `Message`

### `ell.complex(model: str, client: Any| None = None, tools: List[Callable]| None = None, exempt_from_tracking=False, post_callback: Callable| None = None, api_params)`

Decorator for complex LLM interactions.

#### Parameters

| Parameter| Type| Description|
|-|-|-|
| `model`| `str`| Language model name.|
| `client`| `Optional[openai.Client]`| OpenAI client instance.|
| `tools`| `Optional[List[Callable]]`| Tool functions for the LLM.|
| `response_format`| `Optional[Dict[str, Any]]`| Response format.|
| `n`| `Optional[int]`| Number of responses.|
| `temperature`| `Optional[float]`| Controls randomness.|
| `max_tokens`| `Optional[int]`| Max tokens to generate.|
| `top_p`| `Optional[float]`| Diversity control.|
| `frequency_penalty`| `Optional[float]`| Controls repetition.|
| `presence_penalty`| `Optional[float]`| Controls relevance.|
| `stop`| `Optional[List[str]]`| Stop sequences.|
| `exempt_from_tracking`| `bool`| Disable tracking.|
| `post_callback`| `Optional[Callable]`| Process LLM output.|
| `api_params`| `Any`| Additional API parameters.|

**Returns:**
- `Callable`

#### Functionality

1. Multi-turn conversations.
2. Tool usage.
3. Various output formats.
4. Integration with tracking.
5. Output processing.

#### Usage Modes and Examples

1. Basic Prompt:

		```py
		@ell.complex(model="gpt-4")
		def generate_story(prompt: str) -> List[Message]:
				'''You are a creative story writer'''
				return [
						ell.user(f"Write a short story based on this prompt: {prompt}")
				]

		story: ell.Message = generate_story("A robot discovers emotions")
		print(story.text)	# Access the text content of the last message
		```

2. Multi-turn Conversation:

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

		response: ell.Message = chat_bot(conversation)
		print(response.text)	# Print the assistant's response
		```

3. Tool Usage:

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

		response: ell.Message = weather_assistant(conversation)

		if response.tool_calls:
				tool_results = response.call_tools_and_collect_as_message()
				print("Tool results:", tool_results.text)	# Continue with tool results
				final_response = weather_assistant(conversation + [response, tool_results])
				print("Final response:", final_response.text)
		```

4. Structured Output:

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
		result: ell.Message = extract_person_info(text)
		person_info = result.parsed
		print(f"Name: {person_info.name}, Age: {person_info.age}")
		```

5. Multimodal Input:

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

6. Parallel Tool Execution:

		```py
		@ell.complex(model="gpt-4", tools=[tool1, tool2, tool3])
		def parallel_assistant(message_history: List[Message]) -> List[Message]:
				return [
						ell.system("You can use multiple tools in parallel."),
				] + message_history

		response = parallel_assistant([ell.user("Perform tasks A, B, and C simultaneously.")])

		if response.tool_calls:
				tool_results: ell.Message = response.call_tools_and_collect_as_message(parallel=True, max_workers=3)
				print("Parallel tool results:", tool_results.text)
		```

#### Helper Functions for Output Processing

- `response.text`: Get full text of the last message.
- `response.text_only`: Get only text content.
- `response.tool_calls`: List of tool calls.
- `response.tool_results`: List of tool results.
- `response.structured`: Access structured data.
- `response.call_tools_and_collect_as_message()`: Execute tools and collect results.
- `Message(role="user", content=[…]).to_openai_message()`: Convert to OpenAI format.

**Notes:**

- Decorated functions return `List[Message]`.
- Use `@ell.tool()` for tools.
- Use `response_format` for structured outputs.
- `@ell.complex` supports `@ell.simple`.
- Utilize helper functions for output processing.

**See Also:**

- [`ell.simple`](#ell.simple)
- [`ell.tool`](#ell.tool)
- `ell.studio`

### `ell.get_store() → None`

### `ell.init(store: None| str = None, verbose: bool = False, autocommit: bool = True, lazy_versioning: bool = True, default_api_params: Dict[str, Any]| None = None, default_client: Any| None = None, autocommit_model: str = 'gpt-4o-mini') → None`

Initialize `ell` configuration.

#### Parameters

| Parameter| Type| Description|
|-|-|-|
| `verbose`| `bool`| Set verbosity.|
| `store`| `Union[Store, str]`, optional| Set the store (`Store` instance or `SQLiteStore` path).|
| `autocommit`| `bool`| Enable autocommit.|
| `lazy_versioning`| `bool`| Enable lazy versioning.|
| `default_api_params`| `Dict[str, Any]`, optional| Default API parameters.|
| `default_openai_client`| `openai.Client`, optional| Default OpenAI client.|
| `autocommit_model`| `str`| Model for autocommitting.|

### `ell.register_provider(provider: Provider, client_type: Type[Any]) → None`

### `ell.set_store(*args, **kwargs) → None`

### `ell.simple(model: str, client: Any| None = None, exempt_from_tracking=False, api_params)`

Simpler decorator for text-only LMPs.

#### Parameters

| Parameter| Type| Description|
|-|-|-|
| `model`| `str`| Language model name.|
| `client`| `Optional[openai.Client]`| OpenAI client instance.|
| `exempt_from_tracking`| `bool`| Disable tracking.|
| `api_params`| `Any`| Additional API parameters.|

**Usage:**

```py
@ell.simple(model="gpt-4", temperature=0.7)
def summarize_text(text: str) -> str:
		'''You are an expert at summarizing text.'''
		return f"Please summarize the following text:\n\n{text}"	# User prompt

@ell.simple(model="gpt-4", temperature=0.7)
def describe_image(image: PIL.Image.Image) -> List[ell.Message]:
		'''Describe the contents of an image.'''
		return [
				ell.system("You are an AI trained to describe images."),
				ell.user(["Describe this image in detail.", image]),
		]

image_description = describe_image(PIL.Image.open("https://example.com/image.jpg"))
print(image_description)	# Text-only description

summary = summarize_text("Long text to summarize...")
print(summary)	# Text-only summary
```

**Notes:**

- For text-only outputs, supports multimodal inputs.
- Use `@ell.complex` for structured outputs.
- Returns string or `List[Message]`.
- `n > 1` returns list of strings.
- API params can be set in decorator or call.

**Example of passing LM API params:**

```py
@ell.simple(model="gpt-4", temperature=0.7)
def generate_story(prompt: str) -> str:
		return f"Write a short story based on this prompt: {prompt}"	# Using default parameters

story1 = generate_story("A day in the life of a time traveler")

# Overriding parameters during function call
story2 = generate_story(
		"An AI's first day of consciousness",
		api_params={"temperature": 0.9, "max_tokens": 500}
)
```

**See Also:**

- [`ell.complex()`](#ell.complex)
- [`ell.tool()`](#ell.tool)
- `ell.studio`

### `ell.system(content: ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel| List[ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel]) → Message`

Create a system message.

**Args:**
- `content` (`str`)

**Returns:**
- `Message`

### `ell.tool(*, exempt_from_tracking: bool = False, tool_kwargs)`

Define a tool for LMPs.

#### Parameters

| Parameter| Type| Description|
|-|-|-|
| `exempt_from_tracking`| `bool`| Disable tracking.|
| `tool_kwargs`| `Any`| Additional tool config.|

**Returns:**
- `Callable`

#### Requirements

- Fully typed arguments.
- Return types: `str`, JSON-serializable, Pydantic model, or `List[ContentBlock]`.
- Type annotations.
- Descriptive docstring.
- Use with `@ell.complex`.

#### Functionality

1. Extract metadata from docstring and annotations.
2. Integrate with LMs.
3. Handle invocation, tracking, and results.

#### Usage Modes

1. Normal Function Call:

		```py
		result = my_tool(arg1="value", arg2=123)
		```

2. LMP Tool Call:

		```py
		result = my_tool(arg1="value", arg2=123, tool_call_id="unique_id")
		```

#### Result Coercion

- `String → ContentBlock(text=result)`
- `Pydantic BaseModel → ContentBlock(parsed=result)`
- `List[ContentBlock] → Used as-is`
- `Other types → ContentBlock(text=json.dumps(result))`

**Example:**

```py
@ell.tool()
def create_claim_draft(
		claim_details: str,
		claim_type: str,
		claim_amount: float,
		claim_date: str = Field(description="Date format: YYYY-MM-DD")
) -> str:
		'''Create a claim draft. Returns the created claim ID.'''
		return "12345"

# For use in a complex LMP:
@ell.complex(model="gpt-4", tools=[create_claim_draft], temperature=0.1)
def insurance_chatbot(message_history: List[Message]) -> List[Message]:
		# Chatbot implementation...
		x = insurance_chatbot([
				ell.user("I crashed my car into a tree."),
				ell.assistant("I'm sorry to hear that. Can you provide more details?"),
				ell.user("The car is totaled and I need to file a claim. Happened on 2024-08-01. total value is like $5000")
		])
		print(x)
		'''ell.Message(content=[
				ContentBlock(
						tool_call(
								tool_call_id="asdas4e",
								tool_fn=create_claim_draft,
								input=create_claim_draftParams({
										claim_details="The car is totaled and I need to file a claim. Happened on 2024-08-01. total value is like $5000",
										claim_type="car",
										claim_amount=5000,
										claim_date="2024-08-01"
								})
						)
				)
		], role='assistant')'''

		if x.tool_calls:
				next_user_message = response_message.call_tools_and_collect_as_message()	# Calls create_claim_draft
				print(next_user_message)
				'''ell.Message(content=[
						ContentBlock(
								tool_result=ToolResult(
										tool_call_id="asdas4e",
										result=[ContentBlock(text="12345")]
								)
						)
				], role='user')'''
				y = insurance_chatbot(message_history + [x, next_user_message])
				print(y)
				'''ell.Message("I've filed that for you!", role='assistant')'''
```

**Notes:**

- Integrate tools via `tools` in `@ell.complex`.
- LMs receive structured tool information.

### `ell.user(content: ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel| List[ContentBlock| str| ToolCall| ToolResult| ImageContent| ndarray| Image| BaseModel]) → Message`

Create a user message.

**Args:**
- `content` (`str`)

**Returns:**
- `Message`