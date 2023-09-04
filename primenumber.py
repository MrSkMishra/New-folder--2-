def extract_domain_name(url):
    
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    
    if url.startswith("www."):
        url = url[4:]
        
    slash_index = url.find("/")
    if slash_index != -1:
        url = url[:slash_index]
        
    return url

url = "https://github.com/settings/profile"
domain_name = extract_domain_name(url)
print(domain_name)  