from robodk import robolink  # RoboDK API
from robodk import robomath  # Robot toolbox
from robodk.robolink import ITEM_TYPE_ROBOT  # Import ITEM_TYPE_ROBOT explicitly

# Initialize RoboDK link
RDK = robolink.Robolink()

# Get the robot item
robot = RDK.Item('ABB CRB 1300-7/1.4', ITEM_TYPE_ROBOT)

# Define the Tool Frame [X, Y, Z, Rx, Ry, Rz] (replace with your actual tool frame values)
tool_frame = [50.103, -0.005, 66.801, 1.077, 51.542, 0.890]

# Create tool pose using robomath.Mat
tool_pose = robomath.Mat([
    [1, 0, 0, tool_frame[0]],
    [0, 1, 0, tool_frame[1]],
    [0, 0, 1, tool_frame[2]],
    [0, 0, 0, 1]
])

joint_limits_min = [-180, -95, -210, -230, -130, -242]  # min limits
joint_limits_max = [180, 155, 69, 230, 130, 242]        # max limits

def check_joint_limits(joint_positions):
    """Check if joint positions are within the robot's limits."""
    for i in range(len(joint_positions)):
        if not (joint_limits_min[i] <= joint_positions[i] <= joint_limits_max[i]):
            print(f"Joint {i+1} is out of limits: {joint_positions[i]} (limit: {joint_limits_min[i]} to {joint_limits_max[i]})")
            return False
    return True

if robot.Valid():
    print("Robot selected:", robot.Name())

    # Define joint positions
    joint_positions = [
        [0.000000, -0.000001, 0.000001, 0.000000, 0.000000, 0.000000],  # Home
        [-180.000000, -25.000001, 10.000001, -30.000004, 24.999990, 119.999999],  # Rotate_left
        # Pick 1
        [-172.000000, 29.999999, -9.999999, 150.000003, -14.999981, 30.000001],  # P1
        [-172.027606, 30.541225, -9.746584, 147.617661, -12.976729, 35.648119],  # P2
        [-172.000000, 29.999999, -9.999999, 150.000003, -14.999981, 30.000001],  # P1
        # Place 1
        [-180.000000, -25.000001, 10.000001, -29.999998, 24.999990, 210.000000],  # P3
        [-79.999999, -25.000002, 10.000001, -30.000003, 29.999990, 210.000007],  # P4
        [-80.028949, 11.679187, -16.469431, -12.515879, 40.881675, 195.285576],  # P5
        [-79.113367, 7.398772, 18.041420, -50.347643, 13.442762, 238.468402],  # P6
        [-80.028949, 11.679187, -16.469431, -12.515879, 40.881675, 195.285576],  # P5
        # Pick 2
        [-179.000000, 28.499999, -9.999999, 175.000001, -12.499977, 5.000000],  # P7
        [-178.892384, 29.529134, -8.310241, 174.092599, -10.390650, 6.131107],  # P8
        [-179.000000, 28.499999, -9.999999, 175.000001, -12.499977, 5.000000],  # P7
        # Place 2
        [-180.000000, -25.000001, 10.000001, -29.999998, 24.999990, 210.000000],  # P9
        [-79.999999, -25.000002, 10.000001, -30.000003, 29.999990, 210.000007],  # P10
        [-90.000000, 9.999999, -15.000000, 0.000000, 39.999996, 180.000000],  # P11
        [-91.280359, 5.969692, 19.679799, 18.547817, 8.304432, 161.881535],  # P12
        [-90.000000, 9.999999, -15.000000, 0.000000, 39.999996, 180.000000],  # P11
        # Pick 3
        [80.000000, -25.000001, 9.990000, -29.989998, 29.989993, 209.989999],  # P13
        [174.000000, 30.999999, -12.999999, 20.999998, 14.999981, 157.999999],  # P14
        [174.738137, 29.951769, -8.920101, 22.487639, 11.471782, 154.899948],  # P15
        [174.000000, 30.999999, -12.999999, 20.999998, 14.999981, 157.999999],  # P14
        [80.000000, -25.000001, 9.990000, -29.989998, 29.989993, 209.989999],  # P13
        # Place 3
        [-80.000000, -25.000003, 9.999998, -29.999976, 29.999990, 209.999979],  # P16
        [-84.496705, -5.763267, 1.429012, -7.067662, 39.673016, 188.613850],  # P17
        [-84.815480, -7.135253, 31.083859, -20.976598, 11.931740, 203.540385],  # P18
        [-84.496705, -5.763267, 1.429012, -7.067662, 39.673016, 188.613850],  # P17
        # Blow
        [-86.590000, 24.679999, -53.149999, -3.110000, 63.539996, 0.000000],  # B1
        [-72.153862, -15.031087, 6.337767, -20.125911, 46.822646, 21.193120],  # B2
        [-78.305176, 19.598204, -29.475972, -13.286900, 46.209467, 12.706940],  # B3
        [-81.100350, 18.578135, -28.160293, -10.235247, 45.345483, 8.313736],  # B4
        [-76.311567, -16.347431, 7.348706, -15.652494, 45.836489, 14.945879],  # B5
        [-84.247319, -17.833462, 8.454246, -6.677042, 44.687966, 4.014742],  # B6
        [-86.294183, 17.458888, -26.739118, -4.311581, 44.395975, 1.161817],  # B7
        [-84.247319, -17.833462, 8.454246, -6.677042, 44.687966, 4.014742],  # B6
        [-76.311567, -16.347431, 7.348706, -15.652494, 45.836489, 14.945879],  # B5
        [-81.100350, 18.578135, -28.160293, -10.235247, 45.345483, 8.313736],  # B4
        [-78.305176, 19.598204, -29.475972, -13.286900, 46.209467, 12.706940],  # B3
        [-72.153862, -15.031087, 6.337767, -20.125911, 46.822646, 21.193120],  # B2
        [-86.590000, 24.679999, -53.149999, -3.110000, 63.539996, 0.000000],  # B1
        # Home
        [0.000000, -0.000001, 0.000001, 0.000000, 0.000000, 0.000000],  # Home
    ]

    # Move robot through joint positions
    for i, pos in enumerate(joint_positions):
        print(f"\n Moving to joint position {i+1}: {pos}")
        if check_joint_limits(pos):
            robot.MoveJ(pos)

            # Set the robot to the specified joint position
            robot.setJoints(pos)
            # # Forward Kinematics: Solve FK with the current joint positions
            H_tcp_wrt_frame = robot.SolveFK(pos)
            # # Adjust to include the tool offset
            TCP_pose = robot.PoseTool() #to get pose relative to TCP
            tcp_pose_with_tool = H_tcp_wrt_frame * robot.PoseTool()
            # # Inverse Kinematics: Solve IK from the calculated TCP pose
            print("TCP Pose with Tool Offset (H_tcp_wrt_frame):")
            print(tcp_pose_with_tool)
            # Forward Kinematics: Solve FK with the current joint positions
            H_tcp_wrt_frame = robot.SolveFK(pos)
            # Directly use the FK result without adjusting for tool offset
            tcp_pose_without_tool = H_tcp_wrt_frame
            # Inverse Kinematics: Solve IK from the calculated TCP pose
            calculated_joints = robot.SolveIK(tcp_pose_without_tool)
            print("Calculated Joints from Pose without Tool:")
            print(calculated_joints)
            # All IK Solutions: Get all possible solutions for the given TCP pose
            # all_solutions = robot.SolveIK_All(tcp_pose_with_tool)
            all_solutions = robot.SolveIK_All(tcp_pose_without_tool)
            print("All IK Solutions:")
            for solution in all_solutions:
                print(solution)
else:
    print("Robot not found.")
