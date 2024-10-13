from django.db import models
import uuid

# Create your models here.

# @Entity = models.Model tự động ánh xạ class đó thành một bảng trong cơ sở dữ liệu
# models.CharField giống như @Column trong JPA 
# Migration trong Django giống như quá trình Hibernate spring.jpa.hibernate.ddl-auto=update
# Repository trong Spring Boot và Object-Relational Mapping trong Django, Django có hệ thống ORM tích hợp sẵn, không cần viết các lớp repository riêng, mọi thứ đều có sẵn trong model.
# Django không tự động tạo bảng ngay lập tức. Thay vào đó, bạn sử dụng lệnh python manage.py makemigrations
# python manage.py migrate
class Project(models.Model):
      title = models.CharField(max_length=100)
      description = models.TextField(null=True, blank=True)
      demo_link = models.CharField(max_length=2000, null=True, blank=True)
      source_link = models.CharField(max_length=2000, null=True, blank=True)
      tags = models.ManyToManyField('Tag', blank=True)
      vote_total = models.IntegerField(default=0, null=True, blank=True)
      vote_ratio = models.IntegerField(default=0, null=True, blank=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


      def __str__(self):
          return self.title
      

class Review(models.Model):
    VOTE_TYPE = (
         ('up', 'Up Vote'),
         ('down', 'Down Vote'),
     )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



