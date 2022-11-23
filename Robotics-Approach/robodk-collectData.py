import pandas as pd
from datetime import datetime
from itertools import count
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox
import matplotlib.pyplot as plt
# The following 2 lines keep your code compatible with older versions or RoboDK:
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
### RoboDK Station Robot Joints angles data access and Data Dictionary ###----------------------&&&&&----------
def RoboDK():
    df = pd.DataFrame(columns=['DateTime','Time','theta1', 'theta2','theta3','theta4','theta5','theta6'])

    # Link to RoboDK
    RDK = robolink.Robolink()

    # Notify user:
    print('To edit this program:\n right click on the Python program, then, select "Edit Python script"')

    # Program example:
    print('Items in the station:')
    itemlist = RDK.ItemList()
    print(itemlist)
    robot = RDK.Item('Motoman GP7')
    if robot.Valid():
        print('Item selected: ' + robot.Name())
        print('Item position: ' + repr(robot.Pose()))

    # program = RDK.Item('Path-A-B')
    # program = RDK.Item('Path-A-C-B')
    # program = RDK.Item('Path-A-D-B')
    program = RDK.Item('Prog1')
    program.RunProgram()
    # program2 = RDK.Item('DoWeld')
    # program2.RunProgram()
    count = 0
    while program.Busy():

        robot_joints = robot.Joints().list()
        print('current robot joints:\n', robot.Joints())
        # joint1 = robot_joints[0]
        # joint2 = robot_joints[1]
        # joint3 = robot_joints[2]
        # joint4 = robot_joints[3]
        # joint5 = robot_joints[4]
        # joint6 = robot_joints[5]
        # print(joint1)
        # print(joint2)
        # print(joint3)
        # print(joint4)
        # print(joint5)
        # print(joint6)
        # print('current robot joints:\n', robot_joints[1])
        date_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        Current_time= datetime.now().strftime("%H:%M:%S")
        print(Current_time)
        robot_joints.insert(0, Current_time)
        robot_joints.insert(0, date_time)
        a_series = pd.Series(robot_joints, index = df.columns)
        df = df.append(a_series, ignore_index=True)
        # plt.figure(1,figsize=(8, 5),facecolor= 'lightgray')
        # ax1 = plt.subplot()
        # l1, = ax1.plot(df['theta1'],'o-', color='red',linewidth=2.0)
        # l2, = ax1.plot(df['theta2'],'.-', color='green',linewidth=2.0)
        # l3, = ax1.plot(df['theta3'],'x-', color='blue',linewidth=2.0)
        # l4, = ax1.plot(df['theta4'],'--', color='orange',linewidth=2.0)
        # l5, = ax1.plot(df['theta5'],'+-', color='purple',linewidth=2.0)
        # l6, = ax1.plot(df['theta6'],'*-', color='yellow',linewidth=2.0)
        # ax1.set_facecolor('black')
        # plt.legend(["th1", "th2", "th3", "th4", "th5", "th6"]) #"speed", "acceleration"
        # plt.title('Joint Angles Info',color='blue',fontsize=20)

        #-----------------------------------------------------------------------------------------
        plt.figure(1, figsize=(14, 6), facecolor='lightgray')  ## Note: (row*column*plot_no)
        plt.suptitle('GP7 Joints Information ', color='blue', fontsize=20)

        ax1 = plt.subplot(231)
        l1 = ax1.plot(df['theta1'], 'x-', color='red', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta1(deg)', fontsize=10)
        # ax1.set_xlim(0,80)
        ax1.set_facecolor('black')
        plt.legend(["J1-deg"])
        # plt.title('Joint1 angle', fontsize=10)

        ax1 = plt.subplot(232)
        l2 = ax1.plot(df['theta2'], 'o-', color='gray', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta2(deg)', fontsize=10)
        ax1.set_facecolor('black')
        plt.legend(["J2-deg"])
        # plt.title('Joint2 angle', fontsize=10)

        ax1 = plt.subplot(233)
        l3 = ax1.plot(df['theta3'], '.-', color='green', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta3(deg)', fontsize=10)
        ax1.set_facecolor('black')
        plt.legend(["J3-deg"])
        # plt.title('Joint3 angle', fontsize=10)

        ax1 = plt.subplot(234)
        l4 = ax1.plot(df['theta4'], '.-', color='orange', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta4(deg)', fontsize=10)
        ax1.set_facecolor('black')
        plt.legend(["J4-deg"])
        # plt.title('Joint4 angle', fontsize=10)

        ax1 = plt.subplot(235)
        l5 = ax1.plot(df['theta5'], '.-', color='blue', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta5(deg)', fontsize=10)
        ax1.set_facecolor('black')
        plt.legend(["J5-deg"])
        # plt.title('Joint5 angle', fontsize=10)

        ax1 = plt.subplot(236)
        l6 = ax1.plot(df['theta6'], '.-', color='purple', linewidth=2.0)
        ax1.set_xlabel('time [s]', fontsize=10)
        ax1.set_ylabel('theta6(deg)', fontsize=10)
        ax1.set_facecolor('black')
        plt.legend(["J6-deg"])
        # plt.title('Joint6 angle', fontsize=10)
        ###----------------------####--------------------&&&&&-----------------------------$$$$----------
        plt.pause(.01)
        time.sleep(0.001)
        count += 1
        print(count)
        if count == 100:
            break
    #### save data in various file format ####------------------&&&&------------------$$$$-------------
    df.to_csv('CollisionFreeTest-Joints.csv')

    #### Show plot ###-----------------------------------------&&&&&----------------$$$$---------------
    plt.show()

if __name__ == "__main__":
    RoboDK()