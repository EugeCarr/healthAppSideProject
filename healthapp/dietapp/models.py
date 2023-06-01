from django.db import models

class Patient(models.Model):
    patNum = models.AutoField(primary_key=True, verbose_name="Patient Number")
    firstName = models.CharField(max_length=255, null=True, verbose_name="First Name")
    lastName = models.CharField(max_length=255, null=True, verbose_name="Last Name")
    age = models.IntegerField(verbose_name="Age")
    checkedIn = models.BooleanField()
    gender = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=1, decimal_places=1,)
    height = models.DecimalField(max_digits=1, decimal_places=1)

class Dietician(models.Model):
    dieticianNum = models.AutoField(primary_key=True, verbose_name="Dietician Number")
    firstName = models.CharField(max_length=255, null=True, verbose_name="First Name")
    lastName = models.CharField(max_length=255, null=True, verbose_name="Last Name")
    title = models.CharField(max_length=50, null=True, verbose_name="Title")

class Diet(models.Model):
    dietNum = models.AutoField(primary_key=True, verbose_name="Diet Number")
    dietName = models.CharField(max_length=255, null= False, verbose_name="Diet Name")
    patNum = models.ForeignKey("Patient", on_delete=models.CASCADE, verbose_name="Patient")
    dieticianId = models.ForeignKey("Dietician", on_delete=models.CASCADE, verbose_name="Dietician")
    startDate = models.DateField(verbose_name="Start Date")
    endDate = models.DateField(verbose_name="End Date")
    dailyCalories = models.IntegerField(verbose_name="Calorie target")
    targetWeight = models.DecimalField(max_digits=1, decimal_places=1, verbose_name="Target weight")

class Meal(models.Model):
    mealNum = models.AutoField(primary_key=True, verbose_name="Meal Number")
    mealName = models.CharField(max_length=255)
    dietNum = models.ForeignKey("Diet", on_delete=models.CASCADE, verbose_name="Diet")
    

class FoodItem(models.Model):
    foodDocId = models.IntegerField(primary_key=True, verbose_name="Food Doc Id", unique=True)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

class FoodItemMealMap(models.Model):
    mealNum = models.ForeignKey("Meal", on_delete=models.CASCADE, verbose_name="Meal")
    foodItem = models.ForeignKey("FoodItem", on_delete=models.CASCADE, verbose_name="Food Item")
