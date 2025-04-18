#!/usr/bin/python3
# /src/utils/url.py



# Url
class Url:
  def __init__(self, url:str):
    self.url = url.strip().strip("/").lower()

  @staticmethod
  def join(*paths:str):
    segments = [*paths]
    out = []
    for p in paths:
        clean = p.strip().lower().strip('/')
        if clean:
            out.append(clean)
    return "/".join(out)


# test
if __name__ == "__main__":
  url = Url("almdrasa.com")
  print(url)
  print(url.join(url.url, "about_us"))



  # success
