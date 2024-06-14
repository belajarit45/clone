import subprocess
import urllib.request
import getpass

def main():
    while True:
        token = getpass.getpass("Masukkan token: ")
        if token == "andrian123":
            # Unduh skrip Bash
            script_url = "https://raw.githubuserconte>
            try:
                with urllib.request.urlopen(script_ur>
                    bash_script = response.read().dec>
                    # Jalankan skrip Bash
                    subprocess.run(["bash", "-c", bas>
            except Exception as e:
                print("Gagal mengunduh atau menjalank>
            break  # Keluar dari perulangan jika toke>
        else:
            print("Token salah. Silakan coba lagi.")

if __name__ == "__main__":
    main()
