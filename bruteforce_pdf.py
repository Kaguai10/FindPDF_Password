# 🛠️ PDF Bruteforce Tool

import os
import argparse
from pypdf import PdfReader

def brute_force_pdf(pdf_path, wordlist_path):
    if not os.path.exists(pdf_path):
        print(f"[!] File PDF tidak ditemukan: {pdf_path}")
        return None

    if not os.path.exists(wordlist_path):
        print(f"[!] Wordlist tidak ditemukan: {wordlist_path}")
        return None

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        passwords = [line.strip() for line in file if line.strip()]

    print(f"[*] Mulai brute force pada: {pdf_path}")
    print(f"[*] Total kandidat password: {len(passwords)}\n")

    for idx, password in enumerate(passwords, 1):
        try:
            reader = PdfReader(pdf_path)
            result = reader.decrypt(password)
            status = "Berhasil" if result else "Gagal"
            print(f"[{idx}/{len(passwords)}] Coba: '{password}' => {status}")

            if result:
                print(f"\n[✅] Password ditemukan: '{password}'")
                return password
        except Exception as e:
            print(f"[!] Error saat mencoba '{password}': {e}")

    print("\n[✖] Password tidak ditemukan di wordlist.")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Bruteforce Tool - Cari password PDF terenkripsi dengan wordlist")
    parser.add_argument("-f", "--file", required=True, help="Path ke file PDF terenkripsi")
    parser.add_argument("-w", "--wordlist", required=True, help="Path ke file wordlist")

    args = parser.parse_args()

    print("============================")
    print("     PDF Bruteforce Tool    ")
    print("============================\n")

    brute_force_pdf(args.file, args.wordlist)
          
