def embedfix(message: str) -> str:
    res = message
    if "https://x.com/" in res:
        res = res.replace("https://x.com/", "https://fxtwitter.com/")
    if "https://twitter.com/" in res:
        res = res.replace("https://twitter.com/", "https://fxtwitter.com/")
    return res
