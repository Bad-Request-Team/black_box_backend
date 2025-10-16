from connectors import NeuralConnector


class States:
    def __init__(self):
        self.__neural_with_task = []
        self.__neural_without_task = []

    def add_neural(self, neural: NeuralConnector):
        self.__neural_without_task.append(neural)

    def get_neural(self):
        neural = self.__neural_without_task[0]
        self.__neural_with_task.append(neural)
        self.__neural_without_task.remove(neural)
        return neural
