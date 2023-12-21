from django.http import HttpResponse
from django.shortcuts import render

from t11.models import MenuItem, Context, ContextItem, CarouselItem, NewsCategory, NewsItem


def main_view(request):
    all_categories = NewsCategory.objects.all()
    carousel_items = CarouselItem.objects.all()
    # Fetch all context columns
    context_columns = Context.objects.all()

    # Fetch items for each context column
    context_items = {}
    for column in context_columns:
        items = ContextItem.objects.filter(context=column)
        context_items[column] = items
    return render(request, 'main.html', {'all_categories': all_categories,'carousel_items': carousel_items,'context_items': context_items})


def search_view(request):
    return render(request, 'search.html')


def create_data(request):
    # Create the main menu items
    home = MenuItem.objects.create(title='خانه')
    news = MenuItem.objects.create(title='اخبار')
    archive = MenuItem.objects.create(title='آرشیو')
    about_us = MenuItem.objects.create(title='درباره ما')
    contact_us = MenuItem.objects.create(title='ارتباط با ما')
    login = MenuItem.objects.create(title='ورود به باشگاه خبرنگاران', link='/login')
    search = MenuItem.objects.create(title='', link='/search')

    # Create submenu items and relate them to their parent items
    news_sub_menu = MenuItem.objects.create(title='اخبار', parent=news)
    political = MenuItem.objects.create(title='سیاسی', parent=news_sub_menu)
    social = MenuItem.objects.create(title='اجتماعی', parent=news_sub_menu)
    sports = MenuItem.objects.create(title='ورزشی', parent=news_sub_menu)
    sports_sub_menu = MenuItem.objects.create(title='ورزشی', parent=sports)
    football = MenuItem.objects.create(title='فوتبال', parent=sports_sub_menu)
    volleyball = MenuItem.objects.create(title='والیبال', parent=sports_sub_menu)
    basketball = MenuItem.objects.create(title='بسکتبال', parent=sports_sub_menu)
    economic = MenuItem.objects.create(title='اقتصادی', parent=news_sub_menu)
    # ----------------------------------------------
    context_column1 = Context.objects.create(column_id='column1')
    context_column2 = Context.objects.create(column_id='column2')
    context_column3 = Context.objects.create(column_id='column3')

    context_column1_items = [
        ContextItem.objects.create(
            context=context_column1,
            image='images/malake.jpeg',
            title='(ویدئو) ملکه انگلیس به یک بچه فیل شیر داد',
            author='Unknown',
            link='#'
        ),
        ContextItem.objects.create(
            context=context_column1,
            image='images/police.jpg',
            title='(ویدئو) تعقیب و گریز پلیس با هامر سرقتی؛تلاش برای سرفت دو خودروی دیگر!',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column1,
            image='images/akasi.jpg',
            title='(تصاویر) برندگان مسابقه عکاسی از سگ‌ها در سال ۲۰۲۳',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column1,
            image='images/israel.jpg',
            title='(تصاویر) اسرائيل اردوگاه جبالیا را روی سر صدها فلسطینی خراب کرد',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column1,
            image='images/koshti.jpg',
            title='(ویدئو) مدرسه کشتی دختران؛تابوشکنی دختران',
            author='Unknown',
            link='#'
        ),
    ]

    context_column2_items = [
        ContextItem.objects.create(
            context=context_column2,
            image='images/gid.jpg',
            title='امریکا، ایران و خطر یک جنگ گسترده‌تر در خاورمیانه؟<br/>گیدئون راچمن',
            author='Unknown',
            link='#'
        ),
        ContextItem.objects.create(
            context=context_column2,
            image='images/pol.jfif',
            title='به این دلایل جنگ زمینی اسرائيل در غزه خوب پیش نخواهد رفت<br/>پل راجرز',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column2,
            image='images/arash.jpg',
            title='ترس و اضطراب می‌تواند کمک کند؛ چگونه از آن به نفع خود استفاده کنیم؟<br/>آرش جوانبخت',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column2,
            image='images/hamid.jpg',
            title='چگونه غرب در تلاش برای «اختراع مجدد اسرائيل» است؟<br/>حمید دباشی',
            author='Unknown',
            link='#'
        ),
    ]

    context_column3_items = [
        ContextItem.objects.create(
            context=context_column3,
            image='',
            title='سپهر حیدری یک سال محروم شد.',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='توضیح رییس دانشگاه تهران درباره درگیری با دانشجویان',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='وام مسکن ایثارگران 600 میلیون تومان شد',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='اختراع شگفت انگیز دانشمندان ایرانی در آمریکا',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='آمریکا در تله انفجاری غزه چه خواهد کرد؟',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='پشت پرده پام 300 میلیونی بانک ملی',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='رتبه آخر پرسپولیس در آسیا، کمترین فرصت گل',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='این پرسپولیسی مرد اول سینمای ایران شد',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='گران ترین ساعت دنیا به رونالدو رسید',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='طوفان برقی قدرتمند',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='جنگ خندق در قرن 21',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='پیش بینی قیمت بیت کوین',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='خداحافظی حسن یزدانی از کشتی',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='ایران باید با طالبان چه کند؟',
            author='Unknown',
            link='#'
        ), ContextItem.objects.create(
            context=context_column3,
            image='',
            title='چرا رشد اقتصادی چین منافع آمریکا را تهدید خواهد کرد؟',
            author='Unknown',
            link='#'
        ),
    ]
    # ----------------------------------------------
    carousel_item1 = CarouselItem.objects.create(
        title='اعلام حکم AFC: نتیجه سپاهان - الاتحاد 0-3 شد',
        description='علاوه بر نتیجه، سپاهان ۲۰۰هزار دلار جریمه و ۳ بازی خارج از نقش جهان باید بازی کند.',
        image='images/sepahan.jpg',
        link='/sepahan-details'
    )
    carousel_item2 = CarouselItem.objects.create(
        title='جزییات آتش‌سوزی مرگبار در کمپ ترک‌اعتیاد لنگرود',
        description='این خبر تکمیل می‌شود ...',
        image='images/kamp.jpg',
        link='/kamp-details'
    )
    carousel_item3 = CarouselItem.objects.create(
        title='فوران بلندترین آتشفشان فعال در اوراسیا',
        description='ستون‌های خاکستر برفراز شبه‌جزیره کامچاتکا روسیه به آسمان پرتاب شدند.',
        image='images/favaran.jpg',
        link='/favaran-details'
    )
    # ----------------------------------------------
    # Creating instances for each news category
    category_political = NewsCategory.objects.create(name='آخرین اخبار سیاسی')
    category_economic = NewsCategory.objects.create(name='آخرین اخبار اقتصادی')
    category_sports = NewsCategory.objects.create(name='آخرین اخبار ورزشی')
    category_cultural = NewsCategory.objects.create(name='آخرین اخبار فرهنگی')

    # Creating news items and associating them with their respective categories
    NewsItem.objects.create(category=category_political, title='دونالد ترامپ بزرگترین خطر برای جهان در سال ۲۰۲۴ خواهد بود.')
    NewsItem.objects.create(category=category_political, title='واکنش باهنر به رد صلاحیت پزشکان، خردمندانه برخورد نکردند.')
    NewsItem.objects.create(category=category_political, title='انتقاد ابوترایی فرد، امام جمعه موقت تهران از رد صلاحیت ها')
    NewsItem.objects.create(category=category_political, title='حماس از بیمارستان الشفا به عنوان مرکز فرماندهی استفاده میکند.')
    # Create other news items for political category

    NewsItem.objects.create(category=category_economic, title='قیمت مسکن در ارزانترین منطقه تهران')
    NewsItem.objects.create(category=category_economic, title='قیمت جدید خوردروهای وارداتی')
    NewsItem.objects.create(category=category_economic, title='جنجالی که یک عکس به پا کرد، ماجرای اگزوز خودروی برقی ایرانی')
    NewsItem.objects.create(category=category_economic, title='فرمول محاسبه سنوات و عیدی ۱۴۰۲')
    # Create other news items for economic category

    NewsItem.objects.create(category=category_sports, title='ترکیب ایران مقابل کالدونیا مشخص شد.')
    NewsItem.objects.create(category=category_sports, title='شوک بزرگ به نکونام پیش از دربی پایتخت')
    NewsItem.objects.create(category=category_sports, title='بزرگ ترین غایب پرسپولیس در دیدار با النصر')
    NewsItem.objects.create(category=category_sports, title='رونالدو صد و بیست و هشتمین گلش را زد.')
    # Create other news items for economic sport

    NewsItem.objects.create(category=category_cultural, title='کشف یک موزاییک باستانی با طرحی شگفت انگیز در ترکیه')
    NewsItem.objects.create(category=category_cultural, title='افتتاح بزرگترین نیروگاه برق خورشیدی جهان در امارات')
    NewsItem.objects.create(category=category_cultural, title='آلودگی هوای تهران یک شنبه شدیدتر می شود.')
    NewsItem.objects.create(category=category_cultural, title='این سینا برای امروز ما چه حرفی برای گفتن دارد؟')
    # Create other news items for economic cultural

    return HttpResponse("Data creation process completed successfully")
