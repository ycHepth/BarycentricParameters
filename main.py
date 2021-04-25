import sympybotics
import sympy

rbtdef = sympybotics.RobotDef('Example Robot', [(0, 0, 0, 'q'),  # (alpha, a, d, theta)
                                                (0, 0.1, 0, 'q')],
                              dh_convention='modified')

# rbtdef.frictionmodel = {'Coulomb', 'viscous'}
rbtdef.gravityacc = sympy.Matrix([0.0, -9.81, 0.0])

print(rbtdef.dynparms())

rbt = sympybotics.RobotDynCode(rbtdef, verbose = True)

tau_str = sympybotics.robotcodegen.robot_code_to_func('C', rbt.invdyn_code, 'tau_out', 'tau', rbtdef)

# print(tau_str)

rbt.calc_base_parms()
rbt.dyn.baseparms
print('Base Parms: ' , rbt.dyn.baseparms)
# TODO: Notice the basic parms are BaryCentric Parameters: l_1x = m1 * lc1; L_1zz = Izz1 + m1 * lc1 * lc1

rbt.Hb_code

Yr = sympybotics.robotcodegen.robot_code_to_func('C', rbt.Hb_code, 'H', 'Hb_code',rbtdef)
# print(Yr)

data=open("data.txt",'w+')
print(rbt.dyn.dynparms,tau_str,Yr,rbt.dyn.baseparms,file=data)
data.close()

