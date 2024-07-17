
from mycelery.main import app
import time
import datetime
from django.utils.timezone import now
import pymysql

def get_all_data_from_db():
    import pymysql

    # 连接数据库
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 password='123',
                                 database='book_store',
                                 charset='utf8mb4')

    with connection.cursor() as cursor:
        start_date = datetime.datetime.now().replace(day=1)
        start = start_date.strftime("%Y-%m-%d")
        # 获取下个月的第一天，用于筛选结束
        end_date = (start_date + datetime.timedelta(days=32)).replace(day=1)
        end = end_date.strftime("%Y-%m-%d")
        sql = "SELECT id FROM books_book where publication_date >= %(start)s and publication_date <= %(end)s "
        # sql = "SELECT * FROM books"
        # 执行SQL语句
        cursor.execute(sql, {"start": start, "end": end})
        books_nums = cursor.rowcount
        sql1 = "SELECT DISTINCT author FROM books_book where publication_date >= %(start)s and publication_date <= %(end)s "
        cursor.execute(sql1, {"start": start, "end": end})
        ret = cursor.fetchall()
        authors_list = []
        for item in ret:
            authors_list.append(item[0])

        author_detail = {}
        for name in authors_list:
            sql2 = "SELECT id FROM books_book where publication_date >= %(start)s and publication_date <= %(end)s  and author=%(author)s"
            cursor.execute(sql2, {"start": start, "end": end, 'author': name})
            # ret = cursor.rowcount
            author_detail[name] = cursor.rowcount
        data = {'books_nums': books_nums, 'authors_num': len(authors_list), 'author_detail': author_detail}
        return data
@app.task
def get_books_data():
    # current_datetime = now()
    #     # # 获取本月的第一天
    #     # first_day_of_month = current_datetime.replace(day=1)
    #     # # 获取下个月的第一天，用于筛选结束
    #     # next_month_first_day = (first_day_of_month + datetime.timedelta(days=32)).replace(day=1)
    #     #
    #     # # 筛选本月的数据
    #     # month_data = Book.objects.filter(
    #     #     publication_date__gt=first_day_of_month,
    #     #     publication_date__lt=next_month_first_day
    #     # )
    #     # total_num = month_data.count()
    #     # authot_list = month_data.values_list('author', flat=True).distinct()
    #     # author_num = len(authot_list)
    #     # author_detail = {}
    #     # for author in authot_list:
    #     #     num = month_data.filter(author=author).count()
    #     #     author_detail[author] = num
    #     # import json
    #     # ret = {'total_num': total_num, 'author_num': author_num, 'author_detail': author_detail}
    data = get_all_data_from_db()
    return data

'''
docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123 -d mysql:latest
docker exec -it some-mysql mysql -u root -p
celery -A mycelery.main worker --loglevel=info

python manage.py runserver 0.0.0.0:8000
python3 manage.py makemigrations books
python3 manage.py migrate books

'''