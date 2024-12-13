# htmx in a Nutshell

htmx enables modern browser features directly from HTML without JavaScript.

## Example Anchor Tag

```html
<a href="/blog">Blog</a>
```

This issues a GET request to `/blog` and loads the response.

## htmx Button Example

```html
<button hx-post="/clicked"
    hx-trigger="click"
    hx-target="#parent-div"
    hx-swap="outerHTML">
    Click Me!
</button>
```

This sends a POST request to `/clicked` on click and replaces `#parent-div` with the response.

htmx allows:
- Any element to issue HTTP requests
- Any event to trigger requests
- Any HTTP verb
- Any target element for updates

Respond with HTML on the server side.

Use the `data-` prefix:

```html
<a data-hx-post="/click">Click Me!</a>
```

Version 1 supports IE11.

## 1.x to 2.x Migration Guide

Refer to the htmx 1.x migration guide or the intercooler migration guide.

## Installing

### Via A CDN (e.g. unpkg.com)

```html
<script src="https://unpkg.com/htmx.org@2.0.3" integrity="sha384-0895/pl2MU10Hqc6jd4RvrthNlDiE9U1tWmX7WRESftEDRosgxNsQG/Ze9YMRzHq" crossorigin="anonymous"></script>
```

Unminified version:

```html
<script src="https://unpkg.com/htmx.org@2.0.3/dist/htmx.js" integrity="sha384-BBDmZzVt6vjz5YbQqZPtFZW82o8QotoM7RUp5xOxV3nSJ8u2pSdtzFAbGKzTlKtg" crossorigin="anonymous"></script>
```

### Download a copy

```html
<script src="/path/to/htmx.min.js"></script>
```

### npm

```bash
npm install htmx.org@2.0.3
```

### Webpack

1. Install via npm or yarn
2. Import in `index.js`:

    ```javascript
    import 'htmx.org';
    ```

3. Inject into window scope:

    ```javascript
    window.htmx = require('htmx.org');
    ```

4. Rebuild your bundle

## AJAX

htmx uses attributes to issue AJAX requests:

| Attribute | Description |
|-----------|-------------|
| `hx-get`  | GET request to the URL |
| `hx-post` | POST request to the URL |
| `hx-put`  | PUT request to the URL |
| `hx-patch`| PATCH request to the URL |
| `hx-delete`| DELETE request to the URL |

Example:

```html
<button hx-put="/messages">
    Put To Messages
</button>
```

Issues a PUT request to `/messages` on click.

## Triggering Requests

By default, triggers are:
- `change` for `input`, `textarea`, `select`
- `submit` for `form`
- `click` for others

Use `hx-trigger` for different events:

```html
<div hx-post="/mouse_entered" hx-trigger="mouseenter">
    [Here Mouse, Mouse!]
</div>
```

### Trigger Modifiers

Modifiers alter trigger behavior:

```html
<div hx-post="/mouse_entered" hx-trigger="mouseenter once">
    [Here Mouse, Mouse!]
</div>
```

Other modifiers:
- `changed`
- `delay:<time>`
- `throttle:<time>`
- `from:<selector>`

Example Active Search:

```html
<input type="text" name="q"
    hx-get="/trigger_delay"
    hx-trigger="keyup changed delay:500ms"
    hx-target="#search-results"
    placeholder="Search...">
<div id="search-results"></div>
```

### Trigger Filters

Use conditions to trigger:

```html
<div hx-get="/clicked" hx-trigger="click[ctrlKey]">
    Control Click Me
</div>
```

### Special Events

htmx special events:
- `load`
- `revealed`
- `intersect`

## Polling

Use `every` with `hx-trigger`:

```html
<div hx-get="/news" hx-trigger="every 2s"></div>
```

### Load Polling

```html
<div hx-get="/messages"
    hx-trigger="load delay:1s"
    hx-swap="outerHTML">
</div>
```

## Request Indicators

Use `htmx-indicator` class:

```html
<button hx-get="/click">
    Click Me!
    <img class="htmx-indicator" src="/spinner.gif">
</button>
```

Custom CSS:

```css
.htmx-indicator{
    display:none;
}
.htmx-request .htmx-indicator{
    display:inline;
}
```

Specify different indicator:

```html
<div>
    <button hx-get="/click" hx-indicator="#indicator">
        Click Me!
    </button>
    <img id="indicator" class="htmx-indicator" src="/spinner.gif"/>
</div>
```

## Targets

Use `hx-target` to specify where to load the response:

```html
<input type="text" name="q"
    hx-get="/trigger_delay"
    hx-trigger="keyup delay:500ms changed"
    hx-target="#search-results"
    placeholder="Search...">
<div id="search-results"></div>
```

### Extended CSS Selectors

Supports:
- `this`
- `closest <selector>`
- `next <selector>`
- `previous <selector>`
- `find <selector>`

## Swapping

Use `hx-swap` to define swap behavior:

| Name        | Description |
|-------------|-------------|
| `innerHTML` | Default, inserts content inside target |
| `outerHTML` | Replaces target element |
| `afterbegin`| Prepends content inside target |
| `beforebegin`| Inserts before target |
| `beforeend` | Appends content inside target |
| `afterend` | Inserts after target |
| `delete`    | Deletes target element |
| `none`      | No content swap |

## Morph Swaps

Use extensions for morphing swaps to merge content:

- Idiomorph
- Morphdom Swap
- Alpine-morph

## View Transitions

Experimental API for animated transitions. Falls back if unsupported.

Enable globally:

```javascript
htmx.config.globalViewTransitions = true
```

Or per swap:

```html
<button hx-post="/example" hx-swap="morph transition:true" hx-target="#content">
    Update Content
</button>
```

## Swap Options

Modify swap behavior with modifiers:

```html
<button hx-post="/like" hx-swap="outerHTML ignoreTitle:true">Like</button>
```

Modifiers include:
- `transition`
- `swap`
- `settle`
- `ignoreTitle`
- `scroll`
- `show`

## Synchronization

Use `hx-sync` to coordinate requests:

```html
<form hx-post="/store">
    <input id="title" name="title" type="text"
        hx-post="/validate"
        hx-trigger="change"
        hx-sync="closest form:abort">
    <button type="submit">Submit</button>
</form>
```

Programmatically abort requests:

```html
<button id="request-button" hx-post="/example">
    Issue Request
</button>
<button onclick="htmx.trigger('#request-button', 'htmx:abort')">
    Cancel Request
</button>
```

## CSS Transitions

Maintain stable `id` across swaps and use CSS transitions:

```html
<div id="div1">Original Content</div>
```

```css
.red {
    color: red;
    transition: all ease-in 1s;
}
```

## Out of Band Swaps

Use `hx-swap-oob` in response HTML:

```html
<div id="message" hx-swap-oob="true">Swap me directly!</div>
```

### Additional Content

Swaps `div#message` directly while updating normally.

## Troublesome Tables

Use `template` tag for table elements:

```html
<template>
  <tr id="message" hx-swap-oob="true"><td>Joe</td><td>Smith</td></tr>
</template>
```

## Selecting Content To Swap

Use `hx-select` to choose content:

Use `hx-select-oob` for out-of-band swaps.

## Preserving Content During A Swap

Use `hx-preserve` on elements to keep them intact.

## Parameters

Elements include their values. Forms include all inputs.

Use `hx-include` to add more elements. Use `hx-params` to filter.

Modify parameters with `htmx:configRequest` event.

## File Upload

Set `hx-encoding` to `multipart/form-data`:

```html
<form hx-post="/upload" hx-encoding="multipart/form-data">
    <input type="file" name="file">
</form>
```

Handle progress with `htmx:xhr:progress` event.

## Extra Values

Use `hx-vals` and `hx-vars` to add extra data.

## Confirming Requests

Use `hx-confirm` for confirmation dialogs:

```html
<button hx-delete="/account" hx-confirm="Are you sure you wish to delete your account?">
    Delete My Account
</button>
```

### Confirming with Events

Handle `htmx:confirm` event for custom dialogs:

```javascript
document.body.addEventListener('htmx:confirm', function(evt) {
  if (evt.target.matches("[confirm-with-sweet-alert='true']")) {
    evt.preventDefault();
    swal({
      title: "Are you sure?",
      text: "Are you sure you are sure?",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then((confirmed) => {
      if (confirmed) {
        evt.detail.issueRequest();
      }
    });
  }
});
```

## Attribute Inheritance

Attributes like `hx-confirm` are inherited by child elements:

```html
<div hx-confirm="Are you sure?">
    <button hx-delete="/account">
        Delete My Account
    </button>
    <button hx-put="/account">
        Update My Account
    </button>
</div>
```

Override inheritance:

```html
<button hx-confirm="unset" hx-get="/">
    Cancel
</button>
```

Disable inheritance globally with `htmx.config.disableInheritance`.

## Boosting

Use `hx-boost` to make links and forms use AJAX:

```html
<div hx-boost="true">
    <a href="/blog">Blog</a>
</div>
```

## Progressive Enhancement

`hx-boost` degrades gracefully without JavaScript.

Example with form:

```html
<form action="/search" method="POST">
    <input class="form-control" type="search"
        name="search" placeholder="Begin typing to search users..."
        hx-post="/search"
        hx-trigger="keyup changed delay:500ms, search"
        hx-target="#search-results"
        hx-indicator=".htmx-indicator">
</form>
```

Ensure server handles `HX-Request` header.

## Web Sockets & SSE

Supported via extensions. Refer to SSE and WebSocket extension pages.

## History Support

Use `hx-push-url` to manage browser history:

```html
<a hx-get="/blog" hx-push-url="true">Blog</a>
```

Ensure server can handle direct URL access.

## Specifying History Snapshot Element

Use `hx-history-elt` to define snapshot element:

```html
<div hx-history-elt="#snapshot">
    ...
</div>
```

## Undoing DOM Mutations By 3rd Party Libraries

Clean DOM before history save:

```javascript
htmx.on('htmx:beforeHistorySave', function() {
    document.querySelectorAll('.tomSelect')
        .forEach(elt => elt.tomselect.destroy());
});
```

## Disabling History Snapshots

Set `hx-history="false"` to exclude from history cache.

## Requests & Responses

Responses should be HTML. Use `204 - No Content` to do nothing.

Handle errors with events:

- `htmx:responseError`
- `htmx:sendError`

## Configuring Response Handling

Define `htmx.config.responseHandling`:

```javascript
responseHandling: [
    {code:"204", swap: false},
    {code:"[23]..", swap: true},
    {code:"[45]..", swap: false, error:true},
    {code:"...", swap: false}
]
```

## Configuring Response Handling Examples

Handle `422` responses:

```html
<meta
    name="htmx-config"
    content='{
        "responseHandling":[
            {"code":"204", "swap": false},
            {"code":"[23]..", "swap": true},
            {"code":"422", "swap": true},
            {"code":"[45]..", "swap": false, "error":true},
            {"code":"...", "swap": true}
        ]
    }'
/>
```

Swap all responses:

```html
<meta name="htmx-config" content='{"responseHandling": [{"code":".*", "swap": true}]}' />
```

## CORS

Set Access-Control headers for cross-origin htmx requests:
- `Access-Control-Allow-Headers`
- `Access-Control-Expose-Headers`

## Request Headers

htmx includes headers like:
- `HX-Boosted`
- `HX-Current-URL`
- `HX-History-Restore-Request`
- `HX-Prompt`
- `HX-Request`
- `HX-Target`
- `HX-Trigger-Name`
- `HX-Trigger`

## Response Headers

htmx response headers:
- `HX-Location`
- `HX-Push-Url`
- `HX-Redirect`
- `HX-Refresh`
- `HX-Replace-Url`
- `HX-Reswap`
- `HX-Retarget`
- `HX-Reselect`
- `HX-Trigger`
- `HX-Trigger-After-Settle`
- `HX-Trigger-After-Swap`

## Request Order of Operations

1. Trigger and start request
2. Gather values
3. Apply `htmx-request` class
4. Issue AJAX request
5. Mark target with `htmx-swapping`
6. Apply swap delay
7. Perform swap
8. Remove `htmx-swapping`
9. Add `htmx-added`
10. Apply `htmx-settling`
11. Settle delay
12. Settle DOM
13. Remove `htmx-settling`
14. Remove `htmx-added`

## Validation

htmx respects HTML5 Validation API. Use `hx-validate="true"` for non-form elements.

### Validation Example

```html
<form id="example-form" hx-post="/test">
    <input name="example"
           onkeyup="this.setCustomValidity('')"
           hx-on:htmx:validation:validate="if(this.value != 'foo') {
                    this.setCustomValidity('Please enter the value foo')
                    htmx.find('#example-form').reportValidity()
                }">
</form>
```

## Animations

Use CSS transitions with stable `id` across swaps.

## Extensions

Enable extensions with `hx-ext`:

```html
<head>
  <script src="https://unpkg.com/idiomorph@0.3.0/dist/idiomorph-ext.min.js"></script>
</head>
<body hx-ext="morph">
  <button hx-post="/example" hx-swap="morph" hx-target="#content">
    Update Content
  </button>
</body>
```

### Core Extensions

- head-support
- htmx-1-compat
- idiomorph
- preload
- response-targets
- sse
- ws

## Creating Extensions

Refer to the extension documentation for custom extensions.

## Events & Logging

Listen to htmx events:

```javascript
htmx.on("htmx:load", function(evt) {
    myJavascriptLib.init(evt.detail.elt);
});
```

### Initialize A 3rd Party Library With Events

```javascript
htmx.onLoad(function(target) {
    myJavascriptLib.init(target);
});
```

### Configure a Request With Events

```javascript
document.body.addEventListener('htmx:configRequest', function(evt) {
    evt.detail.parameters['auth_token'] = getAuthToken();
    evt.detail.headers['Authentication-Token'] = getAuthToken();
});
```

### Modifying Swapping Behavior With Events

```javascript
document.body.addEventListener('htmx:beforeSwap', function(evt) {
    if(evt.detail.xhr.status === 404){
        alert("Error: Could Not Find Resource");
    } else if(evt.detail.xhr.status === 422){
        evt.detail.shouldSwap = true;
        evt.detail.isError = false;
    } else if(evt.detail.xhr.status === 418){
        evt.detail.shouldSwap = true;
        evt.detail.target = htmx.find("#teapot");
    }
});
```

## Event Naming

Events use both camelCase and kebab-case, e.g., `htmx:afterSwap` and `htmx:after-swap`.

## Logging

Set a logger to log events:

```javascript
htmx.logger = function(elt, event, data) {
    if(console) {
        console.log(event, elt, data);
    }
}
```

## Debugging

Enable detailed logging:

```javascript
htmx.logAll();
```

Monitor events in the console:

```javascript
monitorEvents(htmx.find("#theElement"));
```

## Creating Demos

Include demo script for mocks:

```html
<script src="https://demo.htmx.org"></script>
```

### Demo Example

```html
<!-- load demo environment -->
<script src="https://demo.htmx.org"></script>

<!-- post to /foo -->
<button hx-post="/foo" hx-target="#result">
    Count Up
</button>
<output id="result"></output>

<!-- respond to /foo with some dynamic content in a template tag -->
<script>
    globalInt = 0;
</script>
<template url="/foo" delay="500">
    ${globalInt++}
</template>
```

## Scripting

Use events for scripting with htmx.

### Scripting Solutions

- VanillaJS
- AlpineJS
- jQuery
- hyperscript

### The hx-on* Attributes

Respond to any event:

```html
<button hx-on:click="alert('You clicked me!')">
    Click Me!
</button>
```

Custom event handling:

```html
<button hx-post="/example"
        hx-on:htmx:config-request="event.detail.parameters.example = 'Hello Scripting!'">
    Post Me!
</button>
```

## 3rd Party Javascript

Initialize libraries on htmx load:

```javascript
htmx.onLoad(function(content) {
    var sortables = content.querySelectorAll(".sortable");
    sortables.forEach(sortable => new Sortable(sortable, {
        animation: 150,
        ghostClass: 'blue-background-class'
    }));
});
```

Process dynamically added htmx content:

```javascript
let myDiv = document.getElementById('my-div')
fetch('http://example.com/movies.json')
    .then(response => response.text())
    .then(data => { myDiv.innerHTML = data; htmx.process(myDiv); } );
```

## Web Components

Refer to Web Components Examples for integration.

## Caching

htmx works with HTTP caching. Use `Vary: HX-Request` if responses vary based on `HX-Request` header.

Enable cache buster:

```javascript
htmx.config.getCacheBusterParam = true;
```

## Security

### Rule 1: Escape All User Content

Always escape untrusted content to prevent XSS.

### htmx Security Tools

#### hx-disable

Prevent htmx from processing attributes:

```html
<div hx-disable>
    <%= raw(user_content) %>
</div>
```

#### hx-history

Exclude from history cache:

```html
<div hx-history="false">
    ...
</div>
```

## Configuration Options

Set configurations via JavaScript or meta tag:

```html
<meta name="htmx-config" content='{"defaultSwapStyle":"outerHTML"}'>
```

Key options include:
- `historyEnabled`
- `historyCacheSize`
- `refreshOnHistoryMiss`
- `defaultSwapStyle`
- `defaultSwapDelay`
- `defaultSettleDelay`
- `includeIndicatorStyles`
- `indicatorClass`
- `requestClass`
- `addedClass`
- `settlingClass`
- `swappingClass`
- `allowEval`
- `allowScriptTags`
- `inlineScriptNonce`
- `attributesToSettle`
- `inlineStyleNonce`
- `useTemplateFragments`
- `wsReconnectDelay`
- `wsBinaryType`
- `disableSelector`
- `withCredentials`
- `timeout`
- `scrollBehavior`
- `defaultFocusScroll`
- `getCacheBusterParam`
- `globalViewTransitions`
- `methodsThatUseUrlParams`
- `selfRequestsOnly`
- `ignoreTitle`
- `disableInheritance`
- `scrollIntoViewOnBoost`
- `triggerSpecsCache`
- `responseHandling`
- `allowNestedOobSwaps`
