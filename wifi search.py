from scapy.all import Dot11Beacon , Dot11Elt , Dot11 , sniff

ağlar = set()

def paket_yakala(paket):
    if paket.haslayer(Dot11Beacon):
        ssid = paket[Dot11Elt].info.decode(errors="ignore")
        bssid = paket[Dot11].addr2
        if ssid not in ağlar:
            print(f"SSID: {ssid}, BSSID: {bssid}")
            ağlar.add(ssid)

# wlan0mon: monitor mode'da olan arayüz ismi
sniff(iface="wlan0", prn=paket_yakala, timeout=30)
