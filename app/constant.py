from enum import Enum


class MedicineType(str, Enum):
    syrup = "Syrup"
    tablet = "Tablet"

class MedicineTime(str, Enum):
    morning = "Morning"
    noon = "Noon",
    evening = "Evening"