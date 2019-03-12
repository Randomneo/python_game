class BaseGameObject(object):

    def __init__(self):
        self.is_drawable = True
        self.is_movable = False
        self.object_manager = None

    def destroy(self):
        if not self.object_manager:
            print('No object manager to destroy object')
        self.object_manager.destroy_object(self)
