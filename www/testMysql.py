import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    
    u1 = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    u2 = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    u3 = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')
    b = Blog(user_id='id_zhougongjin52', user_name='zhougongjin52', user_image='about:blank', name='This is a Blog', summary='Blog', content='blog')
    c = Comment(blog_id='id_blog', user_id='id_longchengfeijiang', user_name='longchengfeijiang', user_image='comment_image', content='comment')
    
    await u1.save()
    await u2.save()
    await u3.save()    
    await b.save()
    await c.save()
    
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	loop.run_forever()