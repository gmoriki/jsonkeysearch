from dataclasses import dataclass, field


@dataclass
class JSONKeySearch:
    """
    JSONを明示的に探索するクラス

    Parameters
    -------
    jsonObject
        処理対象のJSONファイル -> searchを経てダウンサイズされる
    _json_element
        jsonObjectを処理する要素単位

    """

    jsonObject: dict = field(default_factory=dict)
    _json_element: object = ""

    def search(self, key="", value=""):
        """
        再帰関数:指定したkeyとvalueをもとにJSONファイルを探索する

        Parameters
        ----------
        key : str, optional
            探索対象の辞書キー, by default ""
        value : str, optional
            探索対象の辞書値, by default ""

        Returns
        -------
        res
            リストに格納された辞書形式
        """
        res = []
        if self.find_key(self.jsonObject, key, value):
            res.append(self.jsonObject)

        elif isinstance(self.jsonObject, list):
            for self._json_element in self.jsonObject:
                self.jsonObject = self._json_element
                res += self.search(key, value)
        elif isinstance(self.jsonObject, dict):
            for self._json_element in self.jsonObject.values():
                self.jsonObject = self._json_element
                res += self.search(key, value)

        self.jsonObject = res
        return res

    def find_key(self, arg, key, value):
        """
        JSONファイルを絞り込む条件を指定する
        条件を変更する場合はfind_keyをオーバーライドすること

        Parameters
        ----------
        arg : dict
            searchから渡されたself.jsonObject
        key : str
            探索対象の辞書キー
        value : str
            探索対象の辞書値

        Returns
        -------
        bool
            searchの返り値としてappendするか否かを決定する条件式
        """
        if isinstance(arg, dict) and key in arg.keys():

            if not value:
                return True
            else:
                return str(value) in str(arg[key])


# find_keyをオーバーライドする例
# ASJC分野別論文指標を取得するための子クラス
class JSONKeySearchWithASJCmetricsFilters(JSONKeySearch):
    def find_key(self, arg, key, value):
        # 特定のmetricTypeの時はvaluesの中にmetricType名を入れる
        for sp_metric in ["OutputsInTopCitationPercentiles", "PublicationsInTopJournalPercentiles"]:
            if isinstance(arg, dict) and ("values" in arg.keys()) and (sp_metric in arg.values()):
                for dict_ in arg["values"]:
                    dict_["metricType"] = sp_metric

        # thresholdの指定条件（Output...のみ=1も含めて処理）
        if isinstance(arg, dict) and "threshold" in arg.keys():
            return (arg["threshold"] == 10) or (
                arg["threshold"] == 1 and "OutputsInTopCitationPercentiles" in arg.values()
            )
        # valueを含む辞書を取得する条件
        elif isinstance(arg, dict):
            return "value" in arg.keys()
