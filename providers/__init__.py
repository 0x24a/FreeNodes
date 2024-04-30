from providers.chromego import fetch as chromego
from providers.freefq import fetch as freefq
from providers.pawdroid import fetch as pawdroid

PROVIDERS={
    "ChromeGo": chromego,
    "freefq": freefq,
    "Pawdroid/Free-servers": pawdroid
}