from motor.motor_asyncio import AsyncIOMotorClient

USERNAME = 'shahrosekhan1362'
PASSEORD = '6Szs8M847vxWrx6p'
# MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_SERVER = 'mongodb+srv://shahrosekhan1362:6Szs8M847vxWrx6p@dbserver.2etzm1e.mongodb.net/?retryWrites=true&w=majority&appName=DBServer'

client = AsyncIOMotorClient(MONGO_SERVER)
database = client["teapot"]

def get_database():
    return database
