import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel_winners = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_winners = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
roller_coasters = pd.read_csv('roller_coasters.csv')


# ==============================================================
# FUNCTIONS
# ==============================================================
def plot_1ranking_over_time(roller_coaster_name, park_name, df_ranking):
    roller_coaster = df_ranking[(df_ranking['Name'] == roller_coaster_name) & (df_ranking['Park'] == park_name)]
    fig = plt.figure()
    plt.plot(roller_coaster['Year of Rank'], roller_coaster.Rank)
    plt.ylabel('Ranking')
    plt.gca().invert_yaxis()
    plt.xlabel('Year')
    plt.title("{} Rankings".format(roller_coaster_name))
    return fig


def plot_2ranking_over_time(roller_coaster_name1, park_name1, roller_coaster_name2, park_name2, df_ranking):
    roller_coaster1 = df_ranking[(df_ranking['Name'] == roller_coaster_name1) & (df_ranking['Park'] == park_name1)]
    roller_coaster2 = df_ranking[(df_ranking['Name'] == roller_coaster_name2) & (df_ranking['Park'] == park_name2)]
    fig = plt.figure()
    plt.plot(roller_coaster1['Year of Rank'], roller_coaster1.Rank)
    plt.plot(roller_coaster2['Year of Rank'], roller_coaster2.Rank)
    plt.ylabel('Ranking')
    plt.gca().invert_yaxis()
    plt.xlabel('Year')
    plt.title("{} and {} Rankings".format(roller_coaster_name1, roller_coaster_name2))
    plt.legend([roller_coaster_name1, roller_coaster_name2])
    return fig


def plot_n_rank(n, df_ranking):
    top_n_ranking = df_ranking[df_ranking['Rank'] <= n]
    fig = plt.figure()
    for coaster in set(top_n_ranking['Name']):
        rankings = top_n_ranking[top_n_ranking['Name'] == coaster]
        plt.plot(rankings['Year of Rank'], rankings['Rank'])

    plt.legend(list(set(top_n_ranking['Name'])))
    plt.gca().invert_yaxis()
    return fig


def hist_numeric_column(column_name, df_coaster):
    df_res = df_coaster[column_name].dropna()
    plt.hist(df_res)
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel('{}'.format(column_name))
    plt.show()


def bar_num_inversions(park_name, df_coaster):
    coasters = df_coaster[df_coaster['park'] == park_name]
    coasters = coasters.sort_values('num_inversions', ascending=False)
    plt.bar(coasters['name'], coasters['num_inversions'])
    plt.xticks(rotation='vertical')
    plt.ylabel('Number of inversions')
    plt.title('Number of inversions per coaster at {}'.format(park_name))
    plt.show()


def pie_chart_coasters(df_coaster):
    operating = df_coaster[df_coaster.status == 'status.operating']
    closed = df_coaster[df_coaster.status == 'status.closed.definitely']
    operating_perc = round(100*len(operating)/(len(operating)+len(closed)), 1)
    closed_perc = 100 -operating_perc

    plt.pie([operating_perc, closed_perc], labels=['Operating', 'Closed'], autopct='%1.2f%%')
    plt.show()


def scatter_2columns(column_x, column_y, df_coaster):
    plt.scatter(df_coaster[column_x], df_coaster[column_y])
    plt.title('Scatter plot of {} vs {}'.format(column_y, column_x))
    plt.xlabel('{}'.format(column_x))
    plt.ylabel('{}'.format(column_y))
    plt.show()

# ==============================================================
# MAIN CALLS
# ==============================================================
