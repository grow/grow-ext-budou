# grow-ext-budou

Budou extension for Grow.

## Concept

Installs a filter into the Jinja2 environment that uses the Google Cloud
Natural language API to analyze text and insert `<span>` tags into HTML for
intelligent word-wrapping. For more information on Budou, see the
[`google/budou`](https://github.com/google/budou) repository.

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-budo`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
extensions:
  jinja2:
  - extensions.budou_ext.BudouExtension
```

1. Use the filter in templates:

```
<h1>{{_("Title Text"|budou)}}</h1>
```
