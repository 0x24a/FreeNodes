from providers import PROVIDERS
from base64 import b64encode

print("Fetching proxies from", len(PROVIDERS.keys()), "providers")

proxies = []

for provider_name, fetch in PROVIDERS.items():
    print("- Fetching proxies from", provider_name)
    try:
        result = fetch()
        proxies += result
        print("- - Got", len(result), "proxies")
    except:
        print("- - Failed, ignoring.")
print(" - Merging nodes")
number_before = len(proxies)
print(" - Removing repeated proxies")
proxies=list(set(proxies))
print(f" - Number: {number_before} -> {len(proxies)}")
result = b64encode(("\n".join(proxies)).encode("utf-8")).decode()
protocols={}
for proxy in proxies:
    protocol=proxy.split("://",1)[0]
    if protocol in protocols.keys():
        protocols[protocol].append(proxy)
    else:
        protocols[protocol]=[proxy]
print(" - Writing...")
print(" - - Main sub")
with open("subs/main.txt", "w+") as f:
    f.write(result)
for protocol in protocols.items():
    if not protocol[0] or len(protocol[0]) > 24:
        continue
    print(f" - - {protocol[0].upper()}")
    result = b64encode(("\n".join(protocol[1])).encode("utf-8")).decode()
    with open(f"subs/{protocol[0].lower()}.txt", "w+") as f:
        f.write(result)
print("Done!")
