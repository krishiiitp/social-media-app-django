from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Profile, Post, LikePost, Followers
from django.contrib.auth.decorators import login_required
def signup(request):
 try:
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        if my_user is not None:
            login(request,my_user)
            return redirect('/')
        return redirect('/login')      
 except:
        invalid="User Already Exists!"
        return render(request, 'signup.html',{'invalid':invalid})   
 return render(request, 'signup.html')
def loginn(request):
  if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        invalid="Invalid Credentials"
        return render(request, 'loginn.html',{'invalid':invalid})       
  return render(request, 'loginn.html')

@login_required(login_url='/login')
def logoutt(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def upload(request):
    if request.method=='POST':
        user=request.user.username
        image=request.FILES.get('image_upload')
        caption=request.POST['caption']
        new_post=Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login')
def likes(request,id):
    if request.method=='GET':
        username=request.user.username
        post=get_object_or_404(Post,id=id)
        like_filter=LikePost.objects.filter(post_id=id,username=username).first()
        if like_filter is None:
            new_like=LikePost.objects.create(post_id=id,username=username)
            post.no_of_likes=post.no_of_likes + 1
        else:
            like_filter.delete()
            post.no_of_likes=post.no_of_likes - 1
        post.save()
        print(post.id)
        return redirect('/#'+id)

@login_required(login_url='/login')
def home_posts(request,id):
    post=Post.objects.get(id=id)
    profile=Profile.objects.get(user=request.user)
    context={
        'post':post,
        'profile':profile
    }
    return render(request,'main.html',context)

@login_required(login_url='/login')
def explore(request):
    post=Post.objects.all().order_by('-created_at')
    profile=Profile.objects.get(user=request.user)
    context={
        'post':post,
        'profile':'profile'
    }
    return render(request,'explore.html',context)

@login_required(login_url='/login')
def profile(request,id_user):
    user_object=User.objects.get(username=id_user)
    profile=Profile.objects.get(user=request.user)
    user_profile=Profile.objects.get(user=user_object)
    user_posts=Post.objects.filter(user=id_user).order_by('-created_at')
    user_post_length=len(user_posts)
    follower=request.user.username
    user=id_user
    if Followers.objects.filter(follower=follower,user=user):
        follow_unfollow='Unfollow'
    else:
        follow_unfollow='Follow'
    user_followers=len(Followers.objects.filter(user=id_user))
    user_following=len(Followers.objects.filter(follower=id_user))
    context={
        'user_object' : user_object,
        'user_profile' : user_profile,
        'user_posts' : user_posts,
        'user_post_length' : user_post_length,
        'follow_unfollow':follow_unfollow,
        'user_following' : user_following,
        'user_followers' : user_followers,
    }
    if request.user.username==id_user:
        if request.method=='POST':
            if request.FILES.get('image')==None:
                image=user_profile.profileimg
                bio=request.POST['bio']
                location=request.POST['location']
                user_profile.profileimg=image
                user_profile.bio=bio
                user_profile.location=location
                user_profile.save()
            if request.FILES.get('image')!=None:
                image=request.FILES.get('image')
                bio=request.POST['bio']
                location=request.POST['location']
                user_profile.profileimg=image
                user_profile.bio=bio
                user_profile.location=location
                user_profile.save()
            return redirect('/profile/'+id_user)
        else:
            return render(request,'profile.html',context)

    return render(request,'profile.html',context)

@login_required(login_url='/login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']
        follow_instance = Followers.objects.filter(follower=follower, user=user).first()

        if follow_instance:
            if follow_instance.status == 'pending':
                follow_instance.delete()
                return redirect('profile/' + user)
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('profile/' + user)
    else:
        return redirect('/')

@login_required(login_url='/login')
def handle_follow_request(request, request_id, action):
    follow_request = get_object_or_404(Followers, id=request_id)
    if action == 'accept':
        follow_request.status = 'accepted'
        follow_request.save()
    elif action == 'reject':
        follow_request.status = 'rejected'
        follow_request.save()
    return redirect('profile/' + follow_request.user)

@login_required(login_url='/login')
def search_results(request):
    query = request.GET.get('q')
    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)
    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'search_user.html', context)

@login_required(login_url='/login')
def home(request):
    post=Post.objects.all().order_by('-created_at')
    # profile=Profile.objects.get(user=request.user)
    context={
        'post' : post,
        # 'profile' : profile
    }
    return render(request,'main.html',context)
