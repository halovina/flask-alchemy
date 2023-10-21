from . import blog_api_blueprint
from flask import request, make_response, jsonify
from application.models import Post, Tag
from .. import db


@blog_api_blueprint.route('/api/blog-post/create', methods=['POST'])
def blog_post():
    title = request.json['title']
    content = request.json['content']
    tags = request.json['tags'] #['test','coba']
    
    blog_post = Post(
        title = title,
        content = content
    )
    
    for n in tags:
        tag_n = Tag(name=n)
        blog_post.tags.append(tag_n)
        db.session.add(tag_n)
        
    db.session.add(blog_post)
    
    #commit 
    db.session.commit()
    
    return jsonify(
        {
            "message":"blog post added"
        }
    )
    

@blog_api_blueprint.route('/api/blog-post', methods=['GET'])
def blogpost_getlistdata():
    blog_post = Post.query.all()
    lst = []
    for bl in blog_post:
        data = {}
        data['title'] = bl.title
        data['content'] = bl.content
        
        tag_list = [] #['tag1','tag2']
        for tg in bl.tags:
            tag_list.append(tg.name)
            
        data['tags'] = tag_list
        lst.append(data)
        
    return jsonify(
        {
            'message':'request success',
            'count': len(lst),
            'data': lst
        }
    )
        