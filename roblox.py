import aiohttp


class Roblox:
    def __init__(self):
        self.requests = aiohttp.ClientSession()

    async def is_user(self, roblox_id: int) -> bool:
        r = await self.requests.get(f'https://api.roblox.com/users/{roblox_id}')
        return r.status == 200

    async def is_user_username(self, username: str) -> int:
        r = await self.requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')
        return r.status == 200


