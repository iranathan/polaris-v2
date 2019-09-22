import aiohttp
import random


class Roblox:
    def __init__(self):
        self.requests = aiohttp.ClientSession()
        # credit to Neztore#6998 for these words:
        self.words = [
            "weather", "hello", "roblox", "favorite", "eating", "chocolate", "cheese", "tasty", "help", "general",
            "know", "baby", "dolly",
            "graphics", "super", "intense", "disruption", "beautiful", "happy", "angry", "excited", "hard", "soft",
            "puppy", "dogs", "cats", "meow", "woof", "like", "enjoyable", "hamster", "tiger", "bear", "guinea", "pig",
            "aardletk", "sea", "lion", "chinchilla",
            "otter", "goat", "skunk", "armadillo", "oats", "beans", "tomato", "onions", "oranges"
        ]

    async def is_user(self, roblox_id: int) -> bool:
        r = await self.requests.get(f'https://api.roblox.com/users/{roblox_id}')
        return r.status == 200

    async def is_user_username(self, username: str) -> bool:
        r = await self.requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')
        return r.status == 200

    async def id_by_username(self, username: str) -> int:
        r = await self.requests.get(f'https://api.roblox.com/users/get-by-username?username={username}')
        json = await r.json()
        return json.get('Id')

    async def status(self, roblox_id: int) -> str:
        r = await self.requests.get(f'https://www.roblox.com/users/profile/profileheader-json?userId={roblox_id}')
        json = await r.json()
        return json.get('UserStatus')

    async def code(self) -> str:
        code = ''
        for i in list(range(0, 5)):
            code += random.choice(self.words)
            if i != 4:
                code += ' '
        return code
