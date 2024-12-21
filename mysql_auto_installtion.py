import os
import subprocess

def is_mysql_installed():
    try:
        # Check if MySQL is installed
        result = subprocess.run(['mysql', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("MySQL is already installed.")
            print(result.stdout.strip())
            return True
        else:
            print("MySQL is not installed.")
            return False
    except FileNotFoundError:
        print("MySQL command not found.")
        return False


def install_mysql():
    try:
        print("Updating package lists...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

        print("Installing MySQL server...")
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'mysql-server'], check=True)

        print("MySQL installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")


if __name__ == "__main__":
    if not is_mysql_installed():
        install_mysql()
