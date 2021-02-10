from django.shortcuts import render, get_object_or_404
from .models import Post, Paper
from django.http import HttpResponse

def index(request):
    posts = Post.objects.filter(is_hidden=False)
    args = {'posts':posts}
    return render(request, 'blog/index.html', args)
    
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    papers = post.reference.all()
    args = {'post':post, 'papers':papers}
    return render(request, 'blog/detail.html', args)

def paper_download(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    content = open(paper.attachment.path, 'rb') 
    resp = HttpResponse(content.read(), content_type='application/pdf')
    resp['Content-Disposition'] = 'inline; filename=' + paper.title + '.pdf'
    return resp