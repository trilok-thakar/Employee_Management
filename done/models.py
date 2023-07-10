from django.db import models

# Create your models here.

ROLE_CHOICES = (
    ('ceo', 'CEO'),
    ('cto', 'CTO'),
    ('team leader', 'Team Leader'),
    ('jr.developer', 'Jr. Developer'),
    ('sr.developer', 'Sr.Developer'),
    ('hr executive', 'HR Executive'),
    ('hr head', 'HR Head'),
)



class Employee(models.Model):
    code = models.CharField(max_length=4, unique=True, blank=True, null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
 
    @classmethod
    def generate_code(cls):
        last_employee = cls.objects.order_by('-id').first()
        if last_employee:
            last_code = last_employee.code
            if last_code:
                last_number = int(last_code[4:])
                new_number = last_number + 1
                new_code = f'acqu{new_number}'
            else:
                new_code = 'acqu1'
        else:
            new_code = 'acqu1'
        return new_code

    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        super().save(*args, **kwargs)

    

