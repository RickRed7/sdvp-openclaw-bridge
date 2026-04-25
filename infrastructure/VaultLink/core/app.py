import asyncio
from services.asset_service import AssetService
from ui.terminal_ui import TerminalUI

class VaultApp:
    def __init__(self):
        self.running = True
        self.assets = AssetService()
        self.ui = TerminalUI(self)

    async def run(self):
        print("[SYSTEM] VaultLink OS Initialized.")
        while self.running:
            await self.ui.render()
            await self.handle_input()

    async def handle_input(self):
        # Optimized for non-blocking terminal input
        loop = asyncio.get_event_loop()
        cmd = await loop.run_in_executor(None, input, "VaultLink> ")
        if cmd == "exit": self.running = False
        elif cmd == "list": print(self.assets.get_assets())
