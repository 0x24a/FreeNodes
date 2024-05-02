from providers.chromego import fetch as chromego
from providers.freefq import fetch as freefq
from providers.pawdroid import fetch as pawdroid
from providers.free18 import fetch as free18
from providers.aiboboxx import fetch as aiboboxx
from providers.hkpc import fetch as hkpc

PROVIDERS={
    "ChromeGo": chromego,
    "freefq": freefq,
    "Pawdroid/Free-servers": pawdroid,
    "free18/v2ray": free18,
    "aiboboxx": aiboboxx,
    "hkpc/V2ray-Configs": hkpc
}