from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Union


class Data(ABC):
    @abstractmethod
    def __init__(self, slice_sign: int, dataid: int, task_id: int):
        self.sign = dataid
        self.slice_sign = slice_sign
        self.type = None
        self.current_router: int = -1
        self.task_id = task_id

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class CommunicationData(Data):
    def __init__(self, slice_sign: int, dataid: int, task_id: int, bandwidth_required: int = 1,
                 path: Union[List[int], None] = None):
        super().__init__(slice_sign=slice_sign, dataid=dataid, task_id=task_id)
        self.type = "CommunicationData"
        self.path: Union[List[int], None] = path
        self.bandwidth_required: int = bandwidth_required
        self.delay: int = 0  # 代表了数据包在上一段链路的时延
        self.delay_every_step: list = []

    def __repr__(self):
        return f"CommunicationData,要求的带宽资源为:{self.bandwidth_required}"

    def __str__(self):
        return f"CommunicationData,要求的带宽资源为:{self.bandwidth_required}"


class CalculateData(Data):
    def __init__(self, slice_sign: int, dataid: int, task_id: int, calculate_required: int = 1):
        super().__init__(slice_sign=slice_sign, dataid=dataid, task_id=task_id)
        self.type = "CalculateData"
        self.calculate_required: int = calculate_required
        self.delay: int = 0

    def __repr__(self):
        return f"CalculateData,要求的计算资源为:{self.calculate_required}"

    def __str__(self):
        return f"CalculateData,要求的计算资源为:{self.calculate_required}"


class SensorData(Data):
    def __init__(self, slice_sign: int, dataid: int, task_id: int, specific_type: int, path, storage_required: int = 1,
                 count=3):
        super().__init__(slice_sign=slice_sign, dataid=dataid, task_id=task_id)
        self.type = "SensorData"
        self.storage_required: int = storage_required
        self.count = count
        self.delay: int = 0  # 代表了数据包在上一段链路的时延
        self.delay_every_step: list = []
        self.specific_type = specific_type
        self.path = path

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
    def create_data(task_type: TypeOfData, slice_sign: int, task_id: int,
                    dataid: int, path: Union[List[int], None] = None, specific_type=None) -> Data:
        if task_type == TypeOfData.communication_data:
            return CommunicationData(slice_sign=slice_sign, dataid=dataid, path=path, task_id=task_id)
        elif task_type == TypeOfData.calculate_data:
            return CalculateData(slice_sign=slice_sign, dataid=dataid, task_id=task_id)
        elif task_type == TypeOfData.sensor_data:
            return SensorData(slice_sign=slice_sign, dataid=dataid, specific_type=specific_type, path=path,
                              task_id=task_id)
