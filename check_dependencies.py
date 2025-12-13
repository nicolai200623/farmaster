#!/usr/bin/env python3
"""
Dependency Checker for FarmAster Bot
Kiểm tra và cài đặt các packages cần thiết
"""
import sys
import subprocess

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name.replace('-', '_')

    try:
        __import__(import_name)
        return True
    except ImportError:
        return False

def install_package(package_spec):
    """Install a package using pip"""
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', package_spec
        ])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("=" * 70)
    print("🔍 FARMASTER BOT - DEPENDENCY CHECKER")
    print("=" * 70)
    print()

    # Required packages with their import names
    packages = [
        ('python-binance', 'binance', 'python-binance==1.0.19'),
        ('pandas', 'pandas', 'pandas>=2.0.0'),
        ('numpy', 'numpy', 'numpy>=1.24.0'),
        ('python-dotenv', 'dotenv', 'python-dotenv>=1.0.0'),
        ('python-telegram-bot', 'telegram', 'python-telegram-bot>=20.0'),
        ('requests', 'requests', 'requests>=2.31.0'),
        ('scikit-learn', 'sklearn', 'scikit-learn>=1.3.0'),
        ('xgboost', 'xgboost', 'xgboost>=2.0.0'),
        ('lightgbm', 'lightgbm', 'lightgbm>=4.0.0'),
        ('catboost', 'catboost', 'catboost>=1.2.0'),
        ('aiohttp', 'aiohttp', 'aiohttp>=3.9.0'),
        ('joblib', 'joblib', 'joblib>=1.3.0'),
    ]

    missing_packages = []
    installed_packages = []

    print("Checking required packages...\n")

    for pkg_name, import_name, pkg_spec in packages:
        if check_package(pkg_name, import_name):
            print(f"✅ {pkg_name}")
            installed_packages.append(pkg_name)
        else:
            print(f"❌ {pkg_name} - NOT INSTALLED")
            missing_packages.append((pkg_name, pkg_spec))

    print()
    print(f"📊 Summary: {len(installed_packages)}/{len(packages)} packages installed")
    print()

    if missing_packages:
        print("⚠️  Missing packages detected!")
        print()
        print("You can install missing packages in 2 ways:")
        print()
        print("Option 1 - Install all from requirements:")
        print("  pip install -r requirements-vps.txt")
        print()
        print("Option 2 - Install individually:")
        for pkg_name, pkg_spec in missing_packages:
            print(f"  pip install {pkg_spec}")
        print()

        # Ask if user wants to auto-install
        try:
            response = input("Do you want to auto-install missing packages now? (y/n): ")
            if response.lower() == 'y':
                print()
                print("Installing missing packages...")
                print()

                for pkg_name, pkg_spec in missing_packages:
                    print(f"Installing {pkg_name}...")
                    if install_package(pkg_spec):
                        print(f"✅ {pkg_name} installed successfully")
                    else:
                        print(f"❌ Failed to install {pkg_name}")

                print()
                print("✅ Installation complete!")
                print()
                print("Run this script again to verify all packages are installed.")
        except KeyboardInterrupt:
            print("\n\nInstallation cancelled.")
            sys.exit(1)
    else:
        print("✅ All required packages are installed!")
        print()
        print("You can now run the bot:")
        print("  python bot.py")
        print()
        print("Or use the VPS helper:")
        print("  python run_vps.py")

    print("=" * 70)

if __name__ == '__main__':
    main()
