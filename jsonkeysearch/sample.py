from jsonkeysearch import JSONKeySearch

# jsonのサンプル https://json.org/example.html
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


# 人力マイニング...あらかじめ全てのキーの把握が必須/特定のjsonに限った運用
# [1] onclickをキーに持つ全ての辞書データ
print(json_example["menu"]["popup"]["menuitem"])
# [
#     {"value": "New", "onclick": "CreateNewDoc()"},
#     {"value": "Open", "onclick": "OpenDoc()"},
#     {"value": "Close", "onclick": "CloseDoc()"},
# ]

# [2] onclickをキーに持ち、値に'Open'を含む辞書データ
for dict_ in json_example["menu"]["popup"]["menuitem"]:
    if "Open" in dict_["onclick"]:
        print(dict_["onclick"])
# 'OpenDoc()'


# JSONKeySearchを使用...必要なキーが分かれば探索可/汎用的にjson探索可
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
target.search(key=key_, value=value_)

# 結果の出力
print(target.jsonObject)
# [{"value": "Open", "onclick": "OpenDoc()"}]

# 値の取得
for dict_ in target.jsonObject:
    print(dict_[key_])
# 'OpenDoc()'
