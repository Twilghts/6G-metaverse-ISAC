from abc import ABC, abstractmethod
from enum import Enum


class Data(ABC):
    @abstractmethod
    def __init__(self, slice_sign: int, dataid: int):
        self.sign = dataid
        self.slice_sign = slice_sign
        self.current_router: int = -1
        self.path: list = []

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class CommunicationData(Data):
    def __init__(self, slice_sign: int, dataid: int, bandwidth_required: int = 1):
        super().__init__(slice_sign, dataid)

        self.bandwidth_required: int = bandwidth_required
        self.delay: int = 0  # 代表了数据包在上一段链路的时延
        self.delay_every_step: list = []

    def __repr__(self):
        return f"CommunicationData,要求的带宽资源为:{self.bandwidth_required}"

    def __str__(self):
        return f"CommunicationData,要求的带宽资源为:{self.bandwidth_required}"


class CalculateData(Data):
    def __init__(self, slice_sign: int, dataid: int, calculate_required: int = 1):
        super().__init__(slice_sign, dataid)
        self.calculate_required: int = calculate_required
        self.delay: int = 0

    def __repr__(self):
        return f"CalculateData,要求的计算资源为:{self.calculate_required}"

    def __str__(self):
        return f"CalculateData,要求的计算资源为:{self.calculate_required}"


class SensorData(Data):
    def __init__(self, slice_sign: int, dataid: int, storage_required: int = 1, count=3):
        super().__init__(slice_sign=slice_sign, dataid=dataid)
        self.storage_required: int = storage_required
        self.count = count

    def __repr__(self):
        return f"SensorData,要求的存储资源为:{self.storage_required}"

    def __str__(self):
        return f"SensorData,要求的存储资源为:{self.storage_required}"


class TypeOfData(Enum):
    sensor_data = SensorData
    calculate_data = CalculateData
    communication_data = CommunicationData


class DataFactory:
    @staticmethod
    def create_data(task_type: TypeOfData, slice_sign: int, dataid: int) -> Data:
        if task_type == TypeOfData.communication_data:
            return CommunicationData(slice_sign=slice_sign, dataid=dataid)
        elif task_type == TypeOfData.calculate_data:
            return CalculateData(slice_sign=slice_sign, dataid=dataid)
        elif task_type == TypeOfData.sensor_data:
            return SensorData(slice_sign=slice_sign, dataid=dataid)
