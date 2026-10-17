"""各腳本共用的 HTTP 請求與重試。

Semantic Scholar 未登入時共用限額，常連續回 429；arXiv、HF API 偶爾讀取逾時。
各腳本原本各寫一套重試，曾漏接逾時而整批中斷，所以集中在這裡。
"""
import json
import time
import urllib.error
import urllib.request

UA = {"User-Agent": "robot-nav-survey/1.0 (https://github.com/chenyuting3077/robot-nav-survey)"}


def fetch(url: str, data: bytes | None = None, headers: dict | None = None, tries: int = 15) -> bytes:
    """429、5xx、逾時、斷線時退避重試（上限 60 秒）；其他 4xx 直接拋出。"""
    req = urllib.request.Request(url, data=data, headers={**UA, **(headers or {})})
    for i in range(tries):
        try:
            return urllib.request.urlopen(req, timeout=60).read()
        except urllib.error.HTTPError as e:
            if (e.code != 429 and e.code < 500) or i == tries - 1:
                raise
        except (TimeoutError, urllib.error.URLError):
            if i == tries - 1:
                raise
        time.sleep(min(2 ** i, 60))
    raise RuntimeError("unreachable")


def fetch_json(url: str, data: bytes | None = None, headers: dict | None = None, tries: int = 15):
    return json.loads(fetch(url, data, headers, tries))
