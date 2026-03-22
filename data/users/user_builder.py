from dataclasses import dataclass

from faker import Faker

fake = Faker("ru_RU")


@dataclass(frozen=True)
class UserData:
    first_name: str
    last_name: str
    login: str
    email: str
    password: str


class UserBuilder:

    def __init__(self):
        self.first_name: str | None = None
        self.last_name: str | None = None
        self.login: str | None = None
        self.email: str | None = None
        self.password: str | None = None

    def with_first_name(self, first_name: str) -> "UserBuilder":
        self.first_name = first_name
        return self

    def with_last_name(self, last_name: str) -> "UserBuilder":
        self.last_name = last_name
        return self

    def with_login(self, login: str) -> "UserBuilder":
        self.login = login
        return self

    def with_email(self, email: str) -> "UserBuilder":
        self.email = email
        return self

    def with_password(self, password: str) -> "UserBuilder":
        self.password = password
        return self

    def build(self):
        return UserData(
            first_name=self.first_name if self.first_name is not None else fake.first_name(),
            last_name=self.last_name if self.last_name is not None else fake.last_name(),
            login=self.login if self.login is not None else fake.user_name(),
            email=self.email if self.email is not None else fake.email(),
            password=self.password if self.password is not None else fake.password(length=8, special_chars=False)
        )
