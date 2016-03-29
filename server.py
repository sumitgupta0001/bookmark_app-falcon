import falcon
from bookmarks import *

api= falcon.API()



api.add_route('/', firstPage())
api.add_route('/register', registration())
api.add_route('/login', login())
api.add_route('/bookmark1/{uid}',bookmark1())
api.add_route('/delete/{uid}',delete())
api.add_route('/add_bookmark/{uid}',add_bookmark())
api.add_route('/views/{uid}',views())
api.add_route('/remove/{uid}/{aa}',remove())
api.add_route('/export/{uid}',export())
api.add_route('/edit/{uid}/{aa}',edit())
api.add_route('/import_file/{uid}',import_file())
api.add_route('/logout/{uid}', logout())
