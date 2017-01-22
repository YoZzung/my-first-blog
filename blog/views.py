from django.shortcuts import render

def post_list(request):
        return render(request, 'blog/post_list.html', {})
def ex_css_1(request):
        return render(request, 'css/ex_css_1.html', {})
