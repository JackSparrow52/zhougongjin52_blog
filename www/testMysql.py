import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    b = Blog(user_id='id_zhougongjin52', user_name='zhougongjin52', user_image='about:blank', name='This is a Blog', summary='Blog', content='blog')
    c = Comment(blog_id='id_blog', user_id='id_longchengfeijiang', user_name='longchengfeijiang', user_image='comment_image', content='comment')
    
    await u.save()
    await b.save()
    await c.save()
    
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	loop.run_forever()