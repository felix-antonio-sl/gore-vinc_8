# Flask 3.1.x

## Installation

### Python Version

Use the latest Python version. Flask supports Python 3.9 and newer.

### Dependencies

Automatically installed with Flask:

- Werkzeug: Implements WSGI.
- Jinja: Template engine.
- MarkupSafe: Escapes inputs in templates.
- ItsDangerous: Securely signs data.
- Click: Command line framework.
- Blinker: Supports Signals.

### Optional Dependencies

Not installed automatically. Flask uses them if available:

- python-dotenv: Supports environment variables.
- Watchdog: Efficient reloader for development.

### greenlet

For using gevent or eventlet:

```py
greenlet>=1.0
```

Use the latest versions.

### Virtual Environments

Manage project dependencies with virtual environments.

#### Create an environment

```bash
# macOS/Linux
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv
```

#### Activate the environment

```bash
# macOS/Linux
$ . .venv/bin/activate
```

#### Install Flask

```bash
pip install Flask
```

## Quickstart

### A Minimal Application

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
 return "<p>Hello, World!</p>"
```

Save as `hello.py`.

#### Run the application

```bash
$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### Application Discovery Behavior

If named `app.py` or `wsgi.py`, omit `--app`.

### Externally Visible Server

Make server public:

```bash
flask run --host=0.0.0.0
```

### Debug Mode

Enable debug mode:

```bash
$ flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

Warning: Do not use in production.

## HTML Escaping

```py
from markupsafe import escape

@app.route("/<name>")
def hello(name):
 return f"Hello, {escape(name)}!"
```

## Routing

Bind functions to URLs:

```py
@app.route('/')
def index():
 return 'Index Page'

@app.route('/hello')
def hello():
 return 'Hello, World'
```

### Variable Rules

Use variables in URLs:

```py
from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
 return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
 return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
 return f'Subpath {escape(subpath)}'
```

#### Converters

- `string` (default)
- `int`
- `float`
- `path`
- `uuid`

## Unique URLs / Redirection Behavior

```py
@app.route('/projects/')
def projects():
 return 'The project page'

@app.route('/about')
def about():
 return 'The about page'
```

## URL Building

Use `url_for()`:

```py
from flask import url_for

@app.route('/')
def index():
 return 'index'

@app.route('/login')
def login():
 return 'login'

@app.route('/user/<username>')
def profile(username):
 return f'{username}\'s profile'

with app.test_request_context():
 print(url_for('index'))
 print(url_for('login'))
 print(url_for('login', next='/'))
 print(url_for('profile', username='John Doe'))
```

## HTTP Methods

Handle different methods:

```py
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
 if request.method == 'POST':
  return do_the_login()
 else:
  return show_the_login_form()
```

Or separate functions:

```py
@app.get('/login')
def login_get():
 return show_the_login_form()

@app.post('/login')
def login_post():
 return do_the_login()
```

## Static Files

Serve static files from `static` folder.

Generate URLs:

```py
url_for('static', filename='style.css')
```

## Rendering Templates

Render templates with Jinja2:

```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
 return render_template('hello.html', person=name)
```

### Template Example (`hello.html`)

```html
<!doctype html>
<title>Hello from Flask</title>
{% if person %}
  <h1>Hello {{ person }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

## Accessing Request Data

### The Request Object

```py
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
 error = None
 if request.method == 'POST':
  if valid_login(request.form['username'], request.form['password']):
   return log_the_user_in(request.form['username'])
  else:
   error = 'Invalid username/password'
 return render_template('login.html', error=error)
```

## File Uploads

Handle file uploads:

```py
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
 if request.method == 'POST':
  f = request.files['the_file']
  f.save('/var/www/uploads/uploaded_file.txt')
 ...
```

Use secure filenames:

```py
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
 if request.method == 'POST':
  file = request.files['the_file']
  file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
 ...
```

## Cookies

### Reading Cookies

```py
from flask import request

@app.route('/')
def index():
 username = request.cookies.get('username')
```

### Storing Cookies

```py
from flask import make_response

@app.route('/')
def index():
 resp = make_response(render_template(...))
 resp.set_cookie('username', 'the username')
 return resp
```

## Redirects and Errors

### Redirect

```py
from flask import redirect, url_for

@app.route('/')
def index():
 return redirect(url_for('login'))
```

### Abort

```py
from flask import abort

@app.route('/login')
def login():
 abort(401)
```

### Custom Error Page

```py
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
 return render_template('page_not_found.html'), 404
```

## About Responses

View return values are converted to responses:

```py
from flask import render_template, make_response

@app.errorhandler(404)
def not_found(error):
 resp = make_response(render_template('error.html'), 404)
 resp.headers['X-Something'] = 'A value'
 return resp
```

## APIs with JSON

Return JSON responses:

```py
@app.route("/me")
def me_api():
 user = get_current_user()
 return {
  "username": user.username,
  "theme": user.theme,
  "image": url_for("user_image", filename=user.image),
 }

@app.route("/users")
def users_api():
 users = get_all_users()
 return [user.to_json() for user in users]
```

## Sessions

Use sessions to store user data:

```py
from flask import session

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
 if 'username' in session:
  return f'Logged in as {session["username"]}'
 return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
 if request.method == 'POST':
  session['username'] = request.form['username']
  return redirect(url_for('index'))
 return '''
  <form method="post">
   <p><input type=text name=username>
   <p><input type=submit value=Login>
  </form>
 '''

@app.route('/logout')
def logout():
 session.pop('username', None)
 return redirect(url_for('index'))
```

Generate a secret key:

```bash
python -c 'import secrets; print(secrets.token_hex())'
```

## Message Flashing

Flash messages for user feedback:

```py
# Example usage not provided in original documentation
```

## Logging

Use Flask's logger:

```py
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```

## Hooking in WSGI Middleware

Add middleware by wrapping `wsgi_app`:

```py
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
```

## Templates

Flask uses Jinja2 as its default template engine, which must be installed to run Flask.

### Jinja Setup

By default, Flask configures Jinja2 with:

- Autoescaping enabled for `.html`, `.htm`, `.xml`, `.xhtml`, `.svg` templates via `render_template()` and all strings via `render_template_string()`.
- Templates can opt in/out autoescaping with `{% autoescape %}`.
- Flask adds global functions and helpers to the Jinja2 context.

### Standard Context

Default global variables in Jinja2 templates:

- `config`: Flask configuration.
- `request`: Current request (available with active request context).
- `session`: Current session (available with active request context).
- `g`: Global variables (available with active request context).
- `url_for()`: Flask's `url_for` function.
- `get_flashed_messages()`: Flask's `get_flashed_messages` function.

### The Jinja Context Behavior

Variables are added to the context, not globally. Imported templates don't see them by default.

To access `request` in an imported macro:

1. Pass `request` explicitly.
2. Import with context:

```jinja
{% from '_helpers.html' import my_macro with context %}
```

### Controlling Autoescaping

Autoescaping replaces special HTML characters to prevent XSS.

To disable autoescaping:

1. Wrap HTML string in `Markup` in Python.
2. Use `|safe` filter in template: `{{ myvariable|safe }}`
3. Use `{% autoescape false %}` block:

```jinja
{% autoescape false %}
 <p>autoescaping is disabled here
 <p>{{ will_not_be_escaped }}
{% endautoescape %}
```

### Registering Filters

Register custom Jinja2 filters via decorator or `jinja_env.filters`:

```py
@app.template_filter('reverse')
def reverse_filter(s):
 return s[::-1]

def reverse_filter(s):
 return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter
```

Use in templates:

```jinja
{% for x in mylist| reverse %}
{% endfor %}
```

### Context Processors

Inject variables/functions into template context:

```py
@app.context_processor
def inject_user():
 return dict(user=g.user)
```

```py
@app.context_processor
def utility_processor():
 def format_price(amount, currency="€"):
  return f"{amount:.2f}{currency}"
 return dict(format_price=format_price)
```

Use in templates:

```jinja
{{ format_price(0.33) }}
```

### Streaming

Render templates as streams with `stream_template()`:

```py
from flask import stream_template

@app.get("/timeline")
def timeline():
 return stream_template("timeline.html")
```

## Testing Flask Applications

Use `pytest` for testing.

```bash
pip install pytest
```

### Identifying Tests

- Located in `tests` folder.
- Functions start with `test_` in modules starting with `test_`.
- Grouped in classes starting with `Test`.

### Fixtures

Reusable setup with `pytest` fixtures in `tests/conftest.py`:

```py
import pytest
from my_project import create_app

@pytest.fixture()
def app():
 app = create_app()
 app.config.update({
  "TESTING": True,
 })
 yield app

@pytest.fixture()
def client(app):
 return app.test_client()

@pytest.fixture()
def runner(app):
 return app.test_cli_runner()
```

### Sending Requests with the Test Client

Use `client` to make requests.

#### Form Data

```py
from pathlib import Path

resources = Path(__file__).parent / "resources"

def test_edit_user(client):
 response = client.post("/user/2/edit", data={
  "name": "Flask",
  "theme": "dark",
  "picture": (resources / "picture.png").open("rb"),
 })
 assert response.status_code == 200
```

#### JSON Data

```py
def test_json_data(client):
 response = client.post("/graphql", json={
  "query": """
   query User($id: String!) {
    user(id: $id) {
     name
     theme
     picture_url
    }
   }
  """,
  "variables": {"id": 2},
 })
 assert response.json["data"]["user"]["name"] == "Flask"
```

#### Following Redirects

```py
def test_logout_redirect(client):
 response = client.get("/logout", follow_redirects=True)
 assert len(response.history) == 1
 assert response.request.path == "/index"
```

### Accessing and Modifying the Session

```py
from flask import session

def test_access_session(client):
 with client:
  client.post("/auth/login", data={"username": "flask"})
  assert session["user_id"] == 1
```

```py
from flask import session

def test_modify_session(client):
 with client.session_transaction() as session:
  session["user_id"] = 1

 response = client.get("/users/me")
 assert response.json["username"] == "flask"
```

### Running Commands with the CLI Runner

Use `runner` to invoke CLI commands:

```py
import click

@app.cli.command("hello")
@click.option("--name", default="World")
def hello_command(name):
 click.echo(f"Hello, {name}!")

def test_hello_command(runner):
 result = runner.invoke(args="hello")
 assert "World" in result.output

 result = runner.invoke(args=["hello", "--name", "Flask"])
 assert "Flask" in result.output
```

### Tests that depend on an Active Context

Use `app.app_context()` or `app.test_request_context()`:

```py
def test_db_post_model(app):
 with app.app_context():
  post = db.session.query(Post).get(1)
```

```py
def test_validate_user_edit(app):
 with app.test_request_context(
  "/user/2/edit", method="POST", data={"name": ""}
 ):
  messages = validate_edit_user()

 assert messages["name"][0] == "Name cannot be empty."
```

```py
def test_auth_token(app):
 with app.test_request_context("/user/2/edit", headers={"X-Auth-Token": "1"}):
  app.preprocess_request()
  assert g.user.name == "Flask"
```

## Handling Application Errors

### Error Logging Tools

Use Sentry for error logging:

```bash
pip install sentry-sdk[flask]
```

```py
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init('YOUR_DSN_HERE', integrations=[FlaskIntegration()])
```

### Error Handlers

Register handlers for HTTP errors.

#### Registering

Using decorator or `register_error_handler()`:

```py
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
 return 'bad request!', 400

# or

app.register_error_handler(400, handle_bad_request)
```

Custom exception:

```py
class InsufficientStorage(werkzeug.exceptions.HTTPException):
 code = 507
 description = 'Not enough storage space.'

app.register_error_handler(InsufficientStorage, handle_507)

raise InsufficientStorage()
```

#### Handling

Flask matches handlers by code or class hierarchy. Blueprint handlers override global ones except for routing errors.

#### Generic Exception Handlers

Handle `HTTPException` or `Exception`:

```py
from flask import json
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
 response = e.get_response()
 response.data = json.dumps({
  "code": e.code,
  "name": e.name,
  "description": e.description,
 })
 response.content_type = "application/json"
 return response
```

```py
from werkzeug.exceptions import HTTPException

@app.errorhandler(Exception)
def handle_exception(e):
 if isinstance(e, HTTPException):
  return e
 return render_template("500_generic.html", e=e), 500
```

#### Unhandled Exceptions

Return 500 error, with original exception accessible as `e.original_exception`.

### Custom Error Pages

Use `abort()` and register error handlers:

```py
from flask import abort, render_template, request

@app.route("/profile")
def user_profile():
 username = request.args.get("username")
 if username is None:
  abort(400)

 user = get_user(username=username)
 if user is None:
  abort(404)

 return render_template("profile.html", user=user)
```

```py
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
```

Using application factory:

```py
from flask import Flask, render_template

def page_not_found(e):
 return render_template('404.html'), 404

def create_app(config_filename):
 app = Flask(__name__)
 app.register_error_handler(404, page_not_found)
 return app
```

Example template:

```jinja
{% extends "layout.html" %}
{% block title %}Page Not Found{% endblock %}
{% block body %}
  <h1>Page Not Found</h1>
  <p>What you were looking for is just not there.
  <p><a href="{{ url_for('index') }}">go somewhere nice</a>
{% endblock %}
```

Custom 500 error page:

```jinja
{% extends "layout.html" %}
{% block title %}Internal Server Error{% endblock %}
{% block body %}
  <h1>Internal Server Error</h1>
  <p>Oops... we seem to have made a mistake, sorry!</p>
  <p><a href="{{ url_for('index') }}">Go somewhere nice instead</a>
{% endblock %}
```

Registering 500 handler:

```py
from flask import render_template

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500
```

Using application factory:

```py
from flask import Flask, render_template

def internal_server_error(e):
 return render_template('500.html'), 500

def create_app():
 app = Flask(__name__)
 app.register_error_handler(500, internal_server_error)
 return app
```

Using Blueprints:

```py
from flask import Blueprint

blog = Blueprint('blog', __name__)

@blog.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

# or

blog.register_error_handler(500, internal_server_error)
```

Blueprint error handlers for 404, 405:

Handled at application level:

```py
from flask import jsonify, render_template

@app.errorhandler(404)
def page_not_found(e):
 if request.path.startswith('/blog/'):
  return render_template("blog/404.html"), 404
 else:
  return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed(e):
 if request.path.startswith('/api/'):
  return jsonify(message="Method Not Allowed"), 405
 else:
  return render_template("405.html"), 405
```

### Returning API Errors as JSON

Use `jsonify()` in error handlers:

```py
from flask import abort, jsonify

@app.errorhandler(404)
def resource_not_found(e):
 return jsonify(error=str(e)), 404

@app.route("/cheese")
def get_one_cheese():
 resource = get_resource()
 if resource is None:
  abort(404, description="Resource not found")
 return jsonify(resource)
```

Custom exception for API:

```py
from flask import jsonify, request

class InvalidAPIUsage(Exception):
 status_code = 400

 def __init__(self, message, status_code=None, payload=None):
  super().__init__()
  self.message = message
  if status_code is not None:
   self.status_code = status_code
  self.payload = payload

 def to_dict(self):
  rv = dict(self.payload or ())
  rv['message'] = self.message
  return rv

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
 return jsonify(e.to_dict()), e.status_code

@app.route("/api/user")
def user_api(user_id):
 user_id = request.args.get("user_id")
 if not user_id:
  raise InvalidAPIUsage("No user id provided!")

 user = get_user(user_id=user_id)
 if not user:
  raise InvalidAPIUsage("No such user!", status_code=404)

 return jsonify(user.to_dict())
```

## Debugging Application Errors

### In Production

- Do not use development server or debugger.
- Use error logging tools like Sentry.
- Optionally, use external debuggers with precautions.

### The Built-In Debugger

Enable with debug mode:

```bash
flask --app hello run --debug
```

Or in code:

```py
app.run(debug=True)
```

Warning: Do not use in production.

### External Debuggers

Disable built-in debugger and reloader when using external debuggers:

```bash
flask --app hello run --debug --no-debugger --no-reload
```

Or in code:

```py
app.run(
 debug=True, passthrough_errors=True,
 use_debugger=False, use_reloader=False
)
```

## Logging

Flask uses Python’s standard logging via `app.logger` for application messages and your own logs.

```py
@app.route('/login', methods=['POST'])
def login():
 user = get_user(request.form['username'])

 if user.check_password(request.form['password']):
  login_user(user)
  app.logger.info('%s logged in successfully', user.username)
  return redirect(url_for('index'))
 else:
  app.logger.info('%s failed to log in', user.username)
  abort(401)
```

By default, the log level is `WARNING`. Logs below this level are not shown unless configured.

### Basic Configuration

Configure logging early, preferably before creating the Flask app, to avoid default handlers.

```py
from logging.config import dictConfig

dictConfig({
 'version': 1,
 'formatters': {'default': {
  'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
 }},
 'handlers': {'wsgi': {
  'class': 'logging.StreamHandler',
  'stream': 'ext://flask.logging.wsgi_errors_stream',
  'formatter': 'default'
 }},
 'root': {
  'level': 'INFO',
  'handlers': ['wsgi']
 }
})

app = Flask(__name__)
```

### Default Configuration

Without custom configuration, Flask adds a `StreamHandler` to `app.logger`, directing logs to `wsgi.errors` during requests and `sys.stderr` otherwise.

### Removing the Default Handler

If logging is configured after accessing `app.logger`, remove the default handler:

```py
from flask.logging import default_handler

app.logger.removeHandler(default_handler)
```

### Email Errors to Admins

Use `SMTPHandler` to email admins on errors and above.

```py
import logging
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
 mailhost='127.0.0.1',
 fromaddr='server-error@example.com',
 toaddrs=['admin@example.com'],
 subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
 '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

if not app.debug:
 app.logger.addHandler(mail_handler)
```

### Injecting Request Information

Subclass `logging.Formatter` to include request details.

```py
from flask import has_request_context, request
from flask.logging import default_handler

class RequestFormatter(logging.Formatter):
 def format(self, record):
  if has_request_context():
   record.url = request.url
   record.remote_addr = request.remote_addr
  else:
   record.url = None
   record.remote_addr = None
  return super().format(record)

formatter = RequestFormatter(
 '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
 '%(levelname)s in %(module)s: %(message)s'
)
default_handler.setFormatter(formatter)
mail_handler.setFormatter(formatter)
```

### Other Libraries

Add handlers to the root logger to capture logs from other libraries.

```py
from flask.logging import default_handler

root = logging.getLogger()
root.addHandler(default_handler)
root.addHandler(mail_handler)

for logger in (
 logging.getLogger(app.name),
 logging.getLogger('sqlalchemy'),
 logging.getLogger('other_package'),
):
 logger.addHandler(default_handler)
 logger.addHandler(mail_handler)
```

### Werkzeug

Werkzeug logs to the `werkzeug` logger. It adds a `StreamHandler` if the root logger has no handlers.

### Flask Extensions

Extensions may log to `app.logger` or their own loggers. Refer to each extension’s documentation.

## Configuration Handling

Flask configurations manage environment-specific settings like debug mode and secret keys.

### Configuration Basics

Access configurations via `app.config`, a dictionary-like object.

```py
app = Flask(__name__)
app.config['TESTING'] = True
app.testing = True
app.config.update(
 TESTING=True,
 SECRET_KEY='your_secret_key'
)
```

### Debug Mode

Set debug mode using the `--debug` flag when running Flask.

```bash
flask --app hello run --debug
```

Avoid setting `DEBUG` in code to ensure consistent behavior.

### Builtin Configuration Values

Key configurations include:

- `DEBUG`: Enables debug mode.
- `TESTING`: Enables testing mode.
- `SECRET_KEY`: Secures session cookies.
- `SESSION_COOKIE_*`: Manages session cookie properties.
- `MAX_CONTENT_LENGTH`: Limits request size.

Refer to the original documentation for all builtin values.

### Configuring from Python Files

Load configurations from Python modules.

```py
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
```

Set the environment variable before running:

```bash
export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
flask run
```

### Configuring from Data Files

Load configurations from formats like TOML or JSON.

```py
import tomllib
app.config.from_file("config.toml", load=tomllib.load, text=False)

import json
app.config.from_file("config.json", load=json.load)
```

### Configuring from Environment Variables

Load configurations prefixed with `FLASK_`.

```bash
export FLASK_SECRET_KEY="your_secret_key"
export FLASK_MAIL_ENABLED=false
flask run
```

Access in code:

```py
app.config.from_prefixed_env()
app.config["SECRET_KEY"]  # "your_secret_key"
```

### Configuration Best Practices

- Create the app in a factory function.
- Avoid configuration-dependent code at import time.
- Load configurations early for extensions.

### Development / Production

Use separate configurations for different environments.

```py
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
```

Example using classes:

```py
class Config:
 TESTING = False

class ProductionConfig(Config):
 DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
 DATABASE_URI = "sqlite:////tmp/foo.db"

app.config.from_object('configmodule.ProductionConfig')
```

### Instance Folders

Use instance folders for deployment-specific configurations.

```py
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('yourapplication.default_settings')
app.config.from_pyfile('application.cfg', silent=True)
```

Access instance path:

```py
filename = os.path.join(app.instance_path, 'application.cfg')
with open(filename) as f:
 config = f.read()

# Or using open_instance_resource:
with app.open_instance_resource('application.cfg') as f:
 config = f.read()
```

## Signals

Signals notify subscribers of events during the application lifecycle. Flask uses Blinker for signals.

### Core Signals

Flask provides built-in signals. Refer to Flask’s documentation for a list.

### Subscribing to Signals

Connect functions to signals using `connect()`.

```py
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
 recorded = []
 def record(sender, template, context, extra):
  recorded.append((template, context))
 template_rendered.connect(record, app)
 try:
  yield recorded
 finally:
  template_rendered.disconnect(record, app)
```

Use with a test client:

```py
with captured_templates(app) as templates:
 rv = app.test_client().get('/')
 assert rv.status_code == 200
 assert len(templates) == 1
 template, context = templates[0]
 assert template.name == 'index.html'
 assert len(context['items']) == 10
```

### Creating Signals

Create custom signals using Blinker’s `Namespace`.

```py
from blinker import Namespace
my_signals = Namespace()
model_saved = my_signals.signal('model-saved')
```

### Sending Signals

Emit signals with `send()`.

```py
class Model(object):
 ...

 def save(self):
  model_saved.send(self)
```

Use `current_app._get_current_object()` as the sender if needed.

### Decorator Based Signal Subscriptions

Subscribe using decorators.

```py
from flask import template_rendered

@template_rendered.connect_via(app)
def when_template_rendered(sender, template, context, extra):
 print(f'Template {template.name} is rendered with {context}')
```

## Class-based Views

### Basic Reusable View

A class-based view acts as a view function, allowing different instances with different arguments for reusable behavior.

Example of converting a view function to a view class:

```py
@app.route("/users/")
def user_list():
 users = User.query.all()
 return render_template("users.html", users=users)
```

To make it reusable:

```py
from flask.views import View

class UserList(View):
 def dispatch_request(self):
  users = User.query.all()
  return render_template("users.html", objects=users)

app.add_url_rule("/users/", view_func=UserList.as_view("user_list"))
```

#### Registering Multiple Models

```py
class ListView(View):
 def __init__(self, model, template):
  self.model = model
  self.template = template

 def dispatch_request(self):
  items = self.model.query.all()
  return render_template(self.template, items=items)

app.add_url_rule(
 "/users/",
 view_func=ListView.as_view("user_list", User, "users.html"),
)
app.add_url_rule(
 "/stories/",
 view_func=ListView.as_view("story_list", Story, "stories.html"),
)
```

### URL Variables

URL variables are passed as keyword arguments to `dispatch_request`.

```py
class DetailView(View):
 def __init__(self, model):
  self.model = model
  self.template = f"{model.__name__.lower()}/detail.html"

 def dispatch_request(self, id):
  item = self.model.query.get_or_404(id)
  return render_template(self.template, item=item)

app.add_url_rule(
 "/users/<int:id>",
 view_func=DetailView.as_view("user_detail", User)
)
```

### View Lifetime and `self`

By default, a new instance is created per request. To reuse a single instance, set `init_every_request` to `False`.

```py
class ListView(View):
 init_every_request = False

 def __init__(self, model, template):
  self.model = model
  self.template = template

 def dispatch_request(self):
  items = self.model.query.all()
  return render_template(self.template, items=items)
```

### View Decorators

Apply decorators to the view function returned by `as_view`.

```py
class UserList(View):
 decorators = [cache(minutes=2), login_required]

app.add_url_rule('/users/', view_func=UserList.as_view())
```

Equivalent manual decoration:

```py
view = UserList.as_view("users_list")
view = cache(minutes=2)(view)
view = login_required(view)
app.add_url_rule('/users/', view_func=view)
```

### Method Hints

Specify allowed HTTP methods with `methods`.

```py
class MyView(View):
 methods = ["GET", "POST"]

 def dispatch_request(self):
  if request.method == "POST":
   ...
  ...

app.add_url_rule('/my-view', view_func=MyView.as_view('my-view'))
```

### Method Dispatching and APIs

Use `MethodView` to handle different HTTP methods with separate class methods.

```py
from flask.views import MethodView

class ItemAPI(MethodView):
 init_every_request = False

 def __init__(self, model):
  self.model = model
  self.validator = generate_validator(model)

 def _get_item(self, id):
  return self.model.query.get_or_404(id)

 def get(self, id):
  item = self._get_item(id)
  return jsonify(item.to_json())

 def patch(self, id):
  item = self._get_item(id)
  errors = self.validator.validate(item, request.json)

  if errors:
   return jsonify(errors), 400

  item.update_from_json(request.json)
  db.session.commit()
  return jsonify(item.to_json())

 def delete(self, id):
  item = self._get_item(id)
  db.session.delete(item)
  db.session.commit()
  return "", 204

class GroupAPI(MethodView):
 init_every_request = False

 def __init__(self, model):
  self.model = model
  self.validator = generate_validator(model, create=True)

 def get(self):
  items = self.model.query.all()
  return jsonify([item.to_json() for item in items])

 def post(self):
  errors = self.validator.validate(request.json)

  if errors:
   return jsonify(errors), 400

  db.session.add(self.model.from_json(request.json))
  db.session.commit()
  return jsonify(item.to_json())

def register_api(app, model, name):
 item = ItemAPI.as_view(f"{name}-item", model)
 group = GroupAPI.as_view(f"{name}-group", model)
 app.add_url_rule(f"/{name}/<int:id>", view_func=item)
 app.add_url_rule(f"/{name}/", view_func=group)

register_api(app, User, "users")
register_api(app, Story, "stories")
```

#### REST API Endpoints

| URL| Method| Description|
|-|-|-|
| /users/| GET| List all users|
| /users/| POST| Create a new user|
| /users/<id>| GET| Show a user|
| /users/<id>| PATCH| Update a user|
| /users/<id>| DELETE| Delete a user|
| /stories/| GET| List all stories|
| /stories/| POST| Create a story|
| /stories/<id>| GET| Show a story|
| /stories/<id>| PATCH| Update a story|
| /stories/<id>| DELETE| Delete a story|

## Application Structure and Lifecycle

### Application Setup

Create the Flask application object and configure it before handling requests.

```py
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
 SECRET_KEY="dev",
)
app.config.from_prefixed_env()

@app.route("/")
def index():
 return "Hello, World!"
```

Ensure all setup is done before serving to maintain consistency across workers.

### Serving the Application

Use a WSGI server to serve the Flask application. During development, use:

```bash
flask run
```

For production, use a production-ready WSGI server.

### Middleware

Middleware wraps the WSGI application to modify requests or responses.

Example using Werkzeug’s `ProxyFix`:

```py
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
```

### How a Request is Handled

1. Client sends HTTP request.
2. WSGI server converts it to WSGI environ and calls the application.
3. Flask processes the request:
 - Creates `RequestContext` and `AppContext`.
 - Matches URL to view.
 - Calls view function.
 - Handles errors.
4. Response is sent back to the client.

## The Application Context

### Purpose of the Context

Access application-level data using `current_app` and `g` without importing the app instance.

### Lifetime of the Context

Created at the start of a request or CLI command and popped after.

### Manually Push a Context

Use `app.app_context()` when needed outside automatic contexts.

```py
def create_app():
 app = Flask(__name__)

 with app.app_context():
  init_db()

 return app
```

### Storing Data

Use `g` to store data during a request.

```py
from flask import g

def get_db():
 if 'db' not in g:
  g.db = connect_to_database()
 return g.db

@app.teardown_appcontext
def teardown_db(exception):
 db = g.pop('db', None)
 if db is not None:
  db.close()
```

Use `LocalProxy` for easier access:

```py
from werkzeug.local import LocalProxy
db = LocalProxy(get_db)
```

### Events and Signals

Signals like `appcontext_pushed`, `appcontext_tearing_down`, and `appcontext_popped` are sent during context lifecycle.

## The Request Context

### Purpose of the Context

Access request-level data using `request` and `session` proxies without passing the request object.

### Lifetime of the Context

Pushed at the start of a request and popped after. Unique to each worker.

### Manually Push a Context

Use `app.test_request_context()` for testing.

```py
def generate_report(year):
 format = request.args.get("format")
 ...

with app.test_request_context(
 "/make_report/2017", query_string={"format": "short"}
):
 generate_report()
```

### How the Context Works

Flask manages contexts using stacks. Proxies like `current_app` and `request` point to the top context.

### Callbacks and Errors

1. `before_request` functions run.
2. View function is called.
3. `after_request` functions modify the response.
4. Teardown functions run after response.

Handle exceptions with `errorhandler` functions. In debug mode, exceptions propagate to show the debugger.

### Teardown Callbacks

Executed when contexts are popped, regardless of exceptions.

```py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
 print('during view')
 return 'Hello, World!'

@app.teardown_request
def show_teardown(exception):
 print('after with block')

with app.test_request_context():
 print('during with block')

with app.test_client() as client:
 client.get('/')
 print(request.path)
```

### Signals

Signals like `request_started`, `request_finished`, `got_request_exception`, and `request_tearing_down` are sent during request lifecycle.

### Notes On Proxies

Proxies cannot perform instance checks. Use `_get_current_object()` to access the underlying object.

```py
app = current_app._get_current_object()
my_signal.send(app)
```

## Modular Applications with Blueprints

### Why Blueprints?

Blueprints allow you to organize your Flask application into reusable components, simplifying large applications and enabling extensions to register operations.

### The Concept of Blueprints

Blueprints record operations to execute when registered on an application, associating view functions and generating URLs.

### My First Blueprint

```py
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
      template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
 try:
  return render_template(f'pages/{page}.html')
 except TemplateNotFound:
  abort(404)
```

### Registering Blueprints

```py
from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
```

### Nesting Blueprints

```py
parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')

parent.register_blueprint(child)
app.register_blueprint(parent)
```

### Blueprint Resources

Blueprints can include static files, templates, and other resources.

### Blueprint Resource Folder

Blueprints have a `root_path` for resources.

```py
simple_page.root_path
'/Users/username/TestProject/yourapplication'

with simple_page.open_resource('static/style.css') as f:
 code = f.read()
```

### Static Files

```py
admin = Blueprint('admin', __name__, static_folder='static')
```

### Templates

Blueprint templates are added to the search path with lower priority than the application's templates.

### Building URLs

```py
url_for('admin.index')
url_for('.index')
```

### Blueprint Error Handlers

```py
@simple_page.errorhandler(404)
def page_not_found(e):
 return render_template('pages/404.html')
```

## Extensions

### Finding Extensions

Search PyPI for packages tagged with Framework :: Flask, usually named “Flask-Foo” or “Foo-Flask”.

### Using Extensions

```py
from flask_foo import Foo

foo = Foo()

app = Flask(__name__)
app.config.update(
 FOO_BAR='baz',
 FOO_SPAM='eggs',
)

foo.init_app(app)
```

### Building Extensions

Refer to Flask Extension Development for creating your own extensions.

## Command Line Interface

### Application Discovery

Use the `--app` option to specify your application.

### Run the Development Server

```bash
flask --app hello run
```

### Debug Mode

```bash
flask --app hello run --debug
```

### Watch and Ignore Files with the Reloader

```bash
flask run --extra-files file1:dirA/file2:dirB/
```

### Open a Shell

```bash
flask shell
```

### Environment Variables From dotenv

Flask loads environment variables from `.env` and `.flaskenv` if `python-dotenv` is installed.

### Setting Command Options

Set options via environment variables like `FLASK_RUN_PORT=8000`.

### Disable dotenv

Set `FLASK_SKIP_DOTENV=1` to prevent loading dotenv files.

### Environment Variables From virtualenv

Add variables to the virtualenv’s activate script.

### Custom Commands

```py
import click
from flask import Flask

app = Flask(__name__)

@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
 ...
```

### Registering Commands with Blueprints

```py
from flask import Blueprint

bp = Blueprint('students', __name__)

@bp.cli.command('create')
@click.argument('name')
def create(name):
 ...

app.register_blueprint(bp)
```

### Application Context

Commands run with an application context for access to app and config.

### Plugins

Define commands in `flask.commands` entry point in `pyproject.toml`.

### Custom Scripts

Create a Click script and define entry points for custom commands.

### PyCharm Integration

Configure PyCharm to run Flask commands by setting up a Python run configuration with the `flask` module.

## Development Server

### Command Line

```bash
flask --app hello run --debug
```

### Address already in use

Use a different port with `--port 5001` or stop the conflicting process.

### Deferred Errors on Reload

The server continues running and shows the debugger on code changes.

### In Code

```py
if __name__ == "__main__":
 app.run(debug=True)
```

## Working with the Shell

### Command Line Interface

Use `flask shell` for an interactive shell with the app context.

### Creating a Request Context

```py
ctx = app.test_request_context()
ctx.push()
# work with request
ctx.pop()
```

### Firing Before/After Request

```py
ctx = app.test_request_context()
ctx.push()
app.preprocess_request()
app.process_response(app.response_class())
ctx.pop()
```

### Further Improving the Shell Experience

Import commonly used modules and define helper functions in a separate module.

```py
from shelltools import *
```

## Patterns for Flask

Common patterns like database connections and user authentication are widely used. Flask facilitates implementing these patterns.

### Large Applications as Packages

#### Simple Packages

For large applications, use a package structure:

```
/yourapplication
 yourapplication.py
 /static
  style.css
 /templates
  layout.html
  index.html
  login.html
  ...
```

Convert to a package by:

```
/yourapplication
 /yourapplication
  __init__.py
  /static
   style.css
  /templates
   layout.html
   index.html
   login.html
   ...
```

Create `pyproject.toml`:

```toml
[project]
name = "yourapplication"
dependencies = [
 "flask",
]

[build-system]
requires = ["flit_core<4"]
build-backend = "flit_core.buildapi"
```

Install the application:

```bash
pip install -e .
```

Run with Flask:

```bash
flask --app yourapplication run
```

#### Checklist

1. Create the Flask app in `__init__.py`.
2. Import view modules in `__init__.py`.

Example `__init__.py`:

```py
from flask import Flask
app = Flask(__name__)

import yourapplication.views
```

Example `views.py`:

```py
from yourapplication import app

@app.route('/')
def index():
 return 'Hello World!'
```

### Application Factories

Create the app object in a function for flexibility.

#### Basic Factories

```py
def create_app(config_filename):
 app = Flask(__name__)
 app.config.from_pyfile(config_filename)

 from yourapplication.model import db
 db.init_app(app)

 from yourapplication.views.admin import admin
 from yourapplication.views.frontend import frontend
 app.register_blueprint(admin)
 app.register_blueprint(frontend)

 return app
```

Use `current_app` in blueprints:

```py
from flask import current_app, Blueprint, render_template
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
 return render_template(current_app.config['INDEX_TEMPLATE'])
```

#### Factories & Extensions

Initialize extensions without binding to the app:

```py
## model.py
db = SQLAlchemy()

## application.py
def create_app(config_filename):
 app = Flask(__name__)
 app.config.from_pyfile(config_filename)

 from yourapplication.model import db
 db.init_app(app)
```

#### Using Applications

Run with Flask:

```bash
flask --app hello run
```

### Application Dispatching

Combine multiple WSGI applications.

#### Combining Applications

```py
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from frontend_app import application as frontend
from backend_app import application as backend

application = DispatcherMiddleware(frontend, {
 '/backend': backend
})
```

#### Dispatch by Subdomain

```py
from threading import Lock

class SubdomainDispatcher:

 def __init__(self, domain, create_app):
  self.domain = domain
  self.create_app = create_app
  self.lock = Lock()
  self.instances = {}

 def get_application(self, host):
  host = host.split(':')[0]
  assert host.endswith(self.domain), 'Configuration error'
  subdomain = host[:-len(self.domain)].rstrip('.')
  with self.lock:
   app = self.instances.get(subdomain)
   if app is None:
    app = self.create_app(subdomain)
    self.instances[subdomain] = app
   return app

 def __call__(self, environ, start_response):
  app = self.get_application(environ['HTTP_HOST'])
  return app(environ, start_response)
```

Usage:

```py
from myapplication import create_app, get_user_for_subdomain
from werkzeug.exceptions import NotFound

def make_app(subdomain):
 user = get_user_for_subdomain(subdomain)
 if user is None:
  return NotFound()
 return create_app(user)

application = SubdomainDispatcher('example.com', make_app)
```

#### Dispatch by Path

```py
from threading import Lock
from wsgiref.util import shift_path_info

class PathDispatcher:

 def __init__(self, default_app, create_app):
  self.default_app = default_app
  self.create_app = create_app
  self.lock = Lock()
  self.instances = {}

 def get_application(self, prefix):
  with self.lock:
   app = self.instances.get(prefix)
   if app is None:
    app = self.create_app(prefix)
    if app is not None:
     self.instances[prefix] = app
   return app

 def __call__(self, environ, start_response):
  app = self.get_application(_peek_path_info(environ))
  if app is not None:
   shift_path_info(environ)
  else:
   app = self.default_app
  return app(environ, start_response)

def _peek_path_info(environ):
 segments = environ.get("PATH_INFO", "").lstrip("/").split("/", 1)
 if segments:
  return segments[0]
 return None
```

Usage:

```py
from myapplication import create_app, default_app, get_user_for_prefix

def make_app(prefix):
 user = get_user_for_prefix(prefix)
 if user is not None:
  return create_app(user)

application = PathDispatcher(default_app, make_app)
```

### Using URL Processors

#### Internationalized Application URLs

```py
from flask import Flask, g

app = Flask(__name__)

@app.route('/<lang_code>/')
def index(lang_code):
 g.lang_code = lang_code
 ...
```

URL defaults:

```py
@app.url_defaults
def add_language_code(endpoint, values):
 if 'lang_code' in values or not g.lang_code:
  return
 if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
  values['lang_code'] = g.lang_code
```

URL value preprocessors:

```py
@app.url_value_preprocessor
def pull_lang_code(endpoint, values):
 g.lang_code = values.pop('lang_code', None)
```

Example routes:

```py
@app.route('/<lang_code>/')
def index():
 ...

@app.route('/<lang_code>/about')
def about():
 ...
```

#### Internationalized Blueprint URLs

```py
from flask import Blueprint, g

bp = Blueprint('frontend', __name__, url_prefix='/<lang_code>')

@bp.url_defaults
def add_language_code(endpoint, values):
 values.setdefault('lang_code', g.lang_code)

@bp.url_value_preprocessor
def pull_lang_code(endpoint, values):
 g.lang_code = values.pop('lang_code')

@bp.route('/')
def index():
 ...

@bp.route('/about')
def about():
 ...
```

### Using SQLite 3 with Flask

#### Connect on Demand

```py
import sqlite3
from flask import g

DATABASE = '/path/to/database.db'

def get_db():
 db = getattr(g, '_database', None)
 if db is None:
  db = g._database = sqlite3.connect(DATABASE)
 return db

@app.teardown_appcontext
def close_connection(exception):
 db = getattr(g, '_database', None)
 if db is not None:
  db.close()
```

#### Easy Querying

```py
def make_dicts(cursor, row):
 return dict((cursor.description[idx][0], value)
    for idx, value in enumerate(row))

db.row_factory = sqlite3.Row
```

```py
def query_db(query, args=(), one=False):
 cur = get_db().execute(query, args)
 rv = cur.fetchall()
 cur.close()
 return (rv[0] if rv else None) if one else rv
```

Usage:

```py
for user in query_db('select * from users'):
 print(user['username'], 'has the id', user['user_id'])

user = query_db('select * from users where username = ?',
    [the_username], one=True)
if user is None:
 print('No such user')
else:
 print(the_username, 'has the id', user['user_id'])
```

#### Initial Schemas

```py
def init_db():
 with app.app_context():
  db = get_db()
  with app.open_resource('schema.sql', mode='r') as f:
   db.cursor().executescript(f.read())
  db.commit()
```

Usage:

```py
from yourapplication import init_db
init_db()
```

### SQLAlchemy in Flask

#### Flask-SQLAlchemy Extension

Install via PyPI.

#### Declarative

```py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False,
           autoflush=False,
           bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
 import yourapplication.models
 Base.metadata.create_all(bind=engine)
```

```py
from yourapplication.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
 db_session.remove()
```

Example model:

```py
from sqlalchemy import Column, Integer, String
from yourapplication.database import Base

class User(Base):
 __tablename__ = 'users'
 id = Column(Integer, primary_key=True)
 name = Column(String(50), unique=True)
 email = Column(String(120), unique=True)

 def __init__(self, name=None, email=None):
  self.name = name
  self.email = email

 def __repr__(self):
  return f'<User {self.name!r}>'
```

Initialize DB:

```py
from yourapplication.database import init_db
init_db()
```

Insert:

```py
from yourapplication.database import db_session
from yourapplication.models import User
u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()
```

Query:

```py
User.query.all()
User.query.filter(User.name == 'admin').first()
```

#### Manual Object Relational Mapping

```py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:////tmp/test.db')
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
           autoflush=False,
           bind=engine))
def init_db():
 metadata.create_all(bind=engine)
```

```py
from yourapplication.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
 db_session.remove()
```

Example table and model:

```py
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from yourapplication.database import metadata, db_session

class User(object):
 query = db_session.query_property()

 def __init__(self, name=None, email=None):
  self.name = name
  self.email = email

 def __repr__(self):
  return f'<User {self.name!r}>'

users = Table('users', metadata,
 Column('id', Integer, primary_key=True),
 Column('name', String(50), unique=True),
 Column('email', String(120), unique=True)
)
mapper(User, users)
```

#### SQL Abstraction Layer

```py
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:////tmp/test.db')
metadata = MetaData(bind=engine)
```

Load tables:

```py
from sqlalchemy import Table

users = Table('users', metadata, autoload=True)
```

Insert:

```py
con = engine.connect()
con.execute(users.insert(), name='admin', email='admin@localhost')
```

Query:

```py
users.select(users.c.id == 1).execute().first()
```

```py
r = users.select(users.c.id == 1).execute().first()
r['name']
```

Using strings:

```py
engine.execute('select * from users where id = :1', [1]).first()
```

### Uploading Files

#### A Gentle Introduction

Basic file upload process:

1. `<form>` with `enctype=multipart/form-data` and `<input type=file>`.
2. Access file from `request.files`.
3. Save with `file.save()`.

Example:

```py
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
```

```py
def allowed_file(filename):
 return '.' in filename and \
     filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
 if request.method == 'POST':
  if 'file' not in request.files:
   flash('No file part')
   return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
   flash('No selected file')
   return redirect(request.url)
  if file and allowed_file(file.filename):
   filename = secure_filename(file.filename)
   file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   return redirect(url_for('download_file', name=filename))
 return '''
 <!doctype html>
 <title>Upload new File</title>
 <h1>Upload new File</h1>
 <form method=post enctype=multipart/form-data>
   <input type=file name=file>
   <input type=submit value=Upload>
 </form>
 '''
```

Secure filename:

```py
secure_filename('../../../../home/username/.bashrc')
## 'home_username_.bashrc'
```

Download file:

```py
from flask import send_from_directory

@app.route('/uploads/<name>')
def download_file(name):
 return send_from_directory(app.config["UPLOAD_FOLDER"], name)
```

Alternatively, register as build_only:

```py
app.add_url_rule(
 "/uploads/<name>", endpoint="download_file", build_only=True
)
```

#### Improving Uploads

Limit file size:

```py
from flask import Flask, Request

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
```

#### Upload Progress Bars

Use JavaScript libraries or Flask extensions for progress bars.

### Caching

Use Flask-Caching for caching.

### View Decorators

#### Login Required Decorator

```py
from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
 @wraps(f)
 def decorated_function(*args, kwargs):
  if g.user is None:
   return redirect(url_for('login', next=request.url))
  return f(*args, kwargs)
 return decorated_function
```

Usage:

```py
@app.route('/secret_page')
@login_required
def secret_page():
 pass
```

#### Caching Decorator

```py
from functools import wraps
from flask import request

def cached(timeout=5 * 60, key='view/{}'):
 def decorator(f):
  @wraps(f)
  def decorated_function(*args, kwargs):
   cache_key = key.format(request.path)
   rv = cache.get(cache_key)
   if rv is not None:
    return rv
   rv = f(*args, kwargs)
   cache.set(cache_key, rv, timeout=timeout)
   return rv
  return decorated_function
 return decorator
```

#### Templating Decorator

```py
from functools import wraps
from flask import request, render_template

def templated(template=None):
 def decorator(f):
  @wraps(f)
  def decorated_function(*args, kwargs):
   template_name = template
   if template_name is None:
    template_name = f"{request.endpoint.replace('.', '/')}.html"
   ctx = f(*args, kwargs)
   if ctx is None:
    ctx = {}
   elif not isinstance(ctx, dict):
    return ctx
   return render_template(template_name, ctx)
  return decorated_function
 return decorator
```

Usage:

```py
@app.route('/')
@templated('index.html')
def index():
 return dict(value=42)
```

#### Endpoint Decorator

```py
from flask import Flask
from werkzeug.routing import Rule

app = Flask(__name__)
app.url_map.add(Rule('/', endpoint='index'))

@app.endpoint('index')
def my_index():
 return "Hello world"
```

### Form Validation with WTForms

#### The Forms

```py
from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
 username = StringField('Username', [validators.Length(min=4, max=25)])
 email = StringField('Email Address', [validators.Length(min=6, max=35)])
 password = PasswordField('New Password', [
  validators.DataRequired(),
  validators.EqualTo('confirm', message='Passwords must match')
 ])
 confirm = PasswordField('Repeat Password')
 accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
```

#### In the View

```py
@app.route('/register', methods=['GET', 'POST'])
def register():
 form = RegistrationForm(request.form)
 if request.method == 'POST' and form.validate():
  user = User(form.username.data, form.email.data,
     form.password.data)
  db_session.add(user)
  flash('Thanks for registering')
  return redirect(url_for('login'))
 return render_template('register.html', form=form)
```

#### Forms in Templates

```html
{% from "_formhelpers.html" import render_field %}
<form method=post>
  <dl>
 {{ render_field(form.username) }}
 {{ render_field(form.email) }}
 {{ render_field(form.password) }}
 {{ render_field(form.confirm) }}
 {{ render_field(form.accept_tos) }}
  </dl>
  <p><input type=submit value=Register>
</form>
```

### Template Inheritance

#### Base Template

```html
<!doctype html>
<html>
  <head>
 {% block head %}
 <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
 <title>{% block title %}{% endblock %} - My Webpage</title>
 {% endblock %}
  </head>
  <body>
 <div id="content">{% block content %}{% endblock %}</div>
 <div id="footer">
   {% block footer %}
   &copy; Copyright 2010 by <a href="http://domain.invalid/">you</a>.
   {% endblock %}
 </div>
  </body>
</html>
```

#### Child Template

```html
{% extends "layout.html" %}
{% block title %}Index{% endblock %}
{% block head %}
  {{ super() }}
  <style type="text/css">
 .important { color: #336699; }
  </style>
{% endblock %}
{% block content %}
  <h1>Index</h1>
  <p class="important">
 Welcome on my awesome homepage.
{% endblock %}
```

### Message Flashing

#### Simple Flashing

```py
from flask import Flask, flash, redirect, render_template, \
  request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
 error = None
 if request.method == 'POST':
  if request.form['username'] != 'admin' or \
    request.form['password'] != 'secret':
   error = 'Invalid credentials'
  else:
   flash('You were successfully logged in')
   return redirect(url_for('index'))
 return render_template('login.html', error=error)
```

```html
<!doctype html>
<title>My Application</title>
{% with messages = get_flashed_messages() %}
  {% if messages %}
 <ul class=flashes>
 {% for message in messages %}
   <li>{{ message }}</li>
 {% endfor %}
 </ul>
  {% endif %}
{% endwith %}
{% block body %}{% endblock %}
```

```html
{% extends "layout.html" %}
{% block body %}
  <h1>Overview</h1>
  <p>Do you want to <a href="{{ url_for('login') }}">log in?</a>
{% endblock %}
```

```html
{% extends "layout.html" %}
{% block body %}
  <h1>Login</h1>
  {% if error %}
 <p class=error><strong>Error:</strong> {{ error }}
  {% endif %}
  <form method=post>
 <dl>
   <dt>Username:
   <dd><input type=text name=username value="{{ request.form.username }}">
   <dt>Password:
   <dd><input type=password name=password>
 </dl>
 <p><input type=submit value=Login>
  </form>
{% endblock %}
```

#### Flashing With Categories

```py
flash('Invalid password provided', 'error')
```

```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
 <ul class=flashes>
 {% for category, message in messages %}
   <li class="{{ category }}">{{ message }}</li>
 {% endfor %}
 </ul>
  {% endif %}
{% endwith %}
```

#### Filtering Flash Messages

```html
{% with errors = get_flashed_messages(category_filter=["error"]) %}
{% if errors %}
<div class="alert-message block-message error">
  <a class="close" href="#">×</a>
  <ul>
 {%- for msg in errors %}
 <li>{{ msg }}</li>
 {% endfor -%}
  </ul>
</div>
{% endif %}
{% endwith %}
```

### JavaScript, fetch, and JSON

#### Rendering Templates

```py
data = generate_report()
return render_template("report.html", chart_data=data)
```

```html
<script>
 const chart_data = {{ chart_data|tojson }}
 chartLib.makeChart(chart_data)
</script>
```

#### Generating URLs

```py
const user_url = {{ url_for("user", id=current_user.id)|tojson }}
fetch(user_url).then(...)
```

```html
const SCRIPT_ROOT = {{ request.script_root|tojson }}
let user_id = ...
let user_url = `${SCRIPT_ROOT}/user/${user_id}`
fetch(user_url).then(...)
```

#### Making a Request with fetch

```js
const room_url = {{ url_for("room_detail", id=room.id)|tojson }}
fetch(room_url)
 .then(response => response.json())
 .then(data => {
  // data is a parsed JSON object
 })
```

```js
let data = new FormData()
data.append("name", "Flask Room")
data.append("description", "Talk about Flask here.")
fetch(room_url, {
 "method": "POST",
 "body": data,
}).then(...)
```

```js
let data = {
 "name": "Flask Room",
 "description": "Talk about Flask here.",
}
fetch(room_url, {
 "method": "POST",
 "headers": {"Content-Type": "application/json"},
 "body": JSON.stringify(data),
}).then(...)
```

#### Following Redirects

```js
fetch("/login", {"body": ...}).then(
 response => {
  if (response.redirected) {
   window.location = response.url
  } else {
   showLoginError()
  }
 }
)
```

#### Replacing Content

```html
<div id="geology-fact">
 {{ include "geology_fact.html" }}
</div>
<script>
 const geology_url = {{ url_for("geology_fact")|tojson }}
 const geology_div = getElementById("geology-fact")
 fetch(geology_url)
  .then(response => response.text)
  .then(text => geology_div.innerHTML = text)
</script>
```

#### Return JSON from Views

```py
@app.route("/user/<int:id>")
def user_detail(id):
 user = User.query.get_or_404(id)
 return {
  "username": User.username,
  "email": User.email,
  "picture": url_for("static", filename=f"users/{id}/profile.png"),
 }
```

```py
from flask import jsonify

@app.route("/users")
def user_list():
 users = User.query.order_by(User.name).all()
 return jsonify([u.to_json() for u in users])
```

#### Receiving JSON in Views

```py
from flask import request

@app.post("/user/<int:id>")
def user_update(id):
 user = User.query.get_or_404(id)
 user.update_from_json(request.json)
 db.session.commit()
 return user.to_json()
```

### Lazily Loading Views

#### Converting to Centralized URL Map

Views without decorators in `views.py`:

```py
def index():
 pass

def user(username):
 pass
```

URL mapping:

```py
from flask import Flask
from yourapplication import views
app = Flask(__name__)
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/user/<username>', view_func=views.user)
```

#### Loading Late

```py
from werkzeug.utils import import_string, cached_property

class LazyView(object):

 def __init__(self, import_name):
  self.__module__, self.__name__ = import_name.rsplit('.', 1)
  self.import_name = import_name

 @cached_property
 def view(self):
  return import_string(self.import_name)

 def __call__(self, *args, kwargs):
  return self.view(*args, kwargs)
```

Usage:

```py
from yourapplication.helpers import LazyView
app.add_url_rule('/',
     view_func=LazyView('yourapplication.views.index'))
app.add_url_rule('/user/<username>',
     view_func=LazyView('yourapplication.views.user'))
```

Helper function:

```py
def url(import_name, url_rules=[], options):
 view = LazyView(f"yourapplication.{import_name}")
 for url_rule in url_rules:
  app.add_url_rule(url_rule, view_func=view, options)

## add a single route to the index view
url('views.index', ['/'])

## add two routes to a single function endpoint
url_rules = ['/user/','/user/<username>']
url('views.user', url_rules)
```

### MongoDB with MongoEngine

#### Configuration

```py
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 "db": "myapp",
}
db = MongoEngine(app)
```

#### Mapping Documents

```py
import mongoengine as me

class Movie(me.Document):
 title = me.StringField(required=True)
 year = me.IntField()
 rated = me.StringField()
 director = me.StringField()
 actors = me.ListField()
```

Nested documents:

```py
class Imdb(me.EmbeddedDocument):
 imdb_id = me.StringField()
 rating = me.DecimalField()
 votes = me.IntField()

class Movie(me.Document):
 ...
 imdb = me.EmbeddedDocumentField(Imdb)
```

#### Creating Data

```py
bttf = Movie(title="Back To The Future", year=1985)
bttf.actors = [
 "Michael J. Fox",
 "Christopher Lloyd"
]
bttf.imdb = Imdb(imdb_id="tt0088763", rating=8.5)
bttf.save()
```

#### Queries

```py
bttf = Movies.objects(title="Back To The Future").get_or_404()

some_theron_movie = Movie.objects(actors__in=["Charlize Theron"]).first()

for recents in Movie.objects(year__gte=2017):
 print(recents.title)
```

### Streaming Contents

#### Basic Usage

```py
@app.route('/large.csv')
def generate_large_csv():
 def generate():
  for row in iter_all_rows():
   yield f"{','.join(row)}\n"
 return generate(), {"Content-Type": "text/csv"}
```

#### Streaming from Templates

```py
from flask import stream_template

@app.get("/timeline")
def timeline():
 return stream_template("timeline.html")
```

#### Streaming with Context

```py
from flask import stream_with_context, request
from markupsafe import escape

@app.route('/stream')
def streamed_response():
 def generate():
  yield '<p>Hello '
  yield escape(request.args['name'])
  yield '!</p>'
 return stream_with_context(generate())
```

### Deferred Request Callbacks

Use `after_this_request()` to register response modifications.

```py
from flask import request, after_this_request

@app.before_request
def detect_user_language():
 language = request.cookies.get('user_lang')

 if language is None:
  language = guess_language_from_request()

  @after_this_request
  def remember_language(response):
   response.set_cookie('user_lang', language)
   return response

 g.language = language
```

### Adding HTTP Method Overrides

#### Middleware

```py
class HTTPMethodOverrideMiddleware(object):
 allowed_methods = frozenset([
  'GET',
  'HEAD',
  'POST',
  'DELETE',
  'PUT',
  'PATCH',
  'OPTIONS'
 ])
 bodyless_methods = frozenset(['GET', 'HEAD', 'OPTIONS', 'DELETE'])

 def __init__(self, app):
  self.app = app

 def __call__(self, environ, start_response):
  method = environ.get('HTTP_X_HTTP_METHOD_OVERRIDE', '').upper()
  if method in self.allowed_methods:
   environ['REQUEST_METHOD'] = method
  if method in self.bodyless_methods:
   environ['CONTENT_LENGTH'] = '0'
  return self.app(environ, start_response)
```

Usage:

```py
from flask import Flask

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
```

### Request Content Checksums

Wrap the input stream to calculate checksum.

```py
import hashlib

class ChecksumCalcStream(object):

 def __init__(self, stream):
  self._stream = stream
  self._hash = hashlib.sha1()

 def read(self, bytes):
  rv = self._stream.read(bytes)
  self._hash.update(rv)
  return rv

 def readline(self, size_hint):
  rv = self._stream.readline(size_hint)
  self._hash.update(rv)
  return rv

def generate_checksum(request):
 env = request.environ
 stream = ChecksumCalcStream(env['wsgi.input'])
 env['wsgi.input'] = stream
 return stream._hash
```

Usage:

```py
@app.route('/special-api', methods=['POST'])
def special_api():
 hash = generate_checksum(request)
 files = request.files
 checksum = hash.hexdigest()
 return f"Hash was: {checksum}"
```

### Background Tasks with Celery

#### Install

```bash
pip install celery
```

#### Integrate Celery with Flask

```py
from celery import Celery, Task

def celery_init_app(app: Flask) -> Celery:
 class FlaskTask(Task):
  def __call__(self, *args: object, kwargs: object) -> object:
   with app.app_context():
    return self.run(*args, kwargs)

 celery_app = Celery(app.name, task_cls=FlaskTask)
 celery_app.config_from_object(app.config["CELERY"])
 celery_app.set_default()
 app.extensions["celery"] = celery_app
 return celery_app
```

Example `example.py`:

```py
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
 CELERY=dict(
  broker_url="redis://localhost",
  result_backend="redis://localhost",
  task_ignore_result=True,
 ),
)
celery_app = celery_init_app(app)
```

Run Celery worker:

```bash
celery -A example worker --loglevel INFO
```

Run Celery beat:

```bash
celery -A example beat --loglevel INFO
```

#### Application Factory

```py
def create_app() -> Flask:
 app = Flask(__name__)
 app.config.from_mapping(
  CELERY=dict(
   broker_url="redis://localhost",
   result_backend="redis://localhost",
   task_ignore_result=True,
  ),
 )
 app.config.from_prefixed_env()
 celery_init_app(app)
 return app
```

`make_celery.py`:

```py
from example import create_app

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
```

Run worker:

```bash
celery -A make_celery worker --loglevel INFO
celery -A make_celery beat --loglevel INFO
```

#### Defining Tasks

```py
from celery import shared_task

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
 return a + b
```

#### Calling Tasks

```py
from flask import request

@app.post("/add")
def start_add() -> dict[str, object]:
 a = request.form.get("a", type=int)
 b = request.form.get("b", type=int)
 result = add_together.delay(a, b)
 return {"result_id": result.id}
```

#### Getting Results

```py
from celery.result import AsyncResult

@app.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
 result = AsyncResult(id)
 return {
  "ready": result.ready(),
  "successful": result.successful(),
  "value": result.result if result.ready() else None,
 }
```

#### Passing Data to Tasks

```py
@shared_task
def generate_user_archive(user_id: str) -> None:
 user = db.session.get(User, user_id)
 ...
```

Usage:

```py
generate_user_archive.delay(current_user.id)
```

### Subclassing Flask

Override Flask's functionality by subclassing.

```py
from flask import Flask, Request
from werkzeug.datastructures import ImmutableOrderedMultiDict
class MyRequest(Request):
 """Request subclass to override request parameter storage"""
 parameter_storage_class = ImmutableOrderedMultiDict

class MyFlask(Flask):
 """Flask subclass using the custom request class"""
 request_class = MyRequest
```

### Single-Page Applications

Serve SPA with Flask by placing static files and a catch-all route.

```py
from flask import Flask, jsonify

app = Flask(__name__, static_folder='app', static_url_path="/app")

@app.route("/heartbeat")
def heartbeat():
 return jsonify({"status": "healthy"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
 return app.send_static_file("index.html")
```

## Security Considerations

### Resource Use

Limit request data and form sizes to prevent DoS attacks.

```py
# Example configuration
app.config.update(
 MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16 MB
 MAX_FORM_MEMORY_SIZE=500 * 1024,   # 500 KB
 MAX_FORM_PARTS=1000
)
```

### Cross-Site Scripting (XSS)

Ensure proper escaping and use Content Security Policy.

```html
<input value="{{ value }}">
<a href="{{ value }}">click here</a>
```

```py
# Setting CSP header
response.headers['Content-Security-Policy'] = "default-src 'self'"
```

### Cross-Site Request Forgery (CSRF)

Use tokens to validate state-changing requests.

```py
@app.route('/login', methods=['POST'])
def login():
 ...
 session.clear()
 session['user_id'] = user.id
 session.permanent = True
 ...
```

### JSON Security

Use `jsonify()` to safely serialize data.

```py
from flask import jsonify

@app.route('/data')
def data():
 return jsonify([1, 2, 3])
```

### Security Headers

#### HTTP Strict Transport Security (HSTS)

Force HTTPS connections.

```py
response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
```

#### Content Security Policy (CSP)

Control resource loading.

```py
response.headers['Content-Security-Policy'] = "default-src 'self'"
```

#### X-Content-Type-Options

Prevent MIME type sniffing.

```py
response.headers['X-Content-Type-Options'] = 'nosniff'
```

#### X-Frame-Options

Prevent clickjacking.

```py
response.headers['X-Frame-Options'] = 'SAMEORIGIN'
```

#### Set-Cookie Options

Secure cookies with `Secure`, `HttpOnly`, and `SameSite`.

```py
app.config.update(
 SESSION_COOKIE_SECURE=True,
 SESSION_COOKIE_HTTPONLY=True,
 SESSION_COOKIE_SAMESITE='Lax',
)

response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
```

#### HTTP Public Key Pinning (HPKP)

Authenticate server certificates.

```py
# Example configuration
response.headers['Public-Key-Pins'] = 'pin-sha256="..."; max-age=5184000; includeSubDomains'
```

#### Copy/Paste to Terminal

Sanitize input to prevent hidden characters.

```py
body = body.replace("\b", "")
```

## Deploying to Production

### Self-Hosted Options

#### Gunicorn

A Python WSGI server.

```bash
# Installing
$ pip install gunicorn

# Running
$ gunicorn -w 4 'hello:app'

# Binding Externally
$ gunicorn -w 4 -b 0.0.0.0 'hello:create_app()'
```

#### Waitress

A pure Python WSGI server.

```bash
# Installing
$ pip install waitress

# Running
$ waitress-serve --host 127.0.0.1 hello:app

# Binding Externally
$ waitress-serve --host 0.0.0.0 hello:app
```

#### mod_wsgi

Integrates with Apache.

```py
# wsgi.py
from hello import app
application = app
```

```bash
# Running
$ mod_wsgi-express start-server wsgi.py --processes 4
```

#### uWSGI

A fast, compiled server suite.

```bash
# Installing
$ pip install pyuwsgi

# Running
$ uwsgi --http 127.0.0.1:8000 --master -p 4 -w hello:app

# Binding Externally
$ uwsgi --http 0.0.0.0:8000 --master -p 4 -w wsgi:app
```

### Hosting Platforms

Use services like PythonAnywhere, Google App Engine, AWS Elastic Beanstalk, etc.

### Tell Flask it is Behind a Proxy

Configure Flask to trust proxy headers.

```py
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
 app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
```

### nginx

Configure nginx as a reverse proxy.

```nginx
server {
 listen 80;
 server_name _;

 location / {
  proxy_pass http://127.0.0.1:8000/;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  proxy_set_header X-Forwarded-Proto $scheme;
  proxy_set_header X-Forwarded-Host $host;
  proxy_set_header X-Forwarded-Prefix /;
 }
}
```

### Apache httpd

Configure Apache as a reverse proxy.

```apache
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
ProxyPass / http://127.0.0.1:8000/
RequestHeader set X-Forwarded-Proto http
RequestHeader set X-Forwarded-Prefix /
```

## Using async and await

```py
@app.route("/get-data")
async def get_data():
 data = await async_db_query(...)
 return jsonify(data)
```

### Performance

Async views run in an event loop but still use one worker per request.

### Background tasks

Use task queues instead of spawning tasks in views.

### When to use Quart instead

Consider Quart for async-first applications.

### Extensions

Ensure extensions support async with `ensure_sync()`.

### Other event loops

Flask supports asyncio; other loops require custom handling.
