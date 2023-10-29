from dataclasses import dataclass
from typing import Protocol
from services import EmailService
from functools import lru_cache

SMTP_SERVER = 'SMTP.gmail.com'
PORT = 465
EMAIL = 'hi@gmail.com'
PASSWORD = 'password'

class EmailSender(Protocol):
    def send_message(self, to_email:str,subject:str, body:str) ->None:
        ...

@lru_cache
def bmi(weight: float,height: float) -> float:
    return weight / (height**2)

@lru_cache
def bmi_category(bmi_value: float) -> str:
    if bmi_value<18.5:
        return 'Underweight'
    elif bmi_value<25:
        return 'normal'
    elif bmi_value<30:
        return 'overweight'
    else:
        return 'Obese'

@dataclass
class Stats:
    age: int
    gender: str
    height: float
    weight: float
    blood_type:str
    eye_color: str
    hair_color: str

@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    country: str
    postal_code: str

    def __str__(self) -> str:
        return f"{self.address_line1}, {self.address_line2}, {self.city}, {self.country}, {self.postal_code}"

@dataclass
class Person:
    name: str
    address: Address
    email: str
    phone_number: str
    stats: Stats

    @property
    def split_name(self) -> tuple[str,str]:
        first_name, last_name = self.name.split(" ")
        return first_name, last_name

    def update_email(self, email:str, email_service: EmailSender) -> None:
        self.email = email

        email_service.send_message(
            self.email,
            "Your email has been updated.",
            'Your email has been updated. If this was not you, you have a problem.'
        )

def main() -> None:
    address = Address(
        address_line_1= '123 Main st',
        address_line_2 = 'Apt 1',
        city = 'Nairobi',
        country = 'Kenya',
        postal_code = '12345',
    )
    stats = Stats(
        age = 30,
        gender = 'male',
        height = 1.6,
        weight = 70,
        blood_type = 'A',
        eye_color = 'Brown',
        hair_color = 'Black',
    )
    person = Person(
        name = 'John Doe',
        address= address,
        email = 'johndoe@gmail.com',
        phone_number = '123-456-7890',
        stats= stats,
    )

    bmi_value = bmi(stats.weight,stats.height)
    print(f'Your BMI is {bmi_value:.2f}')
    print(f'Your BMI category is {bmi_category(bmi_value)}')

    email_service = EmailService(SMTP_SERVER,PORT, EMAIL,PASSWORD)
    person.update_email('johndoe@gmail.com', email_service)


if __name__ == '__main__':
    main()
