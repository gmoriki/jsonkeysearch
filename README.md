# jsonkeysearch
## Description
`jsonkeysearch`はJSON形式のファイルからキーを再帰的に探索するPythonライブラリです。

## Installaction

<!-- ```pip install jsokeysearch``` -->

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

# [1] onclickをキーに持つ全ての辞書データをリストに格納
key_, value_ = "onclick", ""
target.search(key=key_, value=value_)

# 結果の出力
print(target.jsonObject)
# [
#     {"value": "New", "onclick": "CreateNewDoc()"},
#     {"value": "Open", "onclick": "OpenDoc()"},
#     {"value": "Close", "onclick": "CloseDoc()"},
# ]

# [2] onclickをキーに持ち、値に'Open'を含む辞書データをリストに格納
key_, value_ = "onclick", "Open"
target.search(key = key_, value = value_)

# 結果の出力
print(target.jsonObject)
# [{"value": "Open", "onclick": "OpenDoc()"}]

# 値の取得
for dict_ in target.jsonObject:
    print(dict_[key_])
# 'OpenDoc()'

```