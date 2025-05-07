import os
import shutil
import ctypes
import subprocess
import psutil
import time

def clear_temp():
    print("🧹 Geçici dosyalar siliniyor...")
    temp_folders = [os.environ.get('TEMP'), os.environ.get('TMP')]
    for folder in temp_folders:
        if folder and os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                os.makedirs(folder)
                print(f"✅ {folder} temizlendi.")
            except Exception as e:
                print(f"⚠️ {folder} silinemedi: {e}")
    print("✅ Tüm geçici dosyalar temizlendi.\n")

def clear_prefetch():
    print("🧹 Prefetch dosyaları siliniyor...")
    try:
        subprocess.call('del /Q /F C:\\Windows\\Prefetch\\*', shell=True)
        print("✅ Prefetch dosyaları temizlendi.\n")
    except Exception as e:
        print(f"⚠️ Prefetch temizlenemedi: {e}\n")

def clear_ram():
    print("🧠 RAM temizleniyor...")
    try:
        # RAM’i boşaltma denemesi (gereken uygulamaları kapatır)
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            if proc.info['memory_info'].rss > 100 * 1024 * 1024:  # 100 MB üstü
                try:
                    proc.terminate()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        print("✅ RAM mümkün olduğunca temizlendi.\n")
    except Exception as e:
        print(f"⚠️ RAM temizlenemedi: {e}\n")

def disable_startup_apps():
    print("🚫 Başlangıçta çalışan uygulamalar:")
    try:
        result = subprocess.check_output("wmic startup get caption,command", shell=True)
        print(result.decode())
        print("⚠️ Not: Programları devre dışı bırakmak için elle müdahale gerekebilir.")
    except Exception as e:
        print(f"⚠️ Başlangıç uygulamaları listelenemedi: {e}")

def main():
    print("🚀 PC Optimizasyon Botu Başlıyor...")
    time.sleep(1)

    clear_temp()
    clear_prefetch()
    clear_ram()
    disable_startup_apps()

    print("\n✅ Temizlik tamamlandı! Bilgisayarın biraz daha rahatladı 😎")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        print("⚠️ Yönetici olarak çalıştırman gerekiyor! (Sağ tık > Yönetici olarak çalıştır)")
