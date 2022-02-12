from gdps_errors import Error
from Main import cursor

class Level():
    def __init__(self, result):
        self.level = result
    def id(self):
        return int(self.level[0])
    def name(self):
        return str(self.level[1])
    def description(self):
        return str(self.level[2])
    def objects(self):
        return int(self.level[6])
    def version(self):
        return int(self.level[9])
    def author_id(self):
        return int(self.level[10])
    def official_song(self):
        status = int(self.level[11])
        if status != 0:
            return True
        else:
            return False
    def custom_song(self):
        status = int(self.level[12])
        if status == 0:
            return True
        else:
            return False
    def requested_rate(self):
        return int(self.level[13])
    def difficulty(self):
        return int(self.level[14])
    def coins(self):
        return int(self.level[15])
    def coins_verified(self):
        status = int(self.level[16])
        if status == 1:
            return True
        else:
            return False
    def downloads(self):
        return int(self.level[17])
    def likes(self):
        return int(self.level[18])
    def length(self):
        return int(self.level[19])
    def demon(self):
        status = int(self.level[20])
        if status == 0:
            return False
        else:
            return True
    def demon_difficulty(self):
        return int(self.level[21])
    def stars(self):
        return int(self.level[22])
    def featured(self):
        status = int(self.level[23])
        if status == 1:
            return True
        else:
            return False
    def auto(self):
        status = int(self.level[24])
        if status == 1:
            return True
        else:
            return False
    def epic(self):
        status = int(self.level[25])
        if status == 1:
            return True
        else:
            return False
    def password(self):
        return int(self.level[26])
    def original(self):
        return int(self.level[27])
    def is_copy(self):
        status = int(self.level[30])
        if status == 1:
            return True
        else:
            return False

async def fetch_level(identify):
    if type(identify) is str:
        cursor.execute("select * from levels where name = %s", [str(identify)])
    elif type(identify) is int:
        cursor.execute("select * from levels where id = %s", [int(identify)])
    if cursor.rowcount == 0:
        raise Error.level_not_found
    elif cursor.rowcount > 1:
        raise Error.many_levels
    elif cursor.rowcount == 1:
        result = cursor.fetchall()[0]
        return Level(result)