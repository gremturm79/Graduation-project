from .forms import ThreadForm, ReplyForm, CategoryForm
from .models import Thread, Category, Reply


def content(request, pk):
    custom = request.user
    cat = Category.objects.all()
    # cat = custom.thread_set.get()
    # print(cat)
    message = Thread.objects.get(id=pk)
    # response = Reply.objects.get(id=pk)
    response = message.reply_set.all()
    form = ThreadForm()
    reply = ReplyForm()
    context = {
        'category': cat,
        'reply': reply,
        'form': form,
        'message': message,
        'response': response
    }
    return context
