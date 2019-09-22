import psycopg2


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", database="roblox", user="ira", password='iranathan')
        self.cursor = self.connection.cursor()

    def add_user(self, discord_id: int, roblox_id: int, roblox_username: int) -> bool:
        self.cursor.execute(f"""
            INSERT INTO robloxplayer (discord_id, roblox_id, roblox_username)
            VALUES ({discord_id}, {roblox_id}, '{roblox_username}');
        """)
        self.connection.commit()
        return True