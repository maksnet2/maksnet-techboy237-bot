from LaylaRobot.sample_config import Config

class Development(Config):
    OWNER_ID = 842014037  # your telegram ID
    OWNER_USERNAME = "techboy237"  # your telegram username
    API_KEY = "12842387"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://hokildxgyyuvto:79985361846d84d1a2933a21b656d82235ad7a3b2257c12d88abec247df4b4cc@ec2-44-194-4-127.compute-1.amazonaws.com:5432/d1ifco5uefbqfa'  # sample db credentials
    MESSAGE_DUMP = '-289867106' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [842014037]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
