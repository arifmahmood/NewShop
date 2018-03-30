from django.db import models


# Create your models here.


class Item(models.Model):
    itemName = models.CharField(max_length=50)
    itemSize = models.CharField(max_length=50)
    stockRate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saleRate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    itemAvailable= models.IntegerField(default=0)
    itemFree= models.IntegerField(default=0)

    def __str__(self):
        return self.itemName


class SalesRepresentative(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    mobileNo= models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    mobileNo = models.CharField(max_length=20)
    salesRepresentative = models.ForeignKey(SalesRepresentative)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    mobileNo = models.CharField(max_length=20)
    salesRepresentative = models.ForeignKey(SalesRepresentative)

    def __str__(self):
        return self.name


class SaleItem(models.Model):
    saleRate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    item = models.ForeignKey(Item)
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)

    def itemTotal(self):
        total=(self.quantity - self.free) * self.saleRate
        return (self.quantity - self.free) * self.saleRate


class SaleMemo(models.Model):

    date = models.DateField()
    party = models.ForeignKey(Customer)
    saleItem = models.ManyToManyField(SaleItem)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    due=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    memoTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    actualTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    def getTotal(self):
        # type: () -> object

        return sum(i.itemTotal() for i in self.saleItem.all())


class ReturnSaleMemo(models.Model):

    givenMemoNo=models.ForeignKey(SaleMemo)
    date = models.DateField()
    returnSaleItem = models.ManyToManyField(SaleItem)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    due=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    memoTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    actualTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    def getTotal(self):
        # type: () -> object

        return sum(i.itemTotal() for i in self.returnSaleItem.all())


class PurchaseItem(models.Model):
    purchaseRate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    item = models.ForeignKey(Item)

    def itemTotal(self):
        return (self.quantity - self.free) * self.purchaseRate


class PurchaseMemo(models.Model):
    givenMemoNo = models.CharField(max_length=50)
    date = models.DateField()
    party = models.ForeignKey(Supplier)
    purchaseItem = models.ManyToManyField(PurchaseItem)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    memoTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    actualTotal= models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)
    due=models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)



    def getTotal(self):
        return sum(i.itemTotal() for i in self.purchaseItem.all())

class Payment(models.Model):
    date = models.DateField()
    partyType = models.IntegerField(default=0)
    partyId = models.IntegerField(default=-1)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    others = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0, blank=True, null=True)






