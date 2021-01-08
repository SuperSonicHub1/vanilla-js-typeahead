# Vanilla JS Typeahead

A small example displaying typeahead through the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element and less than twenty lines of vanilla JavaScript.

```js
function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
}

const search_box = document.getElementById("search-bar")
const datalist = document.getElementById("autocomplete")

async function handleChange(e) {
    const query = e.target.value
    const res = await fetch(`/autocomplete?q=${encodeURIComponent(query)}`)
    body = await res.json()
    removeAllChildNodes(datalist)
    for (const {result, subtext} of body) {
        const option = new Option(subtext, result)
        datalist.appendChild(option)
    }
}

search_box.addEventListener('input', handleChange)
```

## What?
I know, right! This is pretty awesome! Simple and clean typeahead without the need for a library like [typeahead.js](https://twitter.github.io/typeahead.js/), as long as you don't need more than two text boxes or images.

The only downside I currently see is that updating the results can appear slow and/or glitchy at times.

Also, if you're wondering where I'm getting my autocomplete results from, they're from Google. I request and clean them up on the backend, and then send the results to the frontend.

## Installation
With [Poetry](https://python-poetry.org/) installed:
```bash
# Clone and cd
poetry install
python main.py
```