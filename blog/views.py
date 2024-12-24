from django.shortcuts import render, redirect
from blog import forms 
from . import models
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def index(request):
	photos = models.Photo.objects.order_by('?')
	blogs = models.Blog.objects.order_by('?')
	return render(request, 'index.html', {'photos': photos, 'blogs': blogs })
  	
@login_required
def blog(request):
    blogs = models.Blog.objects.order_by('?')
    return render(request, 'blog.html', {'blogs': blogs })
@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'view_blog.html', {'blog': blog})



@login_required
def create_multiple_photos(request):

    PhotoFormSet = formset_factory(forms.PhotoForm, extra=3)

    formset = PhotoFormSet()

    if request.method == 'POST':

        formset = PhotoFormSet(request.POST, request.FILES)

        if formset.is_valid():

            for form in formset:

                if form.cleaned_data:

                    photo = form.save(commit=False)

                    photo.uploader = request.user

                    photo.save()

            return redirect('index')

    return render(request, 'create_multiple_photos.html', {'formset': formset})
	
@login_required
def edit_photo(request, photo_id):

    photo = get_object_or_404(models.Photo, id=photo_id)

    edit_form = forms.PhotoForm(instance=photo)

    delete_form = forms.DeletePhotoForm()

    if request.method == 'POST':

        if 'edit_photo' in request.POST:

            edit_form = forms.PhotoForm(request.POST, request.FILES, instance=photo)

            if edit_form.is_valid():

                edit_form.save()

                return redirect('index')
        if 'delete_photo' in request.POST:
            delete_form = forms.DeletePhotoForm(request.POST)
            if delete_form.is_valid():
                photo.delete()
                return redirect('index')

    context = {

        'edit_form': edit_form,

        'delete_form': delete_form,

}

    return render(request, 'edit_photo.html', context=context)

@login_required
def create_multiple_blogs(request):

    BlogFormSet = formset_factory(forms.BlogForm, extra=3)

    formset = BlogFormSet()

    if request.method == 'POST':

        formset = BlogFormSet(request.POST, request.FILES)

        if formset.is_valid():

            for form in formset:

                if form.cleaned_data:

                    blog = form.save(commit=False)

                    blog.uploader = request.user

                    blog.save()

            return redirect('index')

    return render(request, 'create_multiple_blogs.html', {'formset': formset})


@login_required
def edit_blog(request, blog_id):

    blog = get_object_or_404(models.Blog, id=blog_id)

    edit_form = forms.BlogForm(instance=blog)

    delete_form = forms.DeleteBlogForm()

    if request.method == 'POST':

        if 'edit_blog' in request.POST:

            edit_form = forms.BlogForm(request.POST, request.FILES, instance=blog)

            if edit_form.is_valid():

                edit_form.save()

                return redirect('index')
        if 'delete_blog' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('index')

    context = {

        'edit_form': edit_form,

        'delete_form': delete_form,

}

    return render(request, 'edit_blog.html', context=context)


