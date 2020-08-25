import Rhino
import scriptcontext
import rhinoscriptsyntax as rs
import compas
import compas_rhino

from compas.datastructures import Mesh
from compas.utilities import XFunc
from compas_rhino.artists import meshartist

mesh = Mesh.from_obj(compas.get('faces.obj'))
vertices = mesh.get_vertices_attributes('xyz')
edges    = list(mesh.edges())
fixed    = list(mesh.vertices_where({'vertex_degree': 2}))
q        = mesh.get_edges_attribute('q', 1.0)
loads    = mesh.get_vertices_attributes(('px', 'py', 'pz'), (0.0, 0.0, 0.0))

xyz, q, f, l, r = XFunc('compas.numerical.fd_numpy')(vertices, edges, fixed, q, loads)

for key, attr in mesh.vertices(True):
    attr['x'] = xyz[key][0]
    attr['y'] = xyz[key][1]
    attr['z'] = xyz[key][2]

artist = MeshArtist(mesh)

artist.clear()

artist.draw_vertices()
artist.draw_edges()

artist.redraw()