# jsonkeysearch
## Description
`jsonkeysearch` is a Python library that recursively searches for keys in JSON format files.

## Installaction

```
pip install jsonkeysearch
```

## Usage

```python
from jsonkeysearch import JSONKeySearch

# https://json.org/example.html
json_example = {
    "menu": {
        "id": "file",
        "value": "File",
        "popup": {
            "menuitem": [
                {"value": "New", "onclick": "CreateNewDoc()"},
                {"value": "Open", "onclick": "OpenDoc()"},
                {"value": "Close", "onclick": "CloseDoc()"},
            ]
        },
    }
}


target = JSONKeySearch(json_example)

# [1] Append all dictionary with onclick as key in a list
key_ = "onclick"
value_ = "" # All value in key
target.search(key=key_, value=value_)

print(target.jsonObject)
# [
#     {"value": "New", "onclick": "CreateNewDoc()"},
#     {"value": "Open", "onclick": "OpenDoc()"},
#     {"value": "Close", "onclick": "CloseDoc()"},
# ]

# [2] Append dictionary in a list with onclick as key and 'Open' as value
key_="onclick"
value_ = "Open"
target.search(key = key_, value = value_)

print(target.jsonObject)
# [{"value": "Open", "onclick": "OpenDoc()"}]

for dict_ in target.jsonObject:
    print(dict_[key_])
# 'OpenDoc()'
```