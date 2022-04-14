import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
seed    = [1,2]


name_lst = []
avg_lst = []

for m in methods:
    for a in agents:
        for g in grid:
            for p in penalty:
                avg_lst.append(str(m+'_'+str(a)+'_'+str(g)+'_'+str(p)))
                for s in seed:
                    if s>1:
                        if a ==8 and g == 8:
                            name_lst.append(str(m+'_'+str(a)+'_'+str(g)+'_'+str(p)+'_'+str(s)))
                    else:
                        name_lst.append(str(m + '_' + str(a) + '_' + str(g) + '_' + str(p) + '_' + str(s)))

#4 env step
#13 avg return

for i in name_lst:
    #print(str('data/local/Junk/'+i+'/progress.csv'))
    data = pd.read_csv(str('data/local/'+i+'/progress.csv')) #, delimiter=',', skip_header=1)
    globals()[str('env_step_' + i)] = data['TotalEnvSteps'].to_numpy()
    globals()[str('avg_return_' + i)] = data['AverageReturn'].to_numpy()

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

avg_return_cent_8_8_0 = np.average((avg_return_cent_8_8_0_1,avg_return_cent_8_8_0_2,avg_return_cent_8_8_0_1), axis=0)
avg_return_dec_8_8_0 = np.average((avg_return_dec_8_8_0_1,avg_return_dec_8_8_0_2,avg_return_dec_8_8_0_1), axis=0)
avg_return_dicgcent_8_8_0 = np.average((avg_return_dicgcent_8_8_0_1,avg_return_dicgcent_8_8_0_2,avg_return_dicgcent_8_8_0_1), axis=0)
avg_return_dicgdec_8_8_0 = np.average((avg_return_dicgdec_8_8_0_1,avg_return_dicgdec_8_8_0_2,avg_return_dicgdec_8_8_0_1), axis=0)

std_cent_8_8_0 = np.std((avg_return_cent_8_8_0_1,avg_return_cent_8_8_0_2,avg_return_cent_8_8_0_1), axis=0)
std_dec_8_8_0 = np.std((avg_return_dec_8_8_0_1,avg_return_dec_8_8_0_2,avg_return_dec_8_8_0_1), axis=0)
std_dicgcent_8_8_0 = np.std((avg_return_dicgcent_8_8_0_1,avg_return_dicgcent_8_8_0_2,avg_return_dicgcent_8_8_0_1), axis=0)
std_dicgdec_8_8_0 = np.std((avg_return_dicgdec_8_8_0_1,avg_return_dicgdec_8_8_0_2,avg_return_dicgdec_8_8_0_1), axis=0)


#Plotting

#Reproductions
fig, ax = plt.subplots(1,2)#nrows=1, ncols=2)
ax[0].plot(env_step_cent_8_8_0_1/(10**6), avg_return_cent_8_8_0, label = 'CENT', color = 'orange')
ax[0].plot(env_step_dec_8_8_0_1/(10**6), avg_return_dec_8_8_0, label = 'DEC', color = 'green')
ax[0].plot(env_step_dicgcent_8_8_0_1/(10**6), avg_return_dicgcent_8_8_0, label = 'DICGCE', color = 'blue')
ax[0].plot(env_step_dicgdec_8_8_0_1/(10**6), avg_return_dicgdec_8_8_0,label = 'DICGDE', color = 'red')
ax[0].fill_between(env_step_cent_8_8_0_1/(10**6), avg_return_cent_8_8_0-2*std_cent_8_8_0,avg_return_cent_8_8_0+2*std_cent_8_8_0, color = 'orange', alpha = 0.5)
ax[0].fill_between(env_step_dec_8_8_0_1/(10**6), avg_return_dec_8_8_0-2*std_dec_8_8_0,avg_return_dec_8_8_0+2*std_dec_8_8_0, color = 'green', alpha = 0.5)
ax[0].fill_between(env_step_dicgcent_8_8_0_1/(10**6), avg_return_dicgcent_8_8_0-2*std_dicgcent_8_8_0,avg_return_dicgcent_8_8_0+2*std_dicgcent_8_8_0, color = 'blue', alpha = 0.5)
ax[0].fill_between(env_step_dicgdec_8_8_0_1/(10**6), avg_return_dicgdec_8_8_0-2*std_dicgdec_8_8_0,avg_return_dicgdec_8_8_0+2*std_dicgdec_8_8_0, color = 'red', alpha = 0.5)
ax[0].axhline(80, color = 'black',linestyle ='dashed')
ax[1].plot(env_step_cent_8_8_0_1/(10**6), avg_return_cent_8_8_0, label = 'CENT', color = 'orange')
ax[1].plot(env_step_dec_8_8_0_1/(10**6), avg_return_dec_8_8_0, label = 'DEC', color = 'green')
ax[1].plot(env_step_dicgcent_8_8_0_1/(10**6), avg_return_dicgcent_8_8_0, label = 'DICGCE', color = 'blue')
ax[1].plot(env_step_dicgdec_8_8_0_1/(10**6), avg_return_dicgdec_8_8_0,label = 'DICGDE', color = 'red')
ax[1].fill_between(env_step_cent_8_8_0_1/(10**6), avg_return_cent_8_8_0-2*std_cent_8_8_0,avg_return_cent_8_8_0+2*std_cent_8_8_0, color = 'orange', alpha = 0.5)
ax[1].fill_between(env_step_dec_8_8_0_1/(10**6), avg_return_dec_8_8_0-2*std_dec_8_8_0,avg_return_dec_8_8_0+2*std_dec_8_8_0, color = 'green', alpha = 0.5)
ax[1].fill_between(env_step_dicgcent_8_8_0_1/(10**6), avg_return_dicgcent_8_8_0-2*std_dicgcent_8_8_0,avg_return_dicgcent_8_8_0+2*std_dicgcent_8_8_0, color = 'blue', alpha = 0.5)
ax[1].fill_between(env_step_dicgdec_8_8_0_1/(10**6), avg_return_dicgdec_8_8_0-2*std_dicgdec_8_8_0,avg_return_dicgdec_8_8_0+2*std_dicgdec_8_8_0, color = 'red', alpha = 0.5)
ax[1].axhline(80, color = 'black',linestyle ='dashed')
ax[0].set_ylabel('Average Return')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[0].legend()
plt.show()

#
'''
#Grid
fig2, ax = plt.subplots(1,2)#nrows=1, ncols=2)
ax[0].plot(env_step_cent_8_12_0/(10**6), avg_return_cent_8_8_0, label = 'CENT', color = 'orange')
ax[0].plot(env_step_dec_8_12_0/(10**6), avg_return_dec_8_8_0, label = 'DEC', color = 'green')
ax[0].plot(env_step_dicgcent_8_12_0/(10**6), avg_return_dicgcent_8_8_0, label = 'DICGCE', color = 'blue')
ax[0].plot(env_step_dicgdec_8_12_0/(10**6), avg_return_dicgdec_8_8_0,label = 'DICGDE', color = 'red')
ax[0].axhline(80, color = 'black',linestyle ='dashed')
ax[1].plot(env_step_cent_8_12_n15/(10**6), avg_return_cent_8_12_n15, label = 'CENT', color = 'orange')
ax[1].plot(env_step_dec_8_12_n15/(10**6), avg_return_dec_8_12_n15, label = 'DEC', color = 'green')
ax[1].plot(env_step_dicgcent_8_12_n15/(10**6), avg_return_dicgcent_8_12_n15, label = 'DICGCE', color = 'blue')
ax[1].plot(env_step_dicgdec_8_12_n15/(10**6), avg_return_dicgdec_8_12_n15,label = 'DICGDE', color = 'red')
ax[1].axhline(80, color = 'black',linestyle ='dashed')
ax[0].set_ylabel('Average Return')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[0].legend()

plt.show()

#Both
fig2, ax = plt.subplots(1,2)#nrows=1, ncols=2)
ax[0].plot(env_step_cent_12_12_0/(10**6), avg_return_cent_12_12_0, label = 'CENT', color = 'orange')
ax[0].plot(env_step_dec_12_12_0/(10**6), avg_return_dec_12_12_0, label = 'DEC', color = 'green')
ax[0].plot(env_step_dicgcent_12_12_0/(10**6), avg_return_dicgcent_12_12_0, label = 'DICGCE', color = 'blue')
ax[0].plot(env_step_dicgdec_12_12_0/(10**6), avg_return_dicgdec_12_12_0,label = 'DICGDE', color = 'red')
ax[0].axhline(80, color = 'black',linestyle ='dashed')
ax[1].plot(env_step_cent_12_12_n15/(10**6), avg_return_cent_12_12_n15, label = 'CENT', color = 'orange')
ax[1].plot(env_step_dec_12_12_n15/(10**6), avg_return_dec_12_12_n15, label = 'DEC', color = 'green')
ax[1].plot(env_step_dicgcent_12_12_n15/(10**6), avg_return_dicgcent_12_12_n15, label = 'DICGCE', color = 'blue')
ax[1].plot(env_step_dicgdec_12_12_n15/(10**6), avg_return_dicgdec_12_12_n15,label = 'DICGDE', color = 'red')
ax[1].axhline(120, color = 'black',linestyle ='dashed')
ax[0].set_ylabel('Average Return')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[0].legend()

plt.show()

#Density
fig2, ax = plt.subplots(1,2)#nrows=1, ncols=2)
ax[0].plot(env_step_cent_12_8_0/(10**6), avg_return_cent_12_8_0, label = 'CENT', color = 'orange')
ax[0].plot(env_step_dec_12_8_0/(10**6), avg_return_dec_12_8_0, label = 'DEC', color = 'green')
ax[0].plot(env_step_dicgcent_12_8_0/(10**6), avg_return_dicgcent_12_8_0, label = 'DICGCE', color = 'blue')
ax[0].plot(env_step_dicgdec_12_8_0/(10**6), avg_return_dicgdec_12_8_0,label = 'DICGDE', color = 'red')
ax[0].axhline(120, color = 'black',linestyle ='dashed')
ax[1].plot(env_step_cent_12_8_n15/(10**6), avg_return_cent_12_8_n15, label = 'CENT', color = 'orange')
ax[1].plot(env_step_dec_12_8_n15/(10**6), avg_return_dec_12_8_n15, label = 'DEC', color = 'green')
ax[1].plot(env_step_dicgcent_12_8_n15/(10**6), avg_return_dicgcent_12_8_n15, label = 'DICGCE', color = 'blue')
ax[1].plot(env_step_dicgdec_12_8_n15/(10**6), avg_return_dicgdec_12_8_n15,label = 'DICGDE', color = 'red')
ax[1].axhline(120, color = 'black',linestyle ='dashed')
ax[0].set_ylabel('Average Return')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[1].set_xlabel('Total Environment Steps [10$^6$]')
ax[0].legend()

plt.show()
'''






















