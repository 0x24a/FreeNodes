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

result = b64encode(("\n".join(proxies)).encode("utf-8")).decode()
with open("sub.txt", "w+") as f:
    f.write(result)
print("Done!")
