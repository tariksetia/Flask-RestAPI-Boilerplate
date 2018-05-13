from flask import request, url_for
from functools import wraps

def paginate(collection, max_per_page=25):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            #The route returns query cursor
            query = f(*args, **kwargs)

            #get page number and per page paremeteres from the url_string
            page = request.args.get('page',1,type=int)
            per_page = request.args.get('per_page',max_per_page,type=int)
            per_page = min(per_page,max_per_page)

            expanded = None
            if request.args.get('expanded',0,type=int) !=0 :
                expanded = 1

            p = query.paginate(page,per_page)
            
            pages = {'page':page, 'per_page':per_page,
                    'total':p.total, 'pages':p.pages}
            
            if p.has_prev:
                pages['prev_url'] = url_for(request.endpoint, page=p.prev_num, per_page=per_page, expanded=expanded, _external=True, **kwargs)
            else:
                pages['prev_url'] = None
            
            if p.has_next:
                pages['next_url'] = url_for(request.endpoint, page=p.next_num, per_page=per_page, expanded=expanded, _external=True, **kwargs)
            else:
                pages['next_url'] = None
            
            pages['first_url'] = url_for(request.endpoint, page=1, per_page=per_page, _external=True, **kwargs)
            pages['last_url'] = url_for(request.endpoint, page=p.pages, per_page=per_page, _external=True, **kwargs)
            if expanded:
                return {collection:[item.to_dict() for item in p.items],
                    'pages':pages}
            else:
                return {collection:[item.get_url() for item in p.items],
                        'pages':pages}
        
        return wrapped
    return decorator