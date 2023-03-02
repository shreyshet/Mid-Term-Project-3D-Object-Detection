# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 
from student.trackmanagement import Track

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dim_state = params.dim_state
        F = np.identity(dim_state)
        dt = params.dt
        j = int(dim_state/2)
        for i in range(j):
            F[i][i+j] = dt
        return np.matrix(F)
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        q = params.q**2
        dt = params.dt
        dim_state = params.dim_state
        pos_dim = int(dim_state/2)
        
        q1 = ((dt**3)/3) * q 
        q2 = ((dt**2)/2) * q
        q3 = dt * q
        
        a1 = q1*np.identity(pos_dim)
        a2 = q2*np.identity(pos_dim)
        a3 = q3*np.identity(pos_dim)
        
        Q = np.vstack((np.hstack((a1,a2)),np.hstack((a2,a3))))

        return Q
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        x = track.x
        P = track.P
        F = self.F()
        x = F*x # state prediction
        P = F*P*F.transpose() + self.Q() # covariance prediction
        track.set_x(x)
        track.set_P(P)
        pass
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        x = track.x
        P = track.P
        z = meas.z
        R = meas.z
        H = meas.sensor.get_H(x)
        
        gamma = self.gamma(track, meas)
        S = self.S(track, meas, H)
        
        K = P*H.transpose()*np.linalg.inv(S) # Kalman gain
        x = x + K*gamma # state update
        I = np.identity(params.dim_state)
        P = (I - K*H) * P
        
        track.set_x(x)
        track.set_P(P)
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        x = track.x
        z = meas.z
        Hx= meas.sensor.get_hx(x)
        gamma = z - Hx
        return gamma
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        x = track.x
        P = track.P
        R = meas.R
        S = H*P*H.transpose() + R
        return S
        
        ############
        # END student code
        ############ 