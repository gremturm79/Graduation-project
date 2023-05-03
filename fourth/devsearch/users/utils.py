from .models import Profile, Skill
from django.db.models import Q # Q класс работает как условие or при поиске filter


def search_profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skill = Skill.objects.filter(name__iexact=search_query)  # iexact если необходимо точное совпадение с запросом

    profile = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query)
                                                | Q(skill__in=skill))
    #  skill__in в данном случае работает как skill_set
    # регистронезависимый поиск icontains
    # при пустой строке из модели Profile берутся все данные
    return profile, search_query
