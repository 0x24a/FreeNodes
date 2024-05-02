from providers.template_b64sub import make_function
def fetch():
    return ("\n".join(make_function("https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt")()).split("\n\n")[1]).split("\n")