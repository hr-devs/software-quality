from dataclasses import dataclass

@dataclass
class User:
    username: str = ""
    password: str = ""
    role_id: int = 0


@dataclass
class Role:
    role_name: str = ""


@dataclass
class Traveller:
    first_name: str = ""
    last_name: str = ""
    birthday: str = ""
    gender: str = ""
    street_name: str = ""
    house_number: int = 0
    zip_code: str = ""
    city: str = ""
    email_address: str = ""
    mobile_phone: str = ""
    driving_license_number: str = ""


@dataclass
class Scooter:
    brand: str = ""
    model: str = ""
    serial_number: str = ""
    top_speed: int = 0
    battery_capacity: int = 0
    soc: float = 0.0
    soc_min_target: float = 0.0
    soc_max_target: float = 0.0
    description: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    out_of_service: int = 0
    mileage: float = 0.0
    last_maintenance_date: str = ""


@dataclass
class ActivityLog:
    log_date: str = ""
    log_time: str = ""
    username: str = ""
    activity_description: str = ""
    additional_info: str = ""
