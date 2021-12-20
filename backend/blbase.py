import re
from dlbase import DLBase
from entity import ServiceResult

class BLBase:
    def __init__(self):
        pass
    
    def filter(self, type, value):
        dl = DLBase()
        if type == 1:
            data = dl.getInfoPlace(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 2:
            data = dl.getFesitvalInfo(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 3:
            data = dl.getLocationPlace(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 4:
            data = dl.getLocationFestival(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 5:
            data = dl.getActivitiesFestival(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 6:
            data = dl.getPurposeFestival(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 7:
            data = dl.getTimeHoldFestival(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 8:
            data = dl.getInfoTour(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 9:
            data = dl.getCostTour(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 10:
            data = dl.getPlanTour(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 11:
            value = self.formatMonth(value)
            if value == 13:
                return self.notFind()
            else:
                data = dl.getSuggestFestival(0, value)
                if len(data) > 0:
                    return self.sendResult(data)
                else:
                    return self.notFind()
        elif type == 12:
            data = dl.getSuggestFestival(1, value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()
        elif type == 13:
            data = dl.getSuggestTour(value)
            if len(data) > 0:
                return self.sendResult(data)
            else:
                return self.notFind()

    def notFind(self):
        result = {}
        result['code'] = 404
        result['msg'] = "Rất tiếc mình không biết câu trả lời"
        return result

    def sendResult(self, data):
        result = {}
        result['code'] = 100
        result['data'] = data
        return result

    def formatMonth(self, data):
        if data == 1 or data == "một" or data == "giêng":
            return 1
        elif data == 2 or data == "hai":
            return 2
        elif data == 3 or data == "ba":
            return 3
        elif data == 4 or data == "bốn":
            return 4
        elif data == 5 or data == "năm":
            return 5
        elif data == 6 or data == "sáu":
            return 6
        elif data == 7 or data == "bảy":
            return 7
        elif data == 8 or data == "tám":
            return 8
        elif data == 9 or data == "chín":
            return 9
        elif data == 10 or data == "mười":
            return 10
        elif data == 11 or data == "mười một":
            return 11
        elif data == 12 or data == "mười hai" or data == "chạp" or data == "tháng chạp":
            return 12
        else:
            return 13