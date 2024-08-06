import json, datetime, os
from dateutil.relativedelta import relativedelta


class IPGuard:
    Default_BanDuration_Year = 0
    Default_BanDuration_Month = 0
    Default_BanDuration_Day = 30

    @staticmethod
    def TimeString():
        return str(datetime.date.today())

    @staticmethod
    def NewBlock(ip, exp_date):
        return {"IP": ip, "BanExpiration": exp_date}

    @staticmethod
    def CreateExpiredDate(today, year, month, day):
        today_date = datetime.datetime.strptime(today, "%Y-%m-%d").date()
        new_date = today_date + relativedelta(years=year, months=month, days=day)
        return new_date.strftime("%Y-%m-%d")

    @staticmethod
    def IsBanExpired(expiration_date: str) -> bool:
        today = datetime.date.today()
        exp_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
        return exp_date < today

    def InitializeDB(self):
        # filename_string = f"{self.TimeString()}-Banned-ips.json"
        filename_string = "Banned-ips.json"

        if not os.path.exists(filename_string):
            with open(filename_string, "w") as init_file:
                json.dump({"BannedIPs": []}, init_file)

        return filename_string

    def Ban(self, IP: str, year=None, month=None, day=None):
        if year is None:
            year = self.Default_BanDuration_Year
        if month is None:
            month = self.Default_BanDuration_Month
        if day is None:
            day = self.Default_BanDuration_Day

        DB_name = self.InitializeDB()

        today = self.TimeString()
        exp_date = self.CreateExpiredDate(today=today, year=year, month=month, day=day)

        data = {
            "BannedIPs": []
        }

        data = json.load(open(DB_name, "r"))

        for block in data['BannedIPs']:
            if block['IP'] == IP:
                return

        data['BannedIPs'].append(self.NewBlock(IP, exp_date))

        with open(DB_name, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def UnBan(self, IP: str):
        file_name = self.InitializeDB()

        data = {
            "BannedIPs": []
        }

        data = json.load(open(file_name, "r"))

        for record in data["BannedIPs"]:
            if record["IP"] == IP:
                data["BannedIPs"].remove(record)
                break

        with open(file_name, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def IsBan(self, IP: str):
        DB_name = self.InitializeDB()
        file = open(DB_name, "r")
        data = json.load(file)

        for record in data["BannedIPs"]:
            if record["IP"] == IP and not self.IsBanExpired(record["BanExpiration"]):
                return True

        return False


# ip_guard = IPGuard()
#
# print(ip_guard.IsBan("192.168.1.20"))
#
# ip_guard.Ban("192.168.1.20", year=0, month=0, day=15)
#
# print(ip_guard.IsBan("192.168.1.20"))
#
# ip_guard.UnBan("192.168.1.20")
#
# print(ip_guard.IsBan("192.168.1.20"))
