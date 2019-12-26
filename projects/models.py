from django.db import models
from core import models as core_models


class Project(core_models.TimeStampedModel):

    name = models.CharField(max_length=150, blank=False)
    initiator = models.ForeignKey(
        "users.User", related_name="projects", on_delete=models.SET_NULL, null=True
    )
    client = models.ForeignKey(
        "clients.Client", related_name="projects", on_delete=models.PROTECT, null=True
    )

    # flute type, order type(신작, 재생), 제작수량 등은 Project Create시 입력되어야 하나, 하나의 Project가 여러개의 Roll을 가질 수 있기 때문에
    # models의 column으로 작성하지 않고 hard coding으로 구현하여야 한다.

    def __str__(self):
        return self.name
