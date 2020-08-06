import matplotlib.pyplot as plt
import matplotlib.ticker
from face2face.statistics.distribution import *
from face2face.statistics.check_distribution import *
from face2face.imports.load_all_data import Data
from face2face.imports.create_network import create_network_from_data
from face2face.statistics.network_quantities import *
from face2face.imports.create_network import *
import powerlaw
import networkx as nx
import pandas as pd
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 10}

matplotlib.rc('font', **font)
plt.rc('legend', fontsize=5)


df = Data("test")
event_list = [("Eve A", 20, 60), ("Eventim B", 120, 180), ("E C", 400, 500)]
#print(df.interaction)
#networks, dfs = hopping_time_networks(df, minutes=2/3)
#network, dfs = sliding_time_networks(df, slide=1/3, interval=2/3)
networks, dfs = event_time_networks(df, events=event_list)
print(dfs)
#print(df.interaction)
#print(dfs[0])
#df_2 = Data(meta_df=df.metadata, tij_df=dfs[0])
#print(df_2.interaction)
#df_3 = df.interaction
#print(df_3)
#print(df_2.metadata)


def analyze_dataset_distribution(delta_t_list, dataset_name, interaction_data):

    fit = powerlaw.Fit(delta_t_list)

    fit_obj, tupel_list, distribution = search_best_fit_distribution(delta_t_list, xmin=fit.xmin, discret=True, approximation_method=50)
    max_value = max(delta_t_list)
    min_value = min(delta_t_list)
    liste = list(set(list(interaction_data["i"] + interaction_data["j"])))
    n = len(liste)

    for j in distribution:
        if j == "power_law":
            para1 = fit_obj.power_law.alpha
            name1 = "alpha"
            para2 = fit_obj.power_law.sigma
            name2 = "sigma"
            para3 = None
            name3 = None

        if j == "lognormal":
            para1 = fit_obj.lognormal.parameter1
            name1 = fit_obj.lognormal.parameter1_name
            para2 = fit_obj.lognormal.parameter2
            name2 = fit_obj.lognormal.parameter2_name
            para3 = fit_obj.lognormal.parameter3
            name3 = fit_obj.lognormal.parameter3_name

        if j == "exponential":
            para1 = fit_obj.exponential.parameter1
            name1 = fit_obj.exponential.parameter1_name
            para2 = fit_obj.exponential.parameter2
            name2 = fit_obj.exponential.parameter2_name
            para3 = fit_obj.exponential.parameter3
            name3 = fit_obj.exponential.parameter3_name

        if j == "truncated_power_law":
            para1 = fit_obj.truncated_power_law.parameter1
            name1 = fit_obj.truncated_power_law.parameter1_name
            para2 = fit_obj.truncated_power_law.parameter2
            name2 = fit_obj.truncated_power_law.parameter2_name
            para3 = fit_obj.truncated_power_law.parameter3
            name3 = fit_obj.truncated_power_law.parameter3_name

        if j == "stretched_exponential":
            para1 = fit_obj.stretched_exponential.parameter1
            name1 = fit_obj.stretched_exponential.parameter1_name
            para2 = fit_obj.stretched_exponential.parameter2
            name2 = fit_obj.stretched_exponential.parameter2_name
            para3 = fit_obj.stretched_exponential.parameter3
            name3 = fit_obj.stretched_exponential.parameter3_name

        if j == "lognormal_positive":
            para1 = fit_obj.lognormal_positive.parameter1
            name1 = fit_obj.lognormal_positive.parameter1_name
            para2 = fit_obj.lognormal_positive.parameter2
            name2 = fit_obj.lognormal_positive.parameter2_name
            para3 = fit_obj.lognormal_positive.parameter3
            name3 = fit_obj.lognormal_positive.parameter3_name

        print(dataset_name + ", xmin: " + str(fit_obj.xmin) + ", distribution: " + j + ", "
                  + str(min_value) + " - " + str(max_value) + ": " + str(name1) + ": " + str(para1) + ", "
                  + str(name2) + ": "+ str(para2) + ", " + str(name3) + ": " + str(para3) + "Individuals: " + str(n))

#analyze_dataset_distribution()
#liste = ["WS16","hospital","HT09","InVS13","InVS15","PS09","SFHH09","sg09","thiers11","thiers12","thiers13"]
#liste = ["hospital","HT09","InVS13","InVS15","PS09","SFHH09","sg09","thiers11","thiers12","thiers13"]

#for i in liste:
#
#    df = Data(i)
#G = nx.Graph()
#G.add_nodes_from(df.metadata["ID"].values)
#df_edge = df.interaction.groupby(["i", "j"]).size().reset_index(name="EdgeWeight")
#print(df_edge)
#
#    list_x_y_contact, delta_t_list_contact = calculate_contact_duration(df)
#print(type(delta_t_list_contact[0]))
#list_x_y_triangle, delta_t_list_triangle = calculate_triangle_duration(df)
#list_of_floats = [float(item) for item in delta_t_list_contact]
#print(type(list_of_floats[0]))

#list_x_y_inter, delta_t_list_inter = calculate_inter_contact_duration(df)
#
  #  analyze_dataset_distribution(delta_t_list_contact, i, interaction_data=df.interaction)
#
# fit = powerlaw.Fit(delta_t_list_contact)
# plt.subplot(121)
# fit.plot_pdf(color='#1b9e77', linewidth=2, label="Original data", original_data=True)
# fit.lognormal.plot_pdf(color='#d95f02', linestyle="--", label="Lognormal")
# fit.truncated_power_law.plot_pdf(color='#7570b3', linestyle="--", label="Truncated Powerlaw")
# plt.ylabel("P(${\Delta t}_{ij}$)")
# plt.xlabel("${\Delta t}_{ij}$ (seconds)")
# plt.legend(loc="upper right")
# plt.title("contact (hospital)")
#
# fit = powerlaw.Fit(delta_t_list_triangle)
# plt.subplot(222)
# fit.plot_pdf(color='#1b9e77', linewidth=2, label="Original data", original_data=True)
# fit.lognormal.plot_pdf(color='#d95f02', linestyle="--", label="Lognormal")
# fit.truncated_power_law.plot_pdf(color='#7570b3', linestyle="--", label="Truncated Powerlaw")
# plt.ylabel("P(${\Delta t}_{ijk}$)")
# plt.xlabel("${\Delta t}_{ijk}$ (seconds)")
# plt.legend(loc="upper right")
# plt.title("triangle (hospital)")
# #
# fit = powerlaw.Fit(delta_t_list_inter)
# plt.subplot(224)
# fit.plot_pdf(color='#1b9e77', linewidth=2, label="Original data", original_data=True)
# fit.lognormal.plot_pdf(color='#d95f02', linestyle="--", label="Lognormal")
# fit.truncated_power_law.plot_pdf(color='#7570b3', linestyle="--", label="Truncated Powerlaw")
# #fit.exponential.plot_pdf(color='m', linestyle="--", ax=fig, label="exponential")
# plt.ylabel("P($t_{ij} - t_{ik}$)")
# plt.xlabel("$t_{ij} - t_{ik}$ (seconds)")
# plt.legend(loc="upper right")
# plt.title("inter-contact (hospital)")
# plt.tight_layout()
# plt.show()
#
#
# fit = powerlaw.Fit(delta_t_list_inter)
# #plt.subplot(224)
# fit.plot_pdf(color='#1b9e77', linewidth=2, label="Original data", original_data=True)
# fit.lognormal.plot_pdf(color='#d95f02', linestyle="--", label="Lognormal")
# fit.truncated_power_law.plot_pdf(color='#7570b3', linestyle="--", label="Truncated Powerlaw")
# #fit.exponential.plot_pdf(color='m', linestyle="--", ax=fig, label="exponential")
# plt.ylabel("P($t_{ij} - t_{ik}$)")
# plt.xlabel("$t_{ij} - t_{ik}$ (seconds)")
# plt.legend(loc="upper right")
# plt.title("inter-contact (hospital)")
# plt.tight_layout()
# plt.show()

# def values(string):
#
#     contacts_at_timestamp = []
#     df = Data(string)
#     for key, value in df.interaction.groupby("Time"):
#         Liste = set(list(value["i"]) + list(value["j"]))
#         p = len(Liste)
#         contacts_at_timestamp.append(p)
#     p_average = sum(contacts_at_timestamp)/len(contacts_at_timestamp)
#
#     G = nx.Graph()
#     df_edge = df.interaction.groupby(["i", "j"]).size().reset_index(name="EdgeWeight")
#     for col, row in df_edge.iterrows():
#         G.add_edge(row["i"], row["j"])
#     k = mean_degree_network(G)
#
#     print(string + " " + "P_average: " + str(p_average) + " " + "k: " + str(k))
#
#
# for i in liste:
#     values(i)


#print(test)


#df = Data("WS16")
#df = df.interaction.groupby("Time")
#for key, value in df.interaction.groupby("Time"):
#    print(value)