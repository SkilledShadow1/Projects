import json

with open ('linked_links.json', 'r') as f:
    info = json.load(f)

 
import networkx 
import pandas
import matplotlib.pyplot as plt


all_connections = []
placeholder = []
main_links = []


map1 = {}
n = 1
for link in info:
    map1[link] = n
    n += 1


map_connection = {}

for l, connection in info.items():
    value = [map1[_] for _ in connection]
    map_connection[map1[l]] = value


print(list(map_connection.values()))



for link, connections in info.items():
    main_links.append(link)
    for connection in connections:
        placeholder.append(connection)
    all_connections.append(placeholder)
    placeholder = []


key_list = []

for key, value in map_connection.items():
    key_list.append(key)

print('running')
# Here, I'm going to create a pandas dataframe with example data
def create_df():
    
    return pandas.DataFrame(
        # Naming the nodes A,B,C,D, and E
        {'node_name':key_list,
         # Edges refers to which nodes each node is connected to
         'edges':list(map_connection.values())},
        # Index number can be used instead of name for any node
         )

def create_graph(nodes_df):
    # First, we must create a graph object
    graph = networkx.Graph()
    # Then we can add nodes to the graph
    # Use [graph.add_node()] to add nodes one at a time. Maybe add to for loop?
    # Or, use [graph.add_nodes_from()] to add all the nodes in a list!
    graph.add_nodes_from(nodes_df.node_name) 
    # Now it's time to add the connections between the nodes
    for row in nodes_df.iterrows(): #<- Pandas iterrows returns iterable list of tuples
        # Here, [row] is a tuple: ('index', pd.Series)
        # We can iterate over every neighbor in the series like this...
        for neighbor in row[1].edges:
            # Adding an edge for every neighbor
            graph.add_edge(row[1].node_name, neighbor)
    # Returning graph
    return graph

for key, value in map1.items():
    print(f"{value}: {key}")


if __name__ == '__main__':
    # Creating the pandas dataframe
    nodes = create_df()
    # Creating the networkx graph
    print(nodes.iloc[0])
    display = create_graph(nodes)
    
    # Creating a matplotlib figure and axis
    fig, axis = plt.subplots()


    # [draw_networkx] can be used to add additional features
    networkx.drawing.nx_pylab.draw_networkx(display, width = 0.2)
    
    
    # Now we can change our graph a bunch using matplotlib! Hurray!!!
    fig.suptitle('Map of helloworldstudio.org', fontsize=16)
    # These lims change the x and y limits, basically zooms out or in.

    # Google for more ideas!

    # This will display the plot
    plt.show(fig)
    input('done?')
    # All matplotlib figures will remain open in the background of your computer,
    # and bog down your system. Make sure to close them all before making more!
    plt.close('all')

    # OR save them with the savefig method.