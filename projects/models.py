from django.db import models
from django.urls import reverse
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

    def project_status(self):
        case = 0
        # Project.project_status를 불러올때 project 진행 상황에 대해 str로 return해주는 method.
        # 설계 사양 등록여부, 소재 준비여부(준비됨 or 입고예정일), 생산 돌입여부, 출고여부 등등

    def is_design_applied(self):
        if self.designs.all().first() is not None:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})

    def test_method(self):
        print(self.rolls.all())

    def __str__(self):
        return self.name
