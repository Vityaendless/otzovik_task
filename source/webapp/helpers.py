class Helper:
    @staticmethod
    def get_avg(data, length):
        total = 0
        for item in data:
            total += item.grade
        return total / length
