CHANNEL_DEFAULT = {
    'only_meme_speak_channel': 0,
    'run_out_before_look': 0,
    'backup_channel_id': 0
}
OVERFLOW_DEFAULT = {"資訊": {"header": "", "footer": "", "hp": 90}, "報名列表": []}
REPORT_DAMAGE_DEFAULT = {"資訊": {"header": "", "footer": "", "hp": 90}, "報名列表": []}
ALL_OUT_KNIFE_DATA_DEFAULT = {1: {'1王': {'資訊': {"header": "", "footer": "", "hp": 600, "week":1}, '報名列表': []},
                            '2王': {'資訊': {"header": "", "footer": "", "hp": 800, "week":1}, '報名列表': []},
                            '3王': {'資訊': {"header": "", "footer": "", "hp": 1000, "week":1}, '報名列表': []},
                            '4王': {'資訊': {"header": "", "footer": "", "hp": 1200, "week":1}, '報名列表': []},
                            '5王': {'資訊': {"header": "", "footer": "", "hp": 1500, "week":1}, '報名列表': []},
                            '補償清單': OVERFLOW_DEFAULT,
                            '出刀清單': REPORT_DAMAGE_DEFAULT}}
NOW_DEFAULT = {'周': 1, '王': 1, 'limit_max_week': 10, 'force_week': 1}
KING_HP_DEFAULT = [[1, 10, 600, 800, 1000, 1200, 1500], [
        11, 34, 1200, 1400, 1700, 1900, 2200], [35, 44, 1900, 2000, 2300, 2500, 2700], [45, False, 8500, 9000, 9500, 10000, 11000]]
# 573893554577866777 窩們一起學牛叫：O
# <@&750720404213203079> @美美管理員
#
# 727170387091259393 功德無量
# 734391146910056478 @TEST
GUILD_ID_DEFAULT = 727170387091259393
ROLE_ID_DEFAULT = 734391146910056478