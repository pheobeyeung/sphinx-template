### get\_forward\_kin(q=’current\_joint\_positions’, tcp=’active\_tcp’)

Calculate the forward kinematic transformation (joint space -> tool space) using the calibrated robot kinematics. If no joint position vector is provided the current joint angles of the robot arm will be used. If no tcp is provided the currently active tcp of the controller will be used.

**Parameters**

`q:` joint position vector (Optional)

`tcp:` tcp offset pose (Optional)

**Return Value**

tool pose

**Example command:** `get_forward_kin([0.,3.14,1.57,.785,0,0], p[0,0,0.01,0,0,0])`

*   Example Parameters:
    *   q = \[0.,3.14,1.57,.785,0,0\] -> joint angles of j0=0 deg, j1=180 deg, j2=90 deg, j3=45 deg, j4=0 deg, j5=0 deg.
    *   tcp = p\[0,0,0.01,0,0,0\] -> tcp offset of x=0mm, y=0mm, z=10mm and rotation vector of rx=0 deg., ry=0 deg, rz=0 deg.