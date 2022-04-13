import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

#Commented sections in green (with ''' ''') are for when we have all data
#naming convention: method, number of agents, size of grid, penalty, seed

methods = ['dicgcent', 'dicgdec', 'cent', 'dec']


#agents  = [8, 12]
#grid    = [8, 12]
#penalty = [0, n15]
#seed    = [1, 2, 3]


agents  = [8]
grid    = [8]
penalty = [0]
seed    = [1]


name_lst = []
avg_lst = []

for m in methods:
    for a in agents:
        for g in grid:
            for p in penalty:
                avg_lst.append(str(m+'_'+str(a)+'_'+str(g)+'_'+str(p)))
                for s in seed:
                    name_lst.append(str(m+'_'+str(a)+'_'+str(g)+'_'+str(p)+'_'+str(s)))


#4 env step
#13 avg return

for i in name_lst:
    #print(str('data/local/Junk/'+i+'/progress.csv'))
    data = np.genfromtxt(str('data/local/Junk/'+i+'/progress.csv'), delimiter=',', skip_header=1)
    globals()[str('env_step_'+i)] = data[:,4]
    globals()[str('avg_return_'+i)] = data[:,13]

#Calculate averages
#Ignore error: undefined name

'''avg_return_cent_8_8_0 = np.average((avg_return_cent_8_8_0_1,
                                    avg_return_cent_8_8_0_2,
                                    avg_return_cent_8_8_0_3), axis=0)

avg_return_cent_8_8_n15 = np.average((avg_return_cent_8_8_n15_1,
                                    avg_return_cent_8_8_n15_2,
                                    avg_return_cent_8_8_n15_3), axis=0)

avg_return_dec_8_8_0 = np.average((avg_return_dec_8_8_0_1,
                                    avg_return_dec_8_8_0_2,
                                    avg_return_dec_8_8_0_3), axis=0)

avg_return_dec_8_8_n15 = np.average((avg_return_dec_8_8_n15_1,
                                    avg_return_dec_8_8_n15_2,
                                    avg_return_dec_8_8_n15_3), axis=0)

avg_return_dicgcent_8_8_0 = np.average((avg_return_dicgcent_8_8_0_1,
                                    avg_return_dicgcent_8_8_0_2,
                                    avg_return_dicgcent_8_8_0_3), axis=0)

avg_return_dicgcent_8_8_n15 = np.average((avg_return_dicgcent_8_8_n15_1,
                                    avg_return_dicgcent_8_8_n15_2,
                                    avg_return_dicgcent_8_8_n15_3), axis=0)

avg_return_dicgdec_8_8_0 = np.average((avg_return_dicgdec_8_8_0_1,
                                    avg_return_dicgdec_8_8_0_2,
                                    avg_return_dicgdec_8_8_0_3), axis=0)

avg_return_dicgdec_8_8_n15 = np.average((avg_return_dicgdec_8_8_n15_1,
                                    avg_return_dicgdec_8_8_n15_2,
                                    avg_return_dicgdec_8_8_n15_3), axis=0)'''

avg_return_cent_8_8_0 = np.average((avg_return_cent_8_8_0_1,
                                    avg_return_cent_8_8_0_1,
                                    avg_return_cent_8_8_0_1), axis=0)

avg_return_dec_8_8_0 = np.average((avg_return_dec_8_8_0_1,
                                    avg_return_dec_8_8_0_1,
                                    avg_return_dec_8_8_0_1), axis=0)

avg_return_dicgcent_8_8_0 = np.average((avg_return_dicgcent_8_8_0_1,
                                    avg_return_dicgcent_8_8_0_1,
                                    avg_return_dicgcent_8_8_0_1), axis=0)

avg_return_dicgdec_8_8_0 = np.average((avg_return_dicgdec_8_8_0_1,
                                    avg_return_dicgdec_8_8_0_1,
                                    avg_return_dicgdec_8_8_0_1), axis=0)


#Plotting

fig, ax = plt.subplots()
ax.plot(env_step_cent_8_8_0_1, avg_return_cent_8_8_0,
        env_step_dec_8_8_0_1, avg_return_dec_8_8_0,
        env_step_dicgcent_8_8_0_1, avg_return_dicgcent_8_8_0,
        env_step_dicgdec_8_8_0_1, avg_return_dicgdec_8_8_0)

'''fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(env_step_cent_8_8_0_1, avg_return_cent_8_8_0,
        env_step_dec_8_8_0_1, avg_return_dec_8_8_0,
        env_step_dicgcent_8_8_0_1, avg_return_dicgcent_8_8_0,
        env_step_dicgdec_8_8_0_1, avg_return_dicgdec_8_8_0)

ax2.plot(env_step_cent_8_8_n15_1, avg_return_cent_8_8_n15,
        env_step_dec_8_8_n15_1, avg_return_dec_8_8_n15,
        env_step_dicgcent_8_8_n15_1, avg_return_dicgcent_8_8_n15,
        env_step_dicgdec_8_8_n15_1, avg_return_dicgdec_8_8_n15)
'''






















