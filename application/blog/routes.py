from . import blog_api_blueprint
from flask import request, make_response, jsonify
from application.models import Post, Tag
from .. import db
from sqlalchemy import text


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
    

@blog_api_blueprint.route('/api/blog-post-raw-sql', methods=['GET'])
def blogpost_execute_raw_sql():
    idpost = request.args.get('idpost')
    if idpost:
        sql = """select * from post where id= :id"""
    else:
        sql = """select * from post"""
    
    result = db.session.execute(text(sql),{'id':idpost})
    lst = []
    for x in result:
        data = {}
        data['id'] = x.id
        data['title'] = x.title
        data['content'] = x.content
        lst.append(data)
        
    return jsonify(
        {
            'message':'request success',
            'count': len(lst),
            'data': lst
        }
    )
    


@blog_api_blueprint.route('/api/blog-post-pagination', methods=['GET'])
def blogpost_pagination():
    #/api/blog-post-pagination?page=1&per_page=2
    
    #query params
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    post_list = Post.query.paginate(page=page, per_page=per_page)
    
    results = {
        "results": [{"id": b.id, "title":b.title, "content":b.content} for b in post_list],
        "pagination": {
            "count": post_list.total,
            "page": page,
            "per_page": per_page,
            "pages": post_list.pages
        }
    }
    
    return jsonify(results)