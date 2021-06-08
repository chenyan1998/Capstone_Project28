from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.routing import request_response
import uvicorn
app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort: Optional[str]= None):
    
    if published:
        return {'data': f'{limit} blogs from the list haha'}
    else:
        return {'data': 'denied'}
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):
    # getch blog with id =id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return limit
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title : str
    body: str
    published_at:Optional[bool]



@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"blog is created with title as {blog.title}"}

# if __name__ == "__main__" :
#    uvicorn.run(app,host='127.0.0.1',port='9000')
