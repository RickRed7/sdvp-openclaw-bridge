from core.app import VaultApp
import asyncio

if __name__ == "__main__":
    app = VaultApp()
    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        print("\n[SYSTEM] VaultLink OS Shutting Down...")
