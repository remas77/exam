
from django.http import Http404
from django.shortcuts import redirect, render
from .models import Developer, Game, Member
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
def search(request):
    query = request.GET.get('q')  # الحصول على قيمة البحث
    results = Member.objects.filter(firstname__icontains=query) if query else []
    return render(request, 'lap/search.html', {'results': results, 'query': query})
def add_member(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')  # الحصول على الاسم الأول
        lastname = request.POST.get('lastname')    # الحصول على الاسم الأخير # إنشاء وحفظ عضو جديد
        if firstname and lastname:
            Member.objects.create(firstname=firstname, lastname=lastname)
            return redirect('add_member')  # إعادة توجيه إلى نفس الصفحة بعد الإضافة

    return render(request, 'lap/add_member.html')

def list_members(request):
    members = Member.objects.all()  # استرجاع جميع الأعضاء من قاعدة البيانات
    return render(request, 'lap/list_members.html', {'members': members})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)  # استرجاع العضو المطلوب
    member.delete()  # حذف العضو
    return redirect('list_members')  # إعادة توجيه إلى صفحة قائمة الأسماء
def delete_member(request, member_id):
    try:
        member = Member.objects.get(id=member_id)  # العثور على العضو
        member.delete()  # حذف العضو
        return redirect('members_list')  # إعادة توجيه إلى صفحة الأعضاء بعد الحذف
    except Member.DoesNotExist:
        raise Http404("Member not found")  # في حال كان العضو غير موجود

def list_members(request):
    members = Member.objects.all()  # جلب جميع الأعضاء
    deleted = False  # متغير لتحديد إذا تم الحذف

    if request.method == 'POST':
        member_id = request.POST.get('member')  # الحصول على الـ ID من النموذج
        if member_id:
            try:
                member = Member.objects.get(id=member_id)  # العثور على العضو
                member.delete()  # حذف العضو
                deleted = True  # تعيين المتغير إلى True بعد الحذف
            except Member.DoesNotExist:
                pass  # في حال لم يتم العثور على العضو

    return render(request, 'lap/list_members.html', {'members': members, 'deleted': deleted})
def home(request):
    return render(request, 'lap/home.html')
def list_games(request):
    games = Game.objects.select_related('developer').all()
    return render(request, 'lap/list_games.html', {'games': games})

def add_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        developer_id = request.POST.get('developer')
        if title and developer_id:
            developer = Developer.objects.get(id=developer_id)
            Game.objects.create(title=title, developer=developer)
            return redirect('list_games')
    developers = Developer.objects.all()
    return render(request, 'lap/add_game.html', {'developers': developers})
def list_games(request):
    games = Game.objects.all()
    query = request.GET.get('q')
    if query:
        games = games.filter(title__icontains=query)
    return render(request, 'lap/list_games.html', {'games': games})
#def edit_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        developer_id = request.POST.get('developer')
        if title and developer_id:
            developer = Developer.objects.get(id=developer_id)
            game.title = title
            game.developer = developer
            game.save()
            return redirect('list_games')
    developers = Developer.objects.all()
    return render(request, 'lap/edit_game.html', {'game': game, 'developers': developers})
def delete_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('list_games')
    return render(request, 'lap/delete_game.html', {'game': game})
def search_games(request):
    query = request.GET.get('q', '')
    results = Game.objects.filter(title__icontains=query) if query else []
    return render(request, 'lap/search_games.html', {'results': results, 'query': query})
def edit_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        developer_id = request.POST.get('developer')
        if title and developer_id:
            developer = Developer.objects.get(id=developer_id)
            game.title = title
            game.developer = developer
            game.save()
            return redirect('list_games')
    developers = Developer.objects.all()
    return render(request, 'lap/edit_game.html', {'game': game, 'developers': developers})
