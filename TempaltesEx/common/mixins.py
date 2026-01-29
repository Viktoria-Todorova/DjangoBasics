from typing import Any


class DisableFormMixin:
    def __init__(self, *args:Any, **kwargs:Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True