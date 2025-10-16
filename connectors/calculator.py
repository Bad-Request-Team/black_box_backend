from models import LastMessage, AnalystData, GraphicMessage


class Calculator:
    def __init__(self): 
        self.__aggressive_percents = []
        self.__lane_percents = []

    def calc_graphic(self, data: AnalystData) -> GraphicMessage:
        aggressive_percent = data.aggressive_count / data.total_count * 100
        lane_percent = data.lane_count / data.aggressive_count * 100
        self.__aggressive_percents.append(aggressive_percent)
        self.__lane_percents.append(lane_percent)
        return GraphicMessage(lane_percent=self.__lane_percents, aggressive_percent=self.__aggressive_percents)

    def calc_last(self, data: AnalystData) -> LastMessage:
        normal_drivers = data.total_count - data.aggressive_count
        return LastMessage(drivers_count=data.total_count,
                            normal_drivers_count=normal_drivers,
                            aggressive_drivers_count=data.aggressive_count,
                            abrupt_braking_count = data.br_count,
                            abrupt_acceleration_count = data.acc_count,
                            avg_speed = data.avg_speed,
                            avg_angle = data.avg_angle,
                            avg_acc = data.avg_acc)