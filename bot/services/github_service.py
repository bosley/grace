from typing import Union, Optional
from github import Github
from github.Repository import Repository
from bot import app


class GithubService(Github):
    __token: Optional[Union[str, int, bool]] = app.config.get("github", "api_key")

    def __init__(self):
        if self.__token:
            super().__init__(self.__token)

    @classmethod
    def can_connect(cls):
        return cls.__token is not None

    def get_grace(self) -> Repository:
        return self.get_repo("code-society-lab/grace", lazy=True)

    def get_cursif(self) -> Repository:
        return self.get_repo("code-society-lab/cursif", lazy=True)
