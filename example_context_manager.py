import asyncio
import aiomysql


class DatabaseConnection:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.connection = None

    async def __aenter__(self):
        # We can wait while connection is being established
        self.connection = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        return self.connection

    async def __aexit__(self, exc_type, exc_value, traceback):
        # We can wait while connection is being closed
        if self.connection:
            self.connection.close()
            await self.connection.wait_closed()


async def main():

    async with DatabaseConnection(
        host='localhost',
        port=3306,
        user='user',
        password='pwd',
        db='db'
    ) as connection:
        async with connection.cursor() as cursor:
            # Async query
            await cursor.execute("SELECT * FROM table")
            result = await cursor.fetchall()
            print(result)


asyncio.run(main())
