import subprocess

def install_libraries():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Libraries installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing libraries.")

if __name__ == "__main__":
    install_libraries()
