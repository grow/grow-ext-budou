# grow-ext-budou

[![Build Status](https://travis-ci.org/grow/grow-ext-budou.svg?branch=master)](https://travis-ci.org/grow/grow-ext-budou)

Budou extension for Grow.

## Concept

Installs a filter into the Jinja2 environment that uses the Google Cloud
Natural Language API to analyze text and insert `<span>` tags into HTML for
intelligent word wrapping. The filter only activates when a page is being
rendered in a supported language. Supported language identifiers:

- ja
- ko
- zh
- zh_Hans
- zh_Hant

For more information on Budou, see the
[`google/budou`](https://github.com/google/budou) repository.

![](https://raw.githubusercontent.com/wiki/google/budou/images/nexus_example.jpeg)

_NOTE:_ Budou requires authentication to the Google Cloud Natural Language API.
You will have to authorize Grow to access this API, or use a service account on
a Google Cloud project where the API is enabled. 

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/grow/grow-ext-budou`
1. Ensure `.gitignore` contains `extensions`.
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```
extensions:
  jinja2:
  - extensions.budou_ext.BudouExtension
```

### In templates

```
# Append the budou filter.
{{_("I will eat rice at Roppongi Hills.")|budou}}

# Outputs the following HTML.
<span class="ww">六本木</span><span class="ww">ヒルズに</span><span
class="ww">います。</span>
```

### In CSS

Budou works by wrapping elements that should not be wrapped in a
`<span class="ww">` element. Add the following CSS to prevent these
elements from wrapping.

```
.wordwrap {
  display: inline-block;
}
```
