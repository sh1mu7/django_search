# import random

# from django.template.defaultfilters import date
# from django.utils.datetime_safe import datetime


# def main():
#     fake: Faker = Faker()
    
#     for i in range(500):
#         post = Posts.objects.create(
#             author_name=fake.name(),
#             title=fake.paragraph(nb_sentences=1),
#             post=fake.paragraph(nb_sentences=10),
#             published_date=fake.date_between(start_date='-5y', end_date='now'),
#             views=random.randint(0, 1000)

#         )
#         print(f'Author: {post.author_name} is posted at {post.published_date}')
#         post_count = Posts.objects.count()
#         print(f'There are {post_count} post in database')
#     student = Posts.objects.all()
#     print(f"There are {student.count()} student in the database")


# if __name__ == "__main__":
#     import os

#     from django.core.wsgi import get_wsgi_application

#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new.settings")
#     application = get_wsgi_application()

#     from test1.models import Posts
#     from faker import Faker

#     main()




a,b,c=map(float,input().split())

x=max(a,b,c)
z=min(a,b,c)
y=(a+b+c)-x-z
a,b,c=x,y,z

if a>=b+c:
    print('NAO FORMA TRIANGULO')
elif a*a==b*b+c*c:
    print('TRIANGULO RETANGULO')
elif a*a>b*b+c*c:
    print('TRIANGULO OBTUSANGULO')
elif a*a<b*b+c*c:
    print('TRIANGULO ACUTANGULO')
if (a==b and b==c):
    print('TRIANGULO EQUILATERO')
elif (a==b or b==c):
    print('TRIANGULO ISOSCELES')
 