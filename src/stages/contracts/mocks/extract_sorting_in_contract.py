# pylint: disable=line-too-long
from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content=[
    ["仓库", "包裹号", "订单号", "发货模式", "推荐库区", "推荐巷道", "操作人", "操作时间"],
    ["巴西瓜卢流斯发货仓二", "GC2308142624096260", "GSHNRC6440002NX", "合单发货", "7", "40", "SPglp2WH176", "2023-08-15 07:59:59"],
    ["巴西瓜卢流斯发货仓二", "GC2308105267422209", "GSHNR124S00NGLX", "合单发货", "12", "71", "SPglp2WH155", "2023-08-15 07:59:59"],
    ["巴西瓜卢流斯发货仓二", "GC2308121317896195", "GSHNRU35U000480", "合单发货", "13", "73", "SPglp2WH1105", "2023-08-15 07:59:58"],
    ["巴西瓜卢流斯发货仓二", "GC2308090885467140", "GSHNRN17100MXAA", "合单发货", "9", "53", "SPglp2WH163", "2023-08-15 07:59:58"],
    ["巴西瓜卢流斯发货仓二", "GC2308140523666434", "GSHNRW42000NQ3M", "合单发货", "6", "31", "SPglp2WH171", "2023-08-15 07:59:57"]
],
)
