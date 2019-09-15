import sys
sys.setrecursionlimit(150)

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


class Connection:
    def __init__(self, nodes, end):
        self.end = end
        self.used = False

class Node:
    def __init__(self, name):
        self.name = name
        self.routes = []

    def add_route(self, nodes, end):
        self.routes.append(Connection(nodes, end))

    def route(self, route):
        routes = []  # List of Connection objects
        for route in self.routes:
            if not route.used:
                route.used = True
                routes.append(route.end.route())
        else:
            return None

    def navigate(self, past_paths, cur_path):
        # print(self.name)
        def path_test(end):
            for path in past_paths:
                if path[0:len(cur_path)+1] == cur_path + [end]:
                    return False
            else:
                # print("##################")
                return True
        for route in self.routes:
            if not route.used and path_test(route.end):
                route.used = True
                cur_path.append(route.end)
                # print(f"Navigating from {self.name} to {route.end.name}")
                route.end.navigate(past_paths, cur_path)
                return cur_path
        else:
            # self.print_route(cur_path)
            return cur_path

    def reset_routes(self):
        for route in self.routes:
            if route.used:
                route.used = False
                route.end.reset_routes()

    @staticmethod
    def print_route(route):
        outstring = ""
        for node in route:
            outstring += node.name
        print(outstring)

    @staticmethod
    def string_route(route):
        outstring = ""
        for node in route:
            outstring += node.name
        return outstring

nodes = {}

def set_connections(route):
    for i in range(len(route)):
        node = route[i]
        for conn in node.routes:
            if i > len(route)-2:
                break
            else:
                # print(conn.end == route[i+1])
                if conn.end == route[i+1]:
                    conn.used = True
                    # print("Connection set.")
                    break

for key in states.keys():
    if key[0] in nodes.keys():
        pass
    else:
        nodes[key[0]] = Node(key[0])

for key in states.keys():
    node = nodes[key[0]]
    if key[1] in nodes:
        node.add_route(nodes, nodes[key[1]])

# for node in nodes.values():
#     for route in node.routes:
#         print(node.name, route.end.name)

# Method: Using DFS, and avoiding past routes:

past_paths = []
for node in nodes.values():
    cur_path = [node]
    path = node.navigate(past_paths, cur_path)
    # node.print_route(path)
    past_paths.append(path)
    node.reset_routes()
    for i in range(len(path)):
        node.reset_routes()
        set_connections(path[0:i])
        new_path = path[-1].navigate(past_paths, path[0:i])
        node.print_route(new_path)
        past_paths.append(new_path)

    node.reset_routes()

max_len = 0
max_path = []
total = 0

champ_paths = open("champ paths.csv", "w+")

for path in past_paths:
    if len(path) > 0:
        node = path[0]
        for i in range(len(path)):
            node.reset_routes()
            set_connections(path[0:i])
            new_path = path[-1].navigate(past_paths, path[0:i])
            total += 1
            if total % 1000 == 0:
                print(f"Checked {total} routes so far.")
            if len(new_path) > 22:
                champ_paths.write(f"{len(new_path)}, {node.string_route(new_path)}, {total}\n")
            if len(new_path) > max_len:
                max_len = len(new_path)
                max_path = new_path
                print("New champ found!")
                print("Length: ", max_len)
                print("Total checked: ", total)
                champ_paths.write(f"{len(new_path)}, {node.string_route(new_path)}, {total}\n")
                node.print_route(max_path)
            # node.print_route(new_path)
            past_paths.append(new_path)
