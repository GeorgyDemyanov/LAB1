import gmsh
import math
import os
gmsh.initialize()
path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'tor.stl'))
angle = 1
forceParametrizablePatches = False
includeBoundary = True
curveAngle = 180
gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)
gmsh.model.mesh.createGeometry()
s = gmsh.model.getEntities(3)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])
gmsh.model.geo.synchronize()
gmsh.fltk.run()
gmsh.finalize()


