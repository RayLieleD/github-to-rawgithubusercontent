# your link goes here
link = "https://github.com/monosans/proxy-list/blob/main/proxies_anonymous/socks5.txt"
link2 = "https://github.com/monosans/proxy-list/blob/main/proxies_anonymous/socks4.txt"
link3 = "https://github.com/monosans/proxy-list/blob/main/proxies_anonymous/http.txt"
link4 = "https://github.com/monosans/proxy-list/blob/main/proxies/socks5.txt"
link5 = "https://github.com/monosans/proxy-list/blob/main/proxies/socks4.txt"
link6 = "https://github.com/monosans/proxy-list/blob/main/proxies/http.txt"


# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
print(link2.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
print(link3.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
print(link4.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
print(link5.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))
print(link6.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))



f = open('proxytotest.txt','w')
f.write(link + '\n' + link2 + '\n' + link3 + '\n' + link4 + '\n' + link5 + '\n' + link6 + '\n' )
f.close()

# example output link:
# https://raw.githubusercontent.com/knightlab-analyses/qurro-mackerel-analysis/master/AnalysisOutput/qurro-plot.qzv