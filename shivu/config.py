class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6982003688"
    sudo_users = "5512261555", "6982003688"
    GROUP_ID = -1002086069788
    TOKEN = "7125549226:AAGufzEcBEhoHbcPo-x93ulDF8y6lQ6CjFY"
    mongo_url = "mongodb://mongo:cpmRievpABDRrCVtXfXSSMDSOKcdCkpl@roundhouse.proxy.rlwy.net:58803"
    PHOTO_URL = ["https://telegra.ph/file/c147cc4bbcf37552a326e.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "GuessTheCharacterGroup"
    UPDATE_CHAT = "GuessTheCharacterUpdates"
    BOT_USERNAME = "GuessTheMovieCharacterBot"
    CHARA_CHANNEL_ID = "-1002040113200"
    api_id = 21187167
    api_hash = "f7c20f7bc2041887a70d62f94310e005"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
