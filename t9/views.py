from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from t9.models import Reporter, News  # Import your models


def create_data(request):
    # Add data to Reporter table
    reporter_data = [
        {
            'name': 'John',
            'family': 'Doe',
            'email': 'john@example.com',
            'salary': 3000,
        },
        {
            'name': 'Alice',
            'family': 'Smith',
            'email': 'alice@example.com',
            'salary': 4000,
        },
        {
            'name': 'Bob',
            'family': 'Johnson',
            'email': 'bob@example.com',
            'salary': 2500,
        },
        {
            'name': 'Emily',
            'family': 'Brown',
            'email': 'emily@example.com',
            'salary': 3500,
        },
        {
            'name': 'Michael',
            'family': 'Davis',
            'email': 'michael@example.com',
            'salary': 4500,
        }
    ]

    for data in reporter_data:
        email = data['email']
        if not Reporter.objects.filter(email=email).exists():
            reporter = Reporter(**data)
            reporter.save()

    # Add data to News table
    news_data = [
        {
            'title': 'Economy on the Rise',
            'short_title': 'Economy',
            'category': 'economic',
            'short_content': 'Positive growth reported in the economy this quarter.',
            'content': 'Detailed content about the economic growth.',
        },
        {
            'title': 'Political Debate Heats Up',
            'short_title': 'Debate',
            'category': 'political',
            'short_content': 'Key politicians clash on crucial policy matters.',
            'content': 'Detailed coverage of the recent political debate.',
        },
        {
            'title': 'Cultural Festival Begins',
            'short_title': 'Festival',
            'category': 'cultural',
            'short_content': 'Celebration of diversity kicks off in the city.',
            'content': 'Highlights and events of the cultural festival.',
        },
        {
            'title': 'Sports Championship Concludes',
            'short_title': 'Championship',
            'category': 'sports',
            'short_content': 'Thrilling matches mark the end of the sports championship.',
            'content': 'Recap and president of the final matches.',
        },
        {
            'title': 'New Technology Breakthrough',
            'short_title': 'Breakthrough',
            'category': 'economic',
            'short_content': 'Innovation poised to revolutionize the tech industry.',
            'content': 'Detailed explanation president of the new technological advancement.',
        }
    ]

    for data in news_data:
        news = News(**data)
        news.save()
    return HttpResponse("Data creation process completed successfully")

def get_political_news(request):
    political_news = News.objects.filter(category='political').values(
        'title', 'short_title', 'category', 'short_content', 'content', 'dateOfcreate'
    )
    political_news_list = list(political_news)
    return JsonResponse(political_news_list, safe=False)


def get_filtered_journalists(request):
    # Filtering journalists based on salary and employment date range
    filtered_journalists = Reporter.objects.filter(
        salary__range=(2000, 4000)
    ).exclude(
        Q(dateOfemp__year__range=(2014, 2016))
    )

    # Serialize the queryset to return JSON response
    journalist_data = list(filtered_journalists.values(
        'name', 'family', 'email', 'salary', 'dateOfemp'
    ))

    return JsonResponse(journalist_data, safe=False)


def get_news_by_keyword(request):
    keyword = 'president'  # Change this keyword as needed

    # Filtering news based on content containing the keyword
    news_with_keyword = News.objects.filter(content__icontains=keyword)

    # Serialize the queryset to return JSON response
    news_data = list(news_with_keyword.values(
        'title', 'short_title', 'category', 'short_content', 'content', 'dateOfcreate'
    ))

    return JsonResponse(news_data, safe=False)


def update_short_titles(request):
    news_before_2014 = News.objects.filter(dateOfcreate__year__lt=2014)

    for news in news_before_2014:
        news.short_title = 'News 2014'
        news.save()

    return HttpResponse("Short titles updated successfully for news produced before 2014")


def delete_sports_2014_news(request):
    News.objects.filter(short_title='News 2014', category='sports').delete()

    return HttpResponse("Sports news with short title 'News 2014' deleted successfully")
