from django.shortcuts import render

#def post_list(request):
#        return render(request, 'blog/post_list.html', {})
def ex_css_1(request):
        return render(request, 'css/ex_css_1.html', {})
def ex_css_2(request):
        return render(request, 'css/ex_css_2.html', {})
def ex_css_3(request):
        return render(request, 'css/ex_css_3.html', {})
def index(request):
        return render(request, 'blog/index.html', {})
def page_html(request):
        return render(request, 'blog/page_html.html', {})
def page_op(request):
        return render(request, 'blog/page_op.html', {})
def page_vc(request):
        return render(request, 'blog/page_vc.html', {})
