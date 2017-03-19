from django.db import models

# Create your models here.
class NumericSystem(models.Model):
	class Meta:
		db_table = "NumericSystem"

	section_name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.section_name)


class AlgebraicSystem(models.Model):
	class Meta:
		db_table = "AlgebraicSystem"

	section_name = models.CharField(max_length=200)

	def __str__(self):
		return str(self.section_name)


class NumericSection(models.Model):
	class Meta:
		db_table = "NumericSection"

	section_name = models.ForeignKey('NumericSystem', on_delete=models.CASCADE)
	subsection_name = models.CharField(max_length=200)
	subsection_text = models.TextField()
	

class AlgebraicSection(models.Model):
	class Meta:
		db_table = "AlgebraicSection"

	section_name = models.ForeignKey('AlgebraicSystem', on_delete=models.CASCADE)
	subsection_name = models.CharField(max_length=200)
	subsection_text = models.TextField()

