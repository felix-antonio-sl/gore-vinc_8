# daisyUI Documentation

## Using daisyUI

### Adding Components to HTML

Use daisyUI components via:

|Method|Description|Example|
|-|-|-|
|Tailwind CSS Classes|Utilize Tailwind utility classes directly.|```html<br><button class="bg-gray-800 text-white px-4 py-3 rounded-md hover:bg-gray-900">Button</button>```|
|daisyUI Component Class|Use predefined daisyUI classes.|```html<br><button class="btn">Button</button>```|
|Modify with daisyUI Utilities|Combine daisyUI classes for customization.|```html<br><button class="btn btn-primary">Button</button>```|
|Customize with Tailwind|Add Tailwind classes for further styling.|```html<br><button class="btn w-64 rounded-full">Button</button>```|

### Using daisyUI from CDN

Include daisyUI via CDN without installation:

```html
<head>
 <link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet" />
 <script src="https://cdn.tailwindcss.com"></script>
</head>
```

## Customizing Components

### Methods of Customization

|Method|Description|Example|
|-|-|-|
|daisyUI Utility Classes|Modify with built-in classes.|```html<br><button class="btn btn-primary">Primary</button>```|
|Tailwind CSS Classes|Enhance with Tailwind utilities.|```html<br><button class="btn rounded-full">Rounded</button>```|
|Custom CSS|Use `@apply` in CSS files.|```css<br>.btn-custom { @apply bg-blue-500 text-white rounded-lg; }```|
|Additional Options|Create custom themes or use unstyled components for full control.|N/A|

## Configuration

### Default Settings

Configure in `tailwind.config.js`:

```js
module.exports = {
 plugins: [require("daisyui")],
 daisyui: {
  themes: false,
  darkTheme: "dark",
  base: true,
  styled: true,
  utils: true,
  prefix: "",
  logs: true,
  themeRoot: ":root",
 },
}
```

### Configuration Options Explained

|Option|Type|Default|Description|
|-|-|-|-|
|`styled`|Boolean|`true`|`true`: Includes default styles.<br>`false`: Unstyled components.|
|`themes`|Boolean \|Array|`false`|`true`: All themes.<br>`false`: Light & dark.<br>Array: Specific themes.|
|`base`|Boolean|`true`|Applies base styles.|
|`utils`|Boolean|`true`|Adds utility classes.|
|`logs`|Boolean|`true`|Logs config info during build.|
|`darkTheme`|String|`"dark"`|Default dark theme.|
|`prefix`|String|`""`|Prefix for daisyUI classes.|
|`themeRoot`|String|`":root"`|Element for theme CSS variables.|

*Note: Prefix applies to component and modifier classes, not utility classes.*

## Colors

### Color Names and Usage

|Color Name|Description|Required for Themes|Example Class|
|-|-|-|-|
|`primary`|Primary color|Yes|`bg-primary`|
|`primary-content`|Foreground on primary|No|`text-primary-content`|
|`secondary`|Secondary color|Yes|`bg-secondary`|
|`secondary-content`|Foreground on secondary|No|`text-secondary-content`|
|`accent`|Accent color|Yes|`bg-accent`|
|`accent-content`|Foreground on accent|No|`text-accent-content`|
|`neutral`|Neutral color|Yes|`bg-neutral`|
|`neutral-content`|Foreground on neutral|No|`text-neutral-content`|
|`base-100`|Base background|Yes|`bg-base-100`|
|`base-200`|Slightly darker base|No|`bg-base-200`|
|`base-300`|Even darker base|No|`bg-base-300`|
|`base-content`|Foreground on base|No|`text-base-content`|
|`info`|Info color|No|`bg-info`|
|`info-content`|Foreground on info|No|`text-info-content`|
|`success`|Success color|No|`bg-success`|
|`success-content`|Foreground on success|No|`text-success-content`|
|`warning`|Warning color|No|`bg-warning`|
|`warning-content`|Foreground on warning|No|`text-warning-content`|
|`error`|Error color|No|`bg-error`|
|`error-content`|Foreground on error|No|`text-error-content`|

### How to Use

- With Components:

 ```html
 <button class="btn btn-primary">Primary</button>
 <input type="checkbox" class="checkbox checkbox-secondary" />
 ```

- With Utility Classes:

 ```html
 <div class="bg-primary text-primary-content border-accent">
  <!-- Content -->
 </div>
 ```

- Available Utility Classes:

 ```
 bg-{COLOR_NAME}, to-{COLOR_NAME}, via-{COLOR_NAME}, from-{COLOR_NAME},
 text-{COLOR_NAME}, ring-{COLOR_NAME}, fill-{COLOR_NAME},
 caret-{COLOR_NAME}, stroke-{COLOR_NAME}, border-{COLOR_NAME},
 divide-{COLOR_NAME}, accent-{COLOR_NAME}, shadow-{COLOR_NAME},
 outline-{COLOR_NAME}, decoration-{COLOR_NAME}, placeholder-{COLOR_NAME},
 ring-offset-{COLOR_NAME}
 ```

 *Opacity example: `bg-primary/50`*

## Themes

### Applying Themes

1. Include Themes in Configuration:

  ```js
  module.exports = {
   daisyui: {
    themes: ["light", "dark", "cupcake"],
   },
  }
  ```

2. Set Theme in HTML:

  ```html
  <html data-theme="cupcake">
   <!-- Content -->
  </html>
  ```

  *Tip: Use [theme-change](https://github.com/saadeghi/theme-change) for dynamic switching.*

### Available Themes

- `light`, `dark`, `cupcake`, `bumblebee`, `emerald`, `corporate`, `synthwave`, `retro`, `cyberpunk`, `valentine`, `halloween`, `garden`, `forest`, `aqua`, `lofi`, `pastel`, `fantasy`, `wireframe`, `black`, `luxury`, `dracula`, `cmyk`, `autumn`, `business`, `acid`, `lemonade`, `night`, `coffee`, `winter`, `dim`, `nord`, `sunset`

### Managing Themes

- Include Specific Themes:

 ```js
 module.exports = {
  daisyui: {
   themes: ["cupcake", "dark", "cmyk"],
  },
 }
 ```

- Disable All Themes:
 	- *Only Light & Dark:*

  ```js
  module.exports = {
   daisyui: {
    themes: false,
   },
  }
  ```

 	- *Skeleton Setup:*

  ```js
  module.exports = {
   daisyui: {
    themes: [],
   },
  }
  ```

- Apply Theme to Specific Section:

 ```html
 <html data-theme="dark">
  <div data-theme="light">
   This section uses the light theme.
   <span data-theme="retro">This span uses the retro theme!</span>
  </div>
 </html>
 ```

### Creating Custom Themes

#### Example Custom Theme

```js
module.exports = {
 daisyui: {
  themes: [
   {
    mytheme: {
     "primary": "#a991f7",
     "secondary": "#f6d860",
     "accent": "#37cdbe",
     "neutral": "#3d4451",
     "base-100": "#ffffff",
     "--rounded-box": "1rem",
     "--rounded-btn": "0.5rem",
     "--rounded-badge": "1.9rem",
     "--animation-btn": "0.25s",
     "--animation-input": "0.2s",
     "--btn-focus-scale": "0.95",
     "--border-btn": "1px",
     "--tab-border": "1px",
     "--tab-radius": "0.5rem",
    },
   },
   "dark",
   "cupcake",
  ],
 },
}
```

#### Customizing an Existing Theme

```js
module.exports = {
 daisyui: {
  themes: [
   {
    light: {
     ...require("daisyui/src/theming/themes")["light"],
     primary: "#1e40af",
     secondary: "#0284c7",
    },
   },
  ],
 },
}
```

#### Adding Custom Styles to a Theme

```js
module.exports = {
 daisyui: {
  themes: [
   {
    mytheme: {
     "--rounded-box": "1rem",
     ".btn-custom": {
      "background-color": "#1EA1F1",
      "border-color": "#1EA1F1",
     },
     ".btn-custom:hover": {
      "background-color": "#1C96E1",
      "border-color": "#1C96E1",
     },
    },
   },
  ],
 },
}
```

#### Using Tailwind's `dark:` Selector with Themes

```js
module.exports = {
 content: ['./src//*.{html,js}'],
 plugins: [require('daisyui')],
 daisyui: {
  themes: ['winter', 'night'],
 },
 darkMode: ['class', '[data-theme="night"]'],
}
```

## Utility Classes and CSS Variables

### Color Utility Classes

Use daisyUI colors with Tailwind utilities:

```html
<div class="bg-primary text-primary-content border-accent">
 <!-- Content -->
</div>
```

*Opacity example: `bg-primary/50`*

### Available Classes

```
bg-{COLOR_NAME}, to-{COLOR_NAME}, via-{COLOR_NAME}, from-{COLOR_NAME},
text-{COLOR_NAME}, ring-{COLOR_NAME}, fill-{COLOR_NAME},
caret-{COLOR_NAME}, stroke-{COLOR_NAME}, border-{COLOR_NAME},
divide-{COLOR_NAME}, accent-{COLOR_NAME}, shadow-{COLOR_NAME},
outline-{COLOR_NAME}, decoration-{COLOR_NAME}, placeholder-{COLOR_NAME},
ring-offset-{COLOR_NAME}
```

### Border Radius Classes

|Class Name|Description|
|-|-|
|`rounded-box`|Large components (cards, modals)|
|`rounded-btn`|Medium components (buttons, inputs)|
|`rounded-badge`|Small components (badges)|

```html
<div class="rounded-box bg-base-200 p-4">Large Element</div>
<button class="btn rounded-btn">Button</button>
<span class="badge rounded-badge">Badge</span>
```

### Glass Effect

Add a matte glass effect:

```html
<div class="glass p-4">
 Glass Effect Element
</div>
```

### CSS Variables

#### In Your Theme

```js
module.exports = {
 daisyui: {
  themes: [
   {
    mytheme: {
     "--rounded-box": "1rem",
     "--rounded-btn": "0.5rem",
     "--rounded-badge": "1.9rem",
     "--animation-btn": "0.25s",
     "--animation-input": "0.2s",
     "--btn-focus-scale": "0.95",
     "--border-btn": "1px",
     "--tab-border": "1px",
     "--tab-radius": "0.5rem",
    },
   },
  ],
 },
}
```

#### Directly in HTML

```html
<div class="[--animation-btn:0.3s]">
 <!-- Content with custom animation speed -->
</div>
```

#### Component-Specific CSS Variables

|Component|CSS Variables|
|-|-|
|Tab|`--tab-border`, `--tab-border-color`, `--tab-padding`, `--tab-bg`, `--tab-radius`, `--tab-corner-bg`, `--circle-pos`, `--tab-grad`|
|Countdown|`--value`|
|Radial Progress|`--value`, `--size`, `--thickness`|
|Tooltip|`--tooltip-color`, `--tooltip-text-color`, `--tooltip-offset`, `--tooltip-tail`, `--tooltip-tail-offset`|
|Checkbox|`--chkbg`, `--chkfg`|
|Toggle|`--tglbg`, `--handleoffset`|
|Range Slider|`--filler-size`, `--filler-offset`, `--range-shdw`|
|Glass Effect|`--glass-blur`, `--glass-opacity`, `--glass-border-opacity`, `--glass-reflex-degree`, `--glass-reflex-opacity`, `--glass-text-shadow-opacity`|

## Layout and Typography

### Layout

Handled by Tailwind CSS utility classes for:

- Sizing
- Grids
- Spacing
- Flexbox

### Typography

Use [Tailwind CSS Typography](https://github.com/tailwindlabs/tailwindcss-typography) with daisyUI:

#### Setup

```js
module.exports = {
 plugins: [require("@tailwindcss/typography"), require("daisyui")],
}
```

#### Usage

```html
<article class="prose">
 <h1>Main Heading</h1>
 <p>Paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
 <ul>
  <li>List item one</li>
  <li>List item two</li>
 </ul>
 <pre><code>console.log('Hello, world!');</code></pre>
</article>
```

#### Features

- Headings: Styled `h1` to `h4`
- Paragraphs: Consistent text styling
- Lists: Styled unordered and ordered
- Code Blocks: Formatted snippets
- Tables: Improved readability
- Images: Styled within content

## Components

### UI Components Summary

|#|Component|Purpose|Base Class|Modifiers|Variants|Usage Notes|
|-|-|-|-|-|-|-|
|1|Button|User actions/selections|`btn`|Colors: `btn-primary`, `btn-secondary`, etc.<br>Styles: `btn-ghost`, `btn-link`, `btn-outline`, `glass`<br>States: `btn-active`, `btn-disabled`<br>Sizes: `btn-lg`, `btn-sm`, `btn-xs`, `btn-wide`, `btn-block`, `btn-circle`, `btn-square`|Various styles and responsive sizes|Apply to `<button>`, `<input>`, `<a>`. Supports multiple styles and sizes.|
|2|Dropdown|Displays a menu on interaction|`dropdown`|Alignment: `dropdown-end`, `dropdown-top`, etc.<br>Behavior: `dropdown-hover`, `dropdown-open`|Positions and trigger methods|Accessible methods using `<details>`, `<summary>`, or JavaScript controls.|
|3|Modal|Dialogs or overlays for interactions|`modal`|Visibility: `modal-open`<br>Positioning: `modal-top`, `modal-middle`, `modal-bottom`|Custom widths, overlays|Methods: `<dialog>`, hidden checkbox, anchor links. Supports multiple closing methods.|
|4|Swap|Toggles visibility between two elements|`swap`|`swap-active`, `swap-rotate`, `swap-flip`|Icon toggles, switches with effects|Activate via checkbox or JS by adding `swap-active` class.|
|5|Theme Controller|Switches website theme|`theme-controller`|CSS-based theming with JS for state persistence|Toggles, checkboxes, swaps, dropdowns, radios|Utilize localStorage or server-side storage for theme state.|
|6|Accordion|Manages expandable sections|`collapse`|`collapse-arrow`, `collapse-plus`, `collapse-open`, `collapse-close`|Integrated with radio inputs, styled with icons|Allows only one section open at a time. Can combine with `join` for cohesive styling.|
|7|Avatar|Displays user/business thumbnails|`avatar`|`online`, `offline`, `placeholder`|Custom sizes, rounded shapes, masks|Supports grouping, placeholders with initials, status indicators.|
|8|Badge|Highlights status indicators/notifications|`badge`|Colors: `badge-primary`, `badge-secondary`, etc.<br>Sizes: `badge-lg`, `badge-sm`, `badge-xs`|Integrated within buttons/links or standalone|Use for notifications and status displays.|
|9|Card|Organizes content in a structured layout|`card`|Styles: `card-bordered`, `image-full`, `card-compact`, `card-side`, `card-normal`<br>Effects: `glass`|Custom colors, image overlays, responsive padding|Components: `card-title`, `card-body`, `card-actions`.|
|10|Carousel|Showcases images/content in scrollable format|`carousel`|`carousel-start`, `carousel-center`, `carousel-end`, `carousel-vertical`|Snap alignment, navigation buttons, vertical|Use `carousel-item` for each slide. Supports full or half-width items.|
|11|Chat Bubble|Displays conversational messages|`chat`|Alignment: `chat-start`, `chat-end`<br>Colors: `chat-bubble-primary`, etc.|Includes images, headers, footers|Supports metadata like timestamps/statuses.|
|12|Collapse|Toggles visibility of content sections|`collapse`|`collapse-arrow`, `collapse-plus`, `collapse-open`, `collapse-close`|Colored lines, icons, custom styles|Methods: Focus-based, checkbox-controlled, `<details>` usage.|
|13|Countdown|Displays a countdown timer|`countdown`|Controlled via `--value` CSS variable|Large text, clock formats|Requires JS to update `--value` dynamically.|
|14|Diff|Compares two items side-by-side|`diff`|Resizable panes|Side-by-side analysis|Use `diff-item-1`, `diff-item-2`, `diff-resizer` for detailed comparison.|
|15|Kbd|Displays keyboard shortcuts/keys|`kbd`|Sizes: `kbd-lg`, `kbd-sm`, `kbd-xs`|Single keys, key combinations, inline|Use within text or for full keyboard layouts.|
|16|Stat|Presents numerical data and info|`stats`|`stats-horizontal`, `stats-vertical`|Icons/images within stats, responsive layouts|Components: `stat`, `stat-title`, `stat-value`, `stat-desc`, `stat-figure`, `stat-actions`.|
|17|Table|Displays structured data|`table`|`table-zebra`, `table-pin-rows`, `table-pin-cols`, `table-xs`, `table-sm`, `table-lg`|Zebra striping, sticky headers/columns|Enhances readability and interaction with large datasets.|
|18|Timeline|Lists events/milestones chronologically|`timeline`|`timeline-compact`, `timeline-snap-icon`, `timeline-vertical`, `timeline-horizontal`, `timeline-box`|Text on both/single side, colorful lines|Connects events with lines, supports detailed descriptions.|
|19|Breadcrumbs|Displays user's location in site hierarchy|`breadcrumbs`|With icons, max-width with scroll capability|Icon-enhanced, scrollable|Ideal for deep navigation structures.|
|20|Bottom Navigation|Provides navigation from bottom interface|`btm-nav`|`active`, `disabled`<br>Sizes: `btm-nav-xs`, `btm-nav-sm`, `btm-nav-lg`|Brand colors, responsive sizes|Requires `<meta name="viewport" content="viewport-fit=cover">` for iOS.|
|21|Link|Styles hyperlinks consistently|`link`|Colors: `link-primary`, `link-secondary`, etc.<br>Modifiers: `link-hover`|Underline always/on hover, multiple colors|Restores default link styling overridden by Tailwind CSS. Ensures accessibility.|
|22|Menu|Displays navigational links|`menu`|`disabled`, `active`, `menu-dropdown-show`, `menu-xs`, `menu-lg`, `menu-vertical`, `menu-horizontal`|Icon-only, badges, submenus, responsive layouts|Supports nested submenus, interactive elements with badges.|
|23|Navbar|Top navigation bar|`navbar`|Content: Titles, icons, menus<br>Layouts: Responsive designs|Start, center, end sections|Integrates with `drawer` for mobile, supports logo placement and interactive elements.|
|24|Pagination|Navigates through paginated content|`join`|Active states, sizes: Extra small to large<br>Controls: Next/Previous, indicators|Grouped buttons with `join-item`|Facilitates easy navigation across multiple content pages.|
|25|Steps|Illustrates a sequence of steps|`steps`|Colors: `step-primary`, etc.<br>Layouts: Horizontal (default), Vertical|Scrollable steps, custom content via `data-content`|Ideal for multi-step forms, progress indicators.|
|26|Tabs|Organizes content into tabbed sections|`tabs`|Styles: `tabs-boxed`, `tabs-bordered`, etc.<br>Sizes: `tabs-xs`, `tabs-lg`|Boxed, bordered, lifted styles, various sizes|Enhances content organization for seamless view switching.|
|27|Alert|Notifies users about important info/events|`alert`|Colors: `alert-info`, `alert-success`, etc.<br>Content: Messages, buttons, titles|Simple messages, actionable buttons|Positioned to draw attention without disrupting user experience. Can include buttons.|
|28|Loading|Indicates ongoing processes/data fetching|`loading`|Animations: `loading-spinner`, `loading-dots`, etc.<br>Colors: Customizable|Various animations|Enhances user feedback during asynchronous operations.|
|29|Progress|Visualizes task/process completion|`progress`|Colors: `progress-primary`, etc.<br>Types: Linear, indeterminate|Themed colors, various statuses|Useful for file uploads, installations, or any process requiring progress indication.|
|30|Radial Progress|Circular indicators for progress|`radial-progress`|Controlled via `--value` (0-100), customizable `--size`, `--thickness`|Various colors|Ideal for dashboards, fitness trackers, circular progress representation.|
|31|Skeleton|Placeholder during content loading|`skeleton`|Shapes: Circle, rectangle<br>With/without content|Overlay content, standalone|Enhances perceived performance by indicating loading states without abrupt shifts.|
|32|Toast|Temporary notifications on screen corners|`toast`|Positions: `toast-start`, `toast-center`, `toast-end`, `toast-top`, `toast-bottom`|Simple messages, alerts within toasts|Non-intrusive notifications informing users without requiring interaction.|
|33|Tooltip|Additional info on hover/focus|`tooltip`|Positions: `tooltip-top`, `tooltip-right`, etc.<br>Colors: `tooltip-primary`, etc.|Various positions, themed colors|Offers contextual information without cluttering the interface.|
|34|Checkbox|Selection/deselection of options|`checkbox`|Colors: `checkbox-primary`, etc.<br>Sizes: `checkbox-lg`, `checkbox-xs`|Disabled, indeterminate states|Integrates within forms, lists, or standalone interactive elements.|
|35|File Input|Facilitates file uploads|`file-input`|Styles: `file-input-bordered`, `file-input-ghost`<br>Sizes: `file-input-lg`, `file-input-xs`|Bordered, ghost styles|Enhances default file input appearance for consistent styling across browsers.|
|36|Radio|Select single option from a group|`radio`|Colors: `radio-primary`, etc.<br>Sizes: `radio-lg`, `radio-xs`|Disabled state|Ensures mutually exclusive selections within forms or interactive lists.|
|37|Range Slider|Select value within a range by sliding handle|`range`|Colors: `range-primary`, etc.<br>Sizes: `range-lg`, `range-xs`|Steps, precise value selection|Ideal for settings like volume, brightness, or range-based inputs.|
|38|Rating|Allows users to rate items with icons|`rating`|Features: `rating-half`, `rating-hidden`<br>Sizes: `rating-lg`, `rating-xs`|Half-stars, hidden inputs|Commonly used in reviews and surveys for user feedback.|
|39|Select|Dropdown list for selecting options|`select`|Styles: `select-bordered`, `select-ghost`<br>Sizes: `select-lg`, `select-xs`|Disabled state|Enhances standard `<select>` elements with consistent styling and interactive features.|
|40|Text Input|Single-line user text entry|`input`|Styles: `input-bordered`, `input-ghost`<br>Sizes: `input-lg`, `input-xs`|Icons inside, labels inside/outside|Versatile for forms, search bars, and text inputs.|
|41|Textarea|Multi-line text input|`textarea`|Styles: `textarea-bordered`, `textarea-ghost`<br>Sizes: `textarea-lg`, `textarea-xs`|Disabled state|Suitable for comments, descriptions, and multi-line inputs.|
|42|Toggle|Binary choice with switch-like interface|`toggle`|Colors: `toggle-primary`, etc.<br>Sizes: `toggle-lg`, `toggle-xs`|Disabled, indeterminate states|Enhances checkboxes with a modern switch appearance for binary settings.|
|43|Artboard|Simulates mobile device screens|`artboard`|Styles: `artboard-demo`, `phone-1` to `phone-6`, `artboard-horizontal`|Predefined phone dimensions, landscape orientation|Ideal for demonstrating mobile-responsive designs in documentation/presentations.|
|44|Divider|Visually separates content sections|`divider`|Orientations: `divider-vertical`, `divider-horizontal`<br>Colors: `divider-primary`, etc.<br>Positions: `divider-start`, `divider-end`|Vertical/Horizontal, themed colors|Enhances content organization by clearly delineating sections.|
|45|Drawer|Sidebar that slides in/out from page sides|`drawer`|Positions: `drawer-end`<br>Visibility: `drawer-open`|Responsive behavior, toggle via checkbox/overlay|Ideal for navigation menus, settings panels, or supplementary content.|
|46|Footer|Bottom section with links, logos, info|`footer`|Layouts: `footer-center`<br>Content: Links, logos, social icons|Multiple columns/rows, forms|Serves as a comprehensive site summary with navigational and informational links.|
|47|Hero|Prominent banner with key messages/visuals|`hero`|Layouts: Centered content, images on sides<br>Features: Forms, background overlays|Various layouts|Effective for landing pages, promotional sections, or introductory content.|
|48|Indicator|Decorative/informational elements on corners|`indicator`|Positions: `indicator-top`, `indicator-bottom`, etc.<br>Multiple indicators|Various alignments, stacking indicators|Enhances UI elements with notifications, status badges, or decorative accents.|
|49|Join|Groups elements with shared borders/styles|`join`|Layouts: `join-vertical`, `join-horizontal`|Grouped elements with `join-item`|Ideal for button groups, segmented controls, or clustered interactive elements.|
|50|Mask|Crops content into predefined shapes|`mask`|Shapes: `mask-circle`, `mask-hexagon`, etc.<br>Half Masks: `mask-half-1`, `mask-half-2`|Various geometric and organic shapes|Enhances visual aesthetics by applying creative shapes to images/icons.|
|51|Stack|Overlays multiple elements for layered effects|`stack`|Layering child elements<br>Variants: Stacked images, shadowed cards|Layered compositions|Useful for complex visual compositions, overlapping elements, or depth effects.|
|52|Browser Mockup|Simulates a browser window|`mockup-browser`|Styles: Borders, background colors|Realistic frames|Ideal for showcasing websites/apps within documentation or presentations.|
|53|Code Mockup|Displays code snippets in editor-like interface|`mockup-code`|Features: Line prefixes, multi-line support, highlighted lines|Enhanced readability of code samples|Makes tutorials and documentation more engaging with formatted code presentations.|
|54|Phone Mockup|Mimics smartphone screens|`mockup-phone`|Styles: With/without background colors|Various visual contexts|Perfect for demonstrating mobile-specific features or responsive designs in media.|
|55|Window Mockup|Emulates OS windows for desktop interfaces|`mockup-window`|Styles: Borders, background colors|Authentic windowed environments|Suitable for presenting desktop applications or software interfaces within windowed frames.|
