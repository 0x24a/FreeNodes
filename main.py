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
print(" - Writing...")
with open("sub.txt", "w+") as f:
    f.write(result)
print("Done!")
