# JSONファイルを探索する

JSON形式のファイルはIR業務の中でよく見かける。例えば、ScivalAPIから取得した論文指標や論文情報を処理するためにはJSONファイルを扱う必要がある。しかしAPIで取得したJSONの階層数やキーの種類はAPIによって様々で、入れ子構造になっている。

こちらはScivalAPIから取得したJSONファイルを一部抜粋・加工したもの。
```
{ 'dataSource': {'sourceName': 'Scopus',
  'lastUpdated': '2099-02-08',
  'metricStartYear': 2000,
  'metricEndYear': 2999},
 'results': [{'metrics': [{'metricType': 'ScholarlyOutput', 'value': 1160},
    {'metricType': 'CitationCount', 'value': 20969},
    {'metricType': 'CitationsPerPublication', 'value': 18.076725},
    {'metricType': 'FieldWeightedCitationImpact', 'value': 1.2139008},
    {'metricType': 'OutputsInTopCitationPercentiles',
     'values': [{'threshold': 1, 'value': 29, 'percentage': 2.5},
      {'threshold': 5, 'value': 69, 'percentage': 5.9482756},
      {'threshold': 10, 'value': 107, 'percentage': 9.224137},
      {'threshold': 25, 'value': 282, 'percentage': 24.310345}]},
    {'metricType': 'PublicationsInTopJournalPercentiles',
     'impactType': 'CiteScore',
     'values': [{'threshold': 1, 'value': 28, 'percentage': 2.5547445},
      {'threshold': 5, 'value': 194, 'percentage': 17.70073},
      {'threshold': 10, 'value': 934, 'percentage': 85.21898},
      {'threshold': 25, 'value': 1075, 'percentage': 98.08395}]}],
   'institution': {'link': {'@ref': 'self',
     '@href': 'https:hogehoge',
     '@type': 'application/json'},
    'name': 'piyo University',
    'id': XXX,
    'uri': 'Institution/XXX',
    'country': 'hoge',
    'countryCode': 'hoge'}}]}
```

このファイルから`'ScholarlyOutput'`の`'value':1160`を取得したい。

地道にパースして取得することも可能だが、後から見て何が何だかわからん。

```python
jsonfilename["results"][0]["metrics"][0]["value"] # どこの何というデータ??
```

そこで、「JSONファイルのどこをどのように探したのか」というプロセスが明確なJSON探索パッケージを作った。<br>
※アルゴリズムそのものは先人の知恵。ちょっと汎用化しただけ。

## 使用方法

クラス`JSONKeySearch`からインスタンスを作成する。インスタンス変数`jsonObject`には解析したいJSONファイルを渡す。

```python
instance = JSONKeySearch(jsonObject=jsonfilename)
```

解析対象となるキー、値をインスタンスメソッド`search`に渡す。
```python
instance.search(key=keyhoge,value=valuepiyo)
```

`keyhoge`に探索したいキーを渡し、`valuepiyo`にキーの値を指定する。<br>
`valuepiyo`を`""`に設定すれば`keyhoge`を含む全ての値を返す。<br>
`search`処理結果は返り値および`instance.jsonObject`に格納される。

## 例
上記したJSONのうち、`ScholaryOutput`を含む要素のみ取得したい場合

```python
target = JSONKeySearch(jsonObject=jsonfilename)
target.search(key="metricType", value="ScholarlyOutput"})
print(target.jsonObject)

# 出力結果
# [{'metricType': 'ScholarlyOutput', 'value': 1160}]
```
`value`を含む要素を全て取得したい場合
```python
target = JSONKeySearch(jsonObject=jsonfilename)
target.search(key="value", value="")
print(target.jsonObject)

# 出力結果
# [{'metricType': 'ScholarlyOutput', 'value': 1160},
#  {'metricType': 'CitationCount', 'value': 20969},
#  {'metricType': 'CitationsPerPublication', 'value': 18.076725},
#  {'metricType': 'FieldWeightedCitationImpact', 'value': 1.2139008},
#  {'threshold': 1, 'value': 29, 'percentage': 2.5},
#  {'threshold': 5, 'value': 69, 'percentage': 5.9482756},
#  {'threshold': 10, 'value': 107, 'percentage': 9.224137},
#  {'threshold': 25, 'value': 282, 'percentage': 24.310345},
#  {'threshold': 1, 'value': 28, 'percentage': 2.5547445},
#  {'threshold': 5, 'value': 194, 'percentage': 17.70073},
#  {'threshold': 10, 'value': 934, 'percentage': 85.21898},
#  {'threshold': 25, 'value': 1075, 'percentage': 98.08395}]
```
なお`JSONKeySearch`のメソッド`find_key`をオーバーライドした子クラスを定義すれば、より複雑な条件で探索が可能になる。<br>
`JSONKeySearchWithASJCmetricsFilters`はその一例。ASJCごとの論文指標を取得するために入れ子を操作している。

## 参考文献

以下で紹介されているJSON探索再帰処理を使用している。Special Thanks!!!<br>
https://jumpyoshim.hatenablog.com/entry/four-steps-to-get-specific-data-from-complex-json
