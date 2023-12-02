# models.py
# models.py

from django.db import models

class Studentinfo(models.Model):
    name = models.CharField(max_length=255, null=True)
    student_id = models.AutoField(primary_key=True)
    place = models.TextField()
    mark = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    phoneno = models.CharField(max_length=15, null=True)

#     def __str__(self) -> str:
#         return self.name

    #     return f"{self.student_id}: {self.name} from {self.place}"




# modelform command


# from django.db import models

# class StudentModel(models.Model):
#      name = models.CharField(max_length=255, null=True)
#      student_id = models.AutoField(primary_key=True)
#      place = models.TextField()
#      mark = models.DecimalField(max_digits=5, decimal_places=2, null=True)
#      phoneno = models.CharField(max_length=15, null=True)
#      def __str__(self) -> str:
#         return self.name

    


   