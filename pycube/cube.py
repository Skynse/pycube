from pyglet.gl import *
import pyglet
from pyglet.window import key
from OpenGL.GLUT import *


class Cube(pyglet.window.Window):
    xRotation = yRotation = 30 

    def __init__(self, width, height, title=''):
        super(Cube, self).__init__(width, height, title)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)  
        
    def on_draw(self):
        self.clear() 
        glPushMatrix()
         
        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_QUADS)

        glColor3ub(255, 255, 255)
        glVertex3f(50,50,50)

        glColor3ub(255, 255, 0)
        glVertex3f(50,-50,50)

        glColor3ub(255, 0, 0)
        glVertex3f(-50,-50,50)
        glVertex3f(-50,50,50)

        glColor3f(0, 0, 1)
        glVertex3f(-50,50,-50)

        glEnd()

        # Pop Matrix off stack
        glPopMatrix()

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= 5
        elif motion == key.DOWN:
            self.xRotation += 5
        elif motion == key.LEFT:
            self.yRotation -= 5
        elif motion == key.RIGHT:
            self.yRotation += 5
    
    def on_resize(self, width, height):
       # set the Viewport
       glViewport(0, 0, width, height)

       # using Projection mode
       glMatrixMode(GL_PROJECTION)
       glLoadIdentity()

       aspectRatio = width / height
       gluPerspective(35, aspectRatio, 1, 1000)

       glMatrixMode(GL_MODELVIEW)
       glLoadIdentity()
       glTranslatef(0, 0, -400)

    def run(self):
        pyglet.app.run()
