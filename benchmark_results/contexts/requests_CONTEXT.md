## ARCHITECTURE

A python-based project composed of the following subsystems:

- **tests/**: Primary subsystem containing 38 files
- **docs/**: Primary subsystem containing 26 files
- **src/**: Primary subsystem containing 18 files
- **ext/**: Primary subsystem containing 1 files
- **Root**: Contains scripts and execution points

## ENTRY_POINTS

*No entry points identified within budget.*

## SYMBOL_INDEX

**`src/requests/compat.py`**
- `_resolve_char_detection()`

**`src/requests/structures.py`**
- class `CaseInsensitiveDict`
  - `__init__()`
  - `__setitem__()`
  - `__getitem__()`
  - `__delitem__()`
  - `__iter__()`
  - `__len__()`
  - `lower_items()`
  - `__eq__()`
  - `copy()`
  - `__repr__()`
- class `LookupDict`
  - `__init__()`
  - `__repr__()`
  - `__getitem__()`
  - `get()`

**`src/requests/cookies.py`**
- class `MockRequest`
  - `__init__()`
  - `get_type()`
  - `get_host()`
  - `get_origin_req_host()`
  - `get_full_url()`
  - `is_unverifiable()`
  - `has_header()`
  - `get_header()`
  - `add_header()`
  - `add_unredirected_header()`
  - `get_new_headers()`
- class `MockResponse`
  - `__init__()`
  - `info()`
  - `getheaders()`
- `extract_cookies_to_jar()`
- `get_cookie_header()`
- `remove_cookie_by_name()`
- class `CookieConflictError`
- class `RequestsCookieJar`
  - `get()`
  - `set()`
  - `iterkeys()`
  - `keys()`
  - `itervalues()`
  - `values()`
  - `iteritems()`
  - `items()`
  - `list_domains()`
  - `list_paths()`
  - `multiple_domains()`
  - `get_dict()`
  - `__contains__()`
  - `__getitem__()`
  - `__setitem__()`
  - `__delitem__()`
  - `set_cookie()`
  - `update()`
  - `_find()`
  - `_find_no_duplicates()`
  - `__getstate__()`
  - `__setstate__()`
  - `copy()`
  - `get_policy()`
- `_copy_cookie_jar()`
- `create_cookie()`
- `morsel_to_cookie()`
- `cookiejar_from_dict()`
- `merge_cookies()`

**`src/requests/__init__.py`**
- `check_compatibility()`
- `_check_cryptography()`

**`src/requests/exceptions.py`**
- class `RequestException`
  - `__init__()`
- class `InvalidJSONError`
- class `JSONDecodeError`
  - `__init__()`
  - `__reduce__()`
- class `HTTPError`
- class `ConnectionError`
- class `ProxyError`
- class `SSLError`
- class `Timeout`
- class `ConnectTimeout`
- class `ReadTimeout`
- class `URLRequired`
- class `TooManyRedirects`
- class `MissingSchema`
- class `InvalidSchema`
- class `InvalidURL`
- class `InvalidHeader`
- class `InvalidProxyURL`
- class `ChunkedEncodingError`
- class `ContentDecodingError`
- class `StreamConsumedError`
- class `RetryError`
- class `UnrewindableBodyError`
- class `RequestsWarning`
- class `FileModeWarning`
- class `RequestsDependencyWarning`

**`src/requests/_internal_utils.py`**
- `to_native_string()`
- `unicode_is_ascii()`

**`src/requests/utils.py`**
- `dict_to_sequence()`
- `super_len()`
- `get_netrc_auth()`
- `guess_filename()`
- `extract_zipped_paths()`
- `atomic_open()`
- `from_key_val_list()`
- `to_key_val_list()`
- `parse_list_header()`
- `parse_dict_header()`
- `unquote_header_value()`
- `dict_from_cookiejar()`
- `add_dict_to_cookiejar()`
- `get_encodings_from_content()`
- `_parse_content_type_header()`
- `get_encoding_from_headers()`
- `stream_decode_response_unicode()`
- `iter_slices()`
- `get_unicode_from_response()`
- `unquote_unreserved()`
- `requote_uri()`
- `address_in_network()`
- `dotted_netmask()`
- `is_ipv4_address()`
- `is_valid_cidr()`
- `set_environ()`
- `should_bypass_proxies()`
- `get_environ_proxies()`
- `select_proxy()`
- `resolve_proxies()`
- `default_user_agent()`
- `default_headers()`
- `parse_header_links()`
- `guess_json_utf()`
- `prepend_scheme_if_needed()`
- `get_auth_from_url()`
- `check_header_validity()`
- `_validate_header_part()`
- `urldefragauth()`
- `rewind_body()`

**`src/requests/models.py`**
- class `RequestEncodingMixin`
- class `RequestHooksMixin`
  - `register_hook()`
  - `deregister_hook()`
- class `Request`
  - `__init__()`
  - `__repr__()`
  - `prepare()`
- class `PreparedRequest`
  - `__init__()`
  - `prepare()`
  - `__repr__()`
  - `copy()`
  - `prepare_method()`
  - `prepare_url()`
  - `prepare_headers()`
  - `prepare_body()`
  - `prepare_content_length()`
  - `prepare_auth()`
  - `prepare_cookies()`
  - `prepare_hooks()`
- class `Response`
  - `__init__()`
  - `__enter__()`
  - `__exit__()`
  - `__getstate__()`
  - `__setstate__()`
  - `__repr__()`
  - `__bool__()`
  - `__nonzero__()`
  - `__iter__()`
  - `iter_content()`
  - `iter_lines()`
  - `json()`
  - `raise_for_status()`
  - `close()`

**`src/requests/auth.py`**
- `_basic_auth_str()`
- class `AuthBase`
  - `__call__()`
- class `HTTPBasicAuth`
  - `__init__()`
  - `__eq__()`
  - `__ne__()`
  - `__call__()`
- class `HTTPProxyAuth`
  - `__call__()`
- class `HTTPDigestAuth`
  - `__init__()`
  - `init_per_thread_state()`
  - `build_digest_header()`
  - `handle_redirect()`
  - `handle_401()`
  - `__call__()`
  - `__eq__()`
  - `__ne__()`

**`src/requests/sessions.py`**
- `merge_setting()`
- `merge_hooks()`
- class `SessionRedirectMixin`
  - `get_redirect_target()`
  - `should_strip_auth()`
  - `resolve_redirects()`
  - `rebuild_auth()`
  - `rebuild_proxies()`
  - `rebuild_method()`
- class `Session`
  - `__init__()`
  - `__enter__()`
  - `__exit__()`
  - `prepare_request()`
  - `request()`
  - `get()`
  - `options()`
  - `head()`
  - `post()`
  - `put()`
  - `patch()`
  - `delete()`
  - `send()`
  - `merge_environment_settings()`
  - `get_adapter()`
  - `close()`
  - `mount()`
  - `__getstate__()`
  - `__setstate__()`
- `session()`

**`src/requests/hooks.py`**
- `default_hooks()`
- `dispatch_hook()`

**`src/requests/adapters.py`**
- `_urllib3_request_context()`
- class `BaseAdapter`
  - `__init__()`
  - `send()`
  - `close()`
- class `HTTPAdapter`
  - `__init__()`
  - `__getstate__()`
  - `__setstate__()`
  - `init_poolmanager()`
  - `proxy_manager_for()`
  - `cert_verify()`
  - `build_response()`
  - `build_connection_pool_key_attributes()`
  - `get_connection_with_tls_context()`
  - `get_connection()`
  - `close()`
  - `request_url()`
  - `add_headers()`
  - `proxy_headers()`
  - `send()`

## IMPORTANT_CALL_PATHS

.coveragerc()

.git-blame-ignore-revs()

.gitignore()

.pre-commit-config()

.readthedocs()

AUTHORS()

HISTORY()

MANIFEST()

Makefile()

NOTICE()

README()

.nojekyll()

Makefile()

custom()

hacks()

sidebarintro()

sidebarlogo()

.gitignore()

flask_theme_support.FlaskyStyle()

api()

faq()

out-there()

recommended()

release-process()

support()

updates()

vulnerabilities()

conf()
  → __init__.check_compatibility()
  → exceptions.RequestException()
  → compat._resolve_char_detection()

authors()

contributing()

index()

make()

requirements()

advanced()

authentication()

install()

quickstart()

requests-logo()

requirements-dev()

setup()

__init__()

README()

Makefile()

README()

Makefile()

ca()

ca()

Makefile()

cert()

server()

Makefile()

README()

Makefile()

Makefile()

ca()

ca()

cert()

client()

Makefile()

ca()

ca()

Makefile()

cert()

server()

conftest.prepare_url()
  → compat._resolve_char_detection()

test_adapters.test_request_url_trims_leading_path_separators()
  → adapters._urllib3_request_context()
  → compat._resolve_char_detection()

test_help.test_system_ssl()
  → help._implementation()
  → __version__()

test_hooks.hook()
  → __init__.check_compatibility()
  → exceptions.RequestException()
  → compat._resolve_char_detection()

test_lowlevel.echo_response_handler()
  → compat._resolve_char_detection()

test_packages.test_can_access_urllib3_attribute()
  → __init__.check_compatibility()
  → exceptions.RequestException()
  → compat._resolve_char_detection()

test_requests.TestRequests()
  → compat._resolve_char_detection()

test_structures.TestCaseInsensitiveDict()
  → structures.CaseInsensitiveDict()
  → compat._resolve_char_detection()

test_testserver.TestTestServer()
  → __init__.check_compatibility()
  → exceptions.RequestException()
  → compat._resolve_char_detection()

test_utils.TestSuperLen()
  → structures.CaseInsensitiveDict()
  → compat._resolve_char_detection()

__init__()

tox()
## CORE_MODULES

### `src/requests/compat.py`

**Purpose:** requests.compat

**Functions:**
- `def _resolve_char_detection()`
  - Find supported character detection libraries.

### `src/requests/structures.py`

**Purpose:** requests.structures
**Depends on:** `compat`

**Types:**
- `CaseInsensitiveDict` (bases: `MutableMapping`) - A case-insensitive ``dict``-like object. methods: `__init__`, `__repr__`, `copy`, `lower_items`
- `LookupDict` (bases: `dict`) - Dictionary lookup object. methods: `__init__`, `__repr__`, `get`

### `src/requests/cookies.py`

**Purpose:** requests.cookies
**Depends on:** `_internal_utils`, `compat`

**Types:**
- `CookieConflictError` (bases: `RuntimeError`) - There are two cookies that meet the criteria specified in the cookie jar.
- `MockRequest` - Wraps a `requests.Request` to mimic a `urllib2.Request`. methods: `__init__`, `add_header`, `add_unredirected_header` (+8 more)

**Functions:**
- `def _copy_cookie_jar(jar)`
- `def cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)`
- `def create_cookie(name, value, **kwargs)`
- `def extract_cookies_to_jar(jar, request, response)`
- `def get_cookie_header(jar, request)`
- `def merge_cookies(cookiejar, cookies)`

### `src/requests/__init__.py`

**Purpose:** Requests HTTP Library
**Depends on:** `__version__`, `api`, `exceptions`, `models`, `packages`, `sessions`, `status_codes`, `utils`

**Functions:**
- `def _check_cryptography(cryptography_version)`
- `def check_compatibility(urllib3_version, chardet_version, charset_normalizer_version)`

### `src/requests/exceptions.py`

**Purpose:** requests.exceptions
**Depends on:** `compat`

**Types:**
- `ChunkedEncodingError` (bases: `RequestException`) - The server declared chunked encoding but sent an invalid chunk.
- `ConnectTimeout` (bases: `ConnectionError, Timeout`) - The request timed out while trying to connect to the remote server.
- `ConnectionError` (bases: `RequestException`) - A Connection error occurred.
- `ContentDecodingError` (bases: `RequestException, BaseHTTPError`) - Failed to decode response content.
- `FileModeWarning` (bases: `RequestsWarning, DeprecationWarning`) - A file was opened in text mode, but Requests determined its binary length.
- `HTTPError` (bases: `RequestException`) - An HTTP error occurred.

### `src/requests/_internal_utils.py`

**Purpose:** requests._internal_utils
**Depends on:** `compat`

**Functions:**
- `def to_native_string(string, encoding="ascii")`
  - Given a string object, regardless of type, returns a representation of
- `def unicode_is_ascii(u_string)`
  - Determine if unicode string only contains ASCII characters.

### `src/requests/utils.py`

**Purpose:** requests.utils
**Depends on:** `__version__`, `_internal_utils`, `certs`, `compat`, `cookies`, `exceptions`, +1 more

**Functions:**
- `def _parse_content_type_header(header)`
- `def _validate_header_part(header, header_part, header_validator_index)`
- `def add_dict_to_cookiejar(cj, cookie_dict)`
- `def address_in_network(ip, net)`
- `def atomic_open(filename)`
- `def check_header_validity(header)`
- `def default_headers()`
- `def default_user_agent(name="python-requests")`

**Notes:** large file (1085 lines)

### `src/requests/models.py`

**Purpose:** requests.models
**Depends on:** `_internal_utils`, `auth`, `compat`, `cookies`, `exceptions`, `hooks`, +3 more

**Types:**
- `PreparedRequest` (bases: `RequestEncodingMixin, RequestHooksMixin`) - The fully mutable :class:`PreparedRequest <PreparedRequest>` object, methods: `__init__`, `__repr__`, `copy`, `prepare` (+8 more)
- `Request` (bases: `RequestHooksMixin`) - A user-created :class:`Request <Request>` object. methods: `__init__`, `__repr__`, `prepare`
- `RequestEncodingMixin`
- `RequestHooksMixin` methods: `deregister_hook`, `register_hook`

**Notes:** decorator-heavy (12 decorators); large file (1042 lines)

### `src/requests/auth.py`

**Purpose:** requests.auth
**Depends on:** `_internal_utils`, `compat`, `cookies`, `utils`

**Types:**
- `AuthBase` - Base class that all auth implementations derive from methods: `__call__`
- `HTTPBasicAuth` (bases: `AuthBase`) - Attaches HTTP Basic Authentication to the given Request object. methods: `__call__`, `__init__`
- `HTTPDigestAuth` (bases: `AuthBase`) - Attaches HTTP Digest Authentication to the given Request object. methods: `__call__`, `__init__`, `build_digest_header`, `handle_401` (+2 more)

**Functions:**
- `def _basic_auth_str(username, password)`

**Notes:** large file (315 lines)

### `src/requests/sessions.py`

**Purpose:** requests.sessions
**Depends on:** `_internal_utils`, `adapters`, `auth`, `compat`, `cookies`, `exceptions`, +5 more

**Types:**
- `Session` (bases: `SessionRedirectMixin`) - A Requests session. methods: `__init__`, `close`, `delete`, `get` (+11 more)
- `SessionRedirectMixin` methods: `get_redirect_target`, `rebuild_auth`, `rebuild_method`, `rebuild_proxies` (+2 more)

**Functions:**
- `def merge_hooks(request_hooks, session_hooks, dict_class=OrderedDict)`
- `def merge_setting(request_setting, session_setting, dict_class=OrderedDict)`
- `def session()`

**Notes:** large file (835 lines)

### `src/requests/hooks.py`

**Purpose:** requests.hooks

**Functions:**
- `def default_hooks()`
- `def dispatch_hook(key, hooks, hook_data, **kwargs)`
  - Dispatches a hook dictionary on a given piece of data.

### `src/requests/adapters.py`

**Purpose:** requests.adapters
**Depends on:** `auth`, `compat`, `cookies`, `exceptions`, `models`, `structures`, `utils`

**Types:**
- `BaseAdapter` - The Base Transport Adapter methods: `__init__`, `close`, `send`
- `HTTPAdapter` (bases: `BaseAdapter`) - The built-in HTTP Adapter for urllib3. methods: `__init__`, `add_headers`, `build_connection_pool_key_attributes`, `build_response`, `cert_verify`, `close` (+7 more)

**Functions:**
- `def _urllib3_request_context(request: "PreparedRequest", ...) -> "(dict[str, typing.Any], dict[str, typing.Any])"`

**Notes:** large file (699 lines)

### `tox.ini`

**Purpose:** Implements tox.

## SUPPORTING_MODULES

*No supporting modules selected within budget.*

## DEPENDENCY_GRAPH

```mermaid
graph LR
    f0["src/requests/compat.py"]
    f1["src/requests/structures.py"]
    f2["src/requests/cookies.py"]
    f3["src/requests/__init__.py"]
    f4["src/requests/exceptions.py"]
    f5["src/requests/_internal_utils.py"]
    f6["src/requests/utils.py"]
    f7["src/requests/models.py"]
    f8["src/requests/auth.py"]
    f9["src/requests/sessions.py"]
    f10["src/requests/hooks.py"]
    f11["src/requests/adapters.py"]
    f12["tox.ini"]
    f13["requirements-dev.txt"]
    f14["setup.py"]
    f15["src/requests/status_codes.py"]
    f16["src/requests/__version__.py"]
    f17["ext/requests-logo.svg"]
    f18["src/requests/help.py"]
    f19["src/requests/packages.py"]
    f20["src/requests/api.py"]
    f21["src/requests/certs.py"]
    f22["NOTICE"]
    f23["MANIFEST.in"]
    f24["Makefile"]
    f1 --> f0
    f2 --> f0
    f2 --> f5
    f3 --> f15
    f3 --> f9
    f3 --> f7
    f3 --> f20
    f3 --> f16
    f3 --> f19
    f3 --> f4
    f4 --> f0
    f5 --> f0
    f6 --> f1
    f6 --> f4
    f6 --> f2
    f6 --> f0
    f6 --> f5
    f6 --> f16
    f6 --> f21
    f7 --> f6
    f7 --> f1
    f7 --> f15
    f7 --> f10
    f7 --> f4
    f7 --> f2
    f7 --> f0
    f7 --> f8
    f7 --> f5
    f8 --> f6
    f8 --> f2
    f8 --> f0
    f8 --> f5
    f9 --> f6
    f9 --> f1
    f9 --> f15
    f9 --> f7
    f9 --> f10
    f9 --> f4
    f9 --> f2
    f9 --> f0
    f9 --> f8
    f9 --> f11
    f9 --> f5
    f11 --> f6
    f11 --> f1
    f11 --> f7
    f11 --> f4
    f11 --> f2
    f11 --> f0
    f11 --> f8
    f15 --> f1
    f18 --> f16
    f19 --> f0
    f20 --> f9
```

## RANKED_FILES

| File | Score | Tier | Tokens |
|------|-------|------|--------|
| `src/requests/compat.py` | 0.508 | structured summary | 36 |
| `src/requests/structures.py` | 0.357 | structured summary | 103 |
| `src/requests/cookies.py` | 0.324 | structured summary | 183 |
| `src/requests/__init__.py` | 0.323 | structured summary | 85 |
| `src/requests/exceptions.py` | 0.293 | structured summary | 177 |
| `src/requests/_internal_utils.py` | 0.293 | structured summary | 79 |
| `src/requests/utils.py` | 0.265 | structured summary | 145 |
| `src/requests/models.py` | 0.232 | structured summary | 183 |
| `src/requests/auth.py` | 0.231 | structured summary | 170 |
| `tests/testserver/server.py` | 0.217 | one-liner | 26 |
| `src/requests/sessions.py` | 0.203 | structured summary | 171 |
| `src/requests/hooks.py` | 0.201 | structured summary | 55 |
| `src/requests/adapters.py` | 0.200 | structured summary | 168 |
| `tox.ini` | 0.200 | structured summary | 12 |
| `tests/test_utils.py` | 0.198 | one-liner | 25 |
| `tests/testserver/__init__.py` | 0.198 | one-liner | 15 |
| `tests/test_requests.py` | 0.196 | one-liner | 12 |
| `tests/test_structures.py` | 0.196 | one-liner | 22 |
| `tests/test_testserver.py` | 0.196 | one-liner | 21 |
| `tests/certs/valid/server/cert.cnf` | 0.195 | one-liner | 18 |
| `tests/certs/valid/server/server.csr` | 0.195 | one-liner | 17 |
| `tests/conftest.py` | 0.195 | one-liner | 21 |
| `tests/test_adapters.py` | 0.195 | one-liner | 21 |
| `tests/test_help.py` | 0.195 | one-liner | 24 |
| `tests/test_hooks.py` | 0.195 | one-liner | 20 |
| `tests/test_lowlevel.py` | 0.195 | one-liner | 21 |
| `tests/test_packages.py` | 0.195 | one-liner | 20 |
| `tests/certs/valid/server/Makefile` | 0.195 | one-liner | 17 |
| `tests/certs/mtls/client/cert.cnf` | 0.194 | one-liner | 19 |
| `tests/certs/mtls/client/client.csr` | 0.194 | one-liner | 18 |
| `tests/certs/mtls/README.md` | 0.193 | one-liner | 17 |
| `tests/certs/mtls/client/Makefile` | 0.193 | one-liner | 18 |
| `tests/certs/expired/server/cert.cnf` | 0.192 | one-liner | 18 |
| `tests/certs/expired/server/server.csr` | 0.192 | one-liner | 17 |
| `tests/certs/mtls/Makefile` | 0.192 | one-liner | 17 |
| `tests/certs/expired/ca/ca.cnf` | 0.191 | one-liner | 17 |
| `tests/certs/expired/ca/ca.srl` | 0.191 | one-liner | 17 |
| `tests/certs/expired/server/Makefile` | 0.191 | one-liner | 17 |
| `tests/certs/mtls/client/ca/ca.cnf` | 0.191 | one-liner | 19 |
| `tests/certs/mtls/client/ca/ca.srl` | 0.191 | one-liner | 19 |

## PERIPHERY

- `tests/testserver/server.py` — 2 classs, 1 function, 4 imports, 177 lines
- `tests/test_utils.py` — 12 classs, 23 functions, 18 imports, 988 lines
- `tests/testserver/__init__.py` — 0 lines
- `tests/test_requests.py` — Tests for Requests.
- `tests/test_structures.py` — 2 classs, 2 imports, 79 lines
- `tests/test_testserver.py` — 1 class, 6 imports, 166 lines
- `tests/certs/valid/server/cert.cnf` — 32 lines
- `tests/certs/valid/server/server.csr` — 20 lines
- `tests/conftest.py` — 4 functions, 8 imports, 59 lines
- `tests/test_adapters.py` — 1 function, 1 imports, 9 lines
- `tests/test_help.py` — 1 class, 3 functions, 2 imports, 28 lines
- `tests/test_hooks.py` — 3 functions, 2 imports, 23 lines
- `tests/test_lowlevel.py` — 14 functions, 6 imports, 429 lines
- `tests/test_packages.py` — 3 functions, 1 imports, 14 lines
- `tests/certs/valid/server/Makefile` — 17 lines
- `tests/certs/mtls/client/cert.cnf` — 27 lines
- `tests/certs/mtls/client/client.csr` — 25 lines
- `tests/certs/mtls/README.md` — 5 lines
- `tests/certs/mtls/client/Makefile` — 17 lines
- `tests/certs/expired/server/cert.cnf` — 25 lines
- `tests/certs/expired/server/server.csr` — 20 lines
- `tests/certs/mtls/Makefile` — 8 lines
- `tests/certs/expired/ca/ca.cnf` — 18 lines
- `tests/certs/expired/ca/ca.srl` — 2 lines
- `tests/certs/expired/server/Makefile` — 17 lines
- `tests/certs/mtls/client/ca/ca.cnf` — 18 lines
- `tests/certs/mtls/client/ca/ca.srl` — 2 lines
- `tests/certs/valid/ca/ca.cnf` — 18 lines
- `tests/certs/valid/ca/ca.srl` — 2 lines
- `tests/certs/expired/README.md` — 12 lines
- `tests/certs/expired/ca/Makefile` — 14 lines
- `tests/certs/mtls/client/ca/Makefile` — 14 lines
- `tests/certs/valid/ca/Makefile` — 14 lines
- `tests/certs/expired/Makefile` — 14 lines
- `tests/certs/README.md` — 11 lines
- `tests/__init__.py` — Requests test package initialisation.
- `tests/utils.py` — 1 function, 2 imports, 18 lines
- `tests/compat.py` — 1 function, 4 imports, 24 lines
- `requirements-dev.txt` — 8 lines
- `setup.py` — 2 imports, 10 lines
- `src/requests/status_codes.py` — r"""
- `src/requests/__version__.py` — 15 lines
- `ext/requests-logo.svg` — 1 lines
- `src/requests/help.py` — Module containing bug report helper(s).
- `docs/user/authentication.rst` — 156 lines
- `docs/user/install.rst` — 37 lines
- `docs/user/quickstart.rst` — 574 lines
- `docs/dev/contributing.rst` — 166 lines
- `docs/index.rst` — 141 lines
- `docs/make.bat` — 264 lines
- `docs/requirements.txt` — 4 lines
- `docs/user/advanced.rst` — 1139 lines
- `docs/community/out-there.rst` — 11 lines
- `docs/community/recommended.rst` — 63 lines
- `docs/community/release-process.rst` — 54 lines
- `docs/community/support.rst` — 32 lines
- `docs/community/updates.rst` — 19 lines
- `docs/community/vulnerabilities.rst` — 6 lines
- `docs/conf.py` — 3 imports, 387 lines
- `docs/dev/authors.rst` — 5 lines
- `docs/_themes/flask_theme_support.py` — 1 class, 2 imports, 87 lines
- `docs/api.rst` — 262 lines
- `docs/community/faq.rst` — 91 lines
- `docs/_templates/sidebarintro.html` — 38 lines
- `docs/_templates/sidebarlogo.html` — 31 lines
- `docs/_themes/.gitignore` — 4 lines
- `docs/_templates/hacks.html` — 81 lines
- `src/requests/packages.py` — 2 imports, 24 lines
- `src/requests/api.py` — 
- `src/requests/certs.py` — 
- `docs/Makefile` — 217 lines
- `docs/_static/custom.css` — 178 lines
- `NOTICE` — 3 lines
- `README.md` — 79 lines
- `docs/.nojekyll` — 2 lines
- `HISTORY.md` — 2013 lines
- `MANIFEST.in` — 4 lines
- `Makefile` — 28 lines
- `.gitignore` — 38 lines
- `.pre-commit-config.yaml` — 17 lines
- `.readthedocs.yaml` — 30 lines
- `AUTHORS.rst` — 196 lines
- `.coveragerc` — 3 lines
- `.git-blame-ignore-revs` — 6 lines

