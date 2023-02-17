from dataclasses import dataclass, field


@dataclass
class JSONKeySearch:

    jsonObject: dict = field(default_factory=dict)
    _json_element: object = ""

    def search(self, key="", value=""):
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
        if isinstance(arg, dict) and key in arg.keys():

            if not value:
                return True
            else:
                return str(value) in str(arg[key])


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
