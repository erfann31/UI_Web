from django.http import HttpResponse
from django.shortcuts import render

from t11.models import Ad, MenuItem, Context, CarouselItem, NewsCategory, NewsItem, ContextColumn, NavButton, Box


def main_view(request):
    all_categories = NewsCategory.objects.all()
    carousel_items = CarouselItem.objects.all()
    columns = ContextColumn.objects.all()
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    ad = Ad.objects.first()
    return render(request, 'main.html', {'all_categories': all_categories, 'carousel_items': carousel_items, 'columns': columns, 'menu_items': menu_items, 'ad': ad, })


def search_view(request):
    return render(request, 'search.html')


def delete_data(request):
    MenuItem.objects.all().delete()
    CarouselItem.objects.all().delete()
    Context.objects.all().delete()
    NewsItem.objects.all().delete()
    NewsCategory.objects.all().delete()
    ContextColumn.objects.all().delete()
    NavButton.objects.all().delete()
    Box.objects.all().delete()
    Ad.objects.all().delete()
    return HttpResponse("Data deleted successfully")


def create_data(request):
    # Create the Ad
    ad = Ad.objects.create(image_path='images/ads.gif')
    # Create the main menu items
    home = MenuItem.objects.create(title='خانه')
    news = MenuItem.objects.create(title='اخبار')
    archive = MenuItem.objects.create(title='آرشیو')
    about_us = MenuItem.objects.create(title='درباره ما')
    contact_us = MenuItem.objects.create(title='ارتباط با ما')
    login = MenuItem.objects.create(title='ورود به باشگاه خبرنگاران', onclick_function='openPopup()')
    search = MenuItem.objects.create(title='', link='/search', class_name='search-icon')

    # Create submenu items and relate them to their parent items
    political = MenuItem.objects.create(title='سیاسی', parent=news)
    social = MenuItem.objects.create(title='اجتماعی', parent=news)
    sports = MenuItem.objects.create(title='ورزشی', parent=news)
    economic = MenuItem.objects.create(title='اقتصادی', parent=news)
    football = MenuItem.objects.create(title='فوتبال', parent=sports)
    volleyball = MenuItem.objects.create(title='والیبال', parent=sports)
    basketball = MenuItem.objects.create(title='بسکتبال', parent=sports)
    economic = MenuItem.objects.create(title='اقتصادی', parent=sports)
    # ----------------------------------------------
    # Create ContextColumns
    column1 = ContextColumn.objects.create(column_id='column1')
    column2 = ContextColumn.objects.create(column_id='column2')
    column3 = ContextColumn.objects.create(column_id='column3')

    # Create NavButtons for each column

    button_column1 = NavButton.objects.create(
        column=column1,
        button_id='button-column1',
        button_text='نگاه ویژه',
        onclick_function='showColumn("column1")',
        is_active = True,
    )
    button_column2 = NavButton.objects.create(
        column=column2,
        button_id='button-column2',
        button_text='پربازدید',
        onclick_function='showColumn("column2")'
    )
    button_column3 = NavButton.objects.create(
        column=column3,
        button_id='button-column3',
        button_text='دیدنی ها',
        onclick_function='showColumn("column3")'
    )

    # Create Contexts for each column
    context_column1 = Context.objects.create(column=column1, context_id='column1')
    context_column2 = Context.objects.create(column=column2, context_id='column2', display_style='none')
    context_column3 = Context.objects.create(column=column3, context_id='column3', display_style='none')

    # Create Boxes for each context
    context_column1_items = [
        Box.objects.create(
            context=context_column3,
            box_type='triangleImage',
            image='images/malake.jpeg',
            text='(ویدئو) ملکه انگلیس به یک بچه فیل شیر داد',
        ),
        Box.objects.create(
            context=context_column3,
            box_type='triangleImage',
            image='images/police.jpg',
            text='(ویدئو) تعقیب و گریز پلیس با هامر سرقتی؛تلاش برای سرفت دو خودروی دیگر!',
        ), Box.objects.create(
            context=context_column3,
            box_type='triangleImage',
            image='images/akasi.jpg',
            text='(تصاویر) برندگان مسابقه عکاسی از سگ‌ها در سال ۲۰۲۳',
        ), Box.objects.create(
            context=context_column3,
            box_type='triangleImage',
            image='images/israel.jpg',
            text='(تصاویر) اسرائيل اردوگاه جبالیا را روی سر صدها فلسطینی خراب کرد',
        ), Box.objects.create(
            context=context_column3,
            box_type='triangleImage',
            image='images/koshti.jpg',
            text='(ویدئو) مدرسه کشتی دختران؛تابوشکنی دختران',
        ),
    ]

    context_column2_items = [
        Box.objects.create(
            context=context_column1,
            box_type='circularImage',
            image='images/gid.jpg',
            text='امریکا، ایران و خطر یک جنگ گسترده‌تر در خاورمیانه؟<br>گیدئون راچمن',
        ),
        Box.objects.create(
            context=context_column1,
            box_type='circularImage',
            image='images/pol.jfif',
            text='به این دلایل جنگ زمینی اسرائيل در غزه خوب پیش نخواهد رفت<br>پل راجرز',
        ), Box.objects.create(
            context=context_column1,
            box_type='circularImage',
            image='images/arash.jpg',
            text='ترس و اضطراب می‌تواند کمک کند؛ چگونه از آن به نفع خود استفاده کنیم؟<br>آرش جوانبخت',
        ), Box.objects.create(
            context=context_column1,
            box_type='circularImage',
            image='images/hamid.jpg',
            text='چگونه غرب در تلاش برای «اختراع مجدد اسرائیل» است؟<br>حمید دباشی',
        ),
    ]

    context_column3_items = [
        Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='سپهر حیدری یک سال محروم شد.',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='توضیح رییس دانشگاه تهران درباره درگیری با دانشجویان',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='وام مسکن ایثارگران 600 میلیون تومان شد',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='اختراع شگفت انگیز دانشمندان ایرانی در آمریکا',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='آمریکا در تله انفجاری غزه چه خواهد کرد؟',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='پشت پرده پام 300 میلیونی بانک ملی',
        ), Box.objects.create(
            context=context_column2,
            image='',
            box_type='onlyTextBox',
            text='رتبه آخر پرسپولیس در آسیا، کمترین فرصت گل',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='این پرسپولیسی مرد اول سینمای ایران شد',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='گران ترین ساعت دنیا به رونالدو رسید',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='طوفان برقی قدرتمند',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='جنگ خندق در قرن 21',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='پیش بینی قیمت بیت کوین',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='خداحافظی حسن یزدانی از کشتی',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='ایران باید با طالبان چه کند؟',
        ), Box.objects.create(
            context=context_column2,
            box_type='onlyTextBox',
            text='چرا رشد اقتصادی چین منافع آمریکا را تهدید خواهد کرد؟',
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
