from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Patient Number")
    firstName = models.CharField(max_length=255, null=True, verbose_name="First Name")
    lastName = models.CharField(max_length=255, null=True, verbose_name="Last Name")
    age = models.IntegerField(verbose_name="Age")
    checkedIn = models.BooleanField()
    gender = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=1, decimal_places=1,)
    height = models.DecimalField(max_digits=1, decimal_places=1)

class Dietician(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Dietician Number")
    firstName = models.CharField(max_length=255, null=True, verbose_name="First Name")
    lastName = models.CharField(max_length=255, null=True, verbose_name="Last Name")
    title = models.CharField(max_length=50, null=True, verbose_name="Title")

class Diet(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Diet Number")
    dietName = models.CharField(max_length=255, null= False, verbose_name="Diet Name")
    patientId = models.ForeignKey(to="Patient", to_field="id", on_delete=models.CASCADE, verbose_name="Patient")
    dieticianId = models.ForeignKey(to="Dietician", to_field="id", on_delete=models.CASCADE, verbose_name="Dietician")
    startDate = models.DateField(verbose_name="Start Date")
    endDate = models.DateField(verbose_name="End Date")
    dailyCalories = models.IntegerField(verbose_name="Calorie target")
    targetWeight = models.DecimalField(max_digits=1, decimal_places=1, verbose_name="Target weight")

class Meal(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Meal Number")
    mealName = models.CharField(max_length=255)
    dietNum = models.ForeignKey(to="Diet", on_delete=models.CASCADE, to_field="id", verbose_name="Diet")
    

class FoodItem(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Food Doc Id", unique=True)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

class FoodItemMealMap(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Food Item Meal Id", unique=True,)
    mealId = models.ForeignKey(to="Meal", on_delete=models.CASCADE, verbose_name="Meal", to_field="id")
    foodItemId = models.ForeignKey(to="FoodItem", on_delete=models.CASCADE, verbose_name="Food Item", to_field="id")
