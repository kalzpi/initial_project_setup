from django.db import models
from core import models as core_models

# Create your models here.


class AbstractPurchasing(core_models.TimeStampedModel):

    """Common contents for every purchasing order"""

    po_number = models.CharField(max_length=150)
    issued_date = models.DateField()
    order_to = models.CharField(max_length=150)
    order_from = models.CharField(max_length=150, default="SRC")
    revision = models.IntegerField(default=0)
    subject = models.CharField(max_length=150)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Purchasing(AbstractPurchasing):
    # base design은 project에 할당된 roll에 할당된 design에 할당된 partdesign을 불러와야함.
    # 발주규격은 위 base design + specific design에 명시된 값을 읽어와야함.

    pass


# Note: PO 작성 및 결재가 끝난 뒤 나중에 Lightbox로 PO preview를 보여주고 pdf print or pdf save button을 배치할 예정.
