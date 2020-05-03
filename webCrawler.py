#偽裝成一般使用者才不會被擋
import urllib.request as req


url="https://www.ptt.cc/bbs/LoL/index.html"

#偽裝一般使用者
request=req.Request(url , headers ={
  "user-agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
})

with req.urlopen(request) as res: 
  data=res.read().decode("utf-8")

