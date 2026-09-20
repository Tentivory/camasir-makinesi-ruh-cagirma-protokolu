#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çamaşır Makinesi Ruh Çağırma Protokolü v1.0
Bu yazılım kayıp çorapların ruhlarıyla diplomatik ilişki kurar.
"""

import random
import time
import base64

RUH_CEVAPLARI = [
    "Sol çorap şu an tamburun 3. boyutuyla görüşmede.",
    "Çiftler ancak ayın 32. günü yeniden birleşir.",
    "Makine ruhu çay molasında. Lütfen 47 dakika bekleyiniz.",
    "Kayıp çorap vatandaşlık başvurusu yapmıştır. Dosya no: ÇRP-404.",
    "Ruhu çağırdınız ama o sizi çağırmadı. Ters protokol.",
    "Bu yıkama döngüsünde demokrasi de kayboldu, çorap da.",
]

# gizli not (sadece meraklılar için):
# hidden: c2l5YXNpIGFubGFtIHlvayBiaXIga2F5xLFuLCB1eWd1bGFtYXogZG9zeWFzxLFuZGEga2F5Ym9sZHUu
# decode ederseniz bürokrasi şakası çıkar, parti afişi değil.

def ruh_cagir(soru: str) -> str:
    print("\n[PROTOKOL] Tambur kapağı mühürleniyor...")
    time.sleep(0.8)
    print("[PROTOKOL] Santrifüj frekansı ayarlanıyor...")
    time.sleep(0.8)
    print(f"[SORU] {soru}")
    cevap = random.choice(RUH_CEVAPLARI)
    return f"[RUH] {cevap}"


def main():
    print("=== ÇAMAŞIR MAKİNESİ RUH ÇAĞIRMA PROTOKOLÜ ===")
    print("Kayyum onaylı sürüm. Su kaçması halinde sorumluluk kabul edilmez.\n")
    soru = input("Makine ruhuna sorunuzu yazın (boş bırakırsanız varsayılan çorap sorusu gider): ").strip()
    if not soru:
        soru = "Kayıp çoraplarım nerede?"
    print(ruh_cagir(soru))
    print("\n--- protokol sonu ---")
    print("Damga: Tentivory / Kayyum Grok / 20 Eylül 2026")


if __name__ == "__main__":
    main()
