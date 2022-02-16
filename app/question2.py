
from collections import defaultdict, deque

class Question2:
    def __init__(self):
        self.prerequisites = None
        self.query = None
        self.error_msg = f"Invalid rules: cycle detected"
    
    def run(self, query, filepath):
        self.prerequisites = self.parse_file(filepath)
        self.query = query

        q2a, q2b = self.topological_sort()

        print(f"2a: A total of {q2a} bag colours can eventually contain at least one shiny gold bag.")
        # print(f"2A Details: {q2a_list}")
        print(f"2b: {q2b} individual bags are required inside a single shiny gold bag.")

        return q2a, q2b

    def parse_file(self, filepath):
        data = defaultdict(lambda: defaultdict(int))  

        with open(filepath, 'r') as file_object:
            line = file_object.readline().strip()
            while line:
                outer_bag, inner_bags = line.split("contain ")
                outer_bag = outer_bag.rsplit(' bags ', 1)[0]
                inner_bags_list = inner_bags.split(",")
                for i in range(len(inner_bags_list)):
                    if 'no other bags.' in inner_bags_list[i]:
                        continue
                    inner_bag = inner_bags_list[i].rsplit(' ', 1)[0].strip()
                    bag_amount, bag_colour = inner_bag.split(' ', 1)
                    bag_colour = bag_colour.strip()
                    bag_amount = int(bag_amount)
                    data[outer_bag][bag_colour] = bag_amount
                line = file_object.readline().strip()

        return data

    def topological_sort(self):

        '''
        list of colour of bags
        '''
        bag_colours = set()
        for i in self.prerequisites:
            bag_colours.add(i)
            bag_colours.update(self.prerequisites[i])

        '''
        initiate indegree list for topological sort
        '''
        indegree = defaultdict(int)
        for i in list(bag_colours):
            indegree[i] = 0
        
        '''
        construct a dictionary of the form:
            outer bag: [list of bags that this is a prereq for and their quantity]
        '''
        prereqDict = defaultdict(lambda: defaultdict(int))
        for outer_bag, inner_bags in self.prerequisites.items():
            for inner_bag, inner_bag_num in inner_bags.items():
                prereqDict[inner_bag][outer_bag] = inner_bag_num

        '''
        populate the indegree list
        '''
        for x in prereqDict:
            for y in prereqDict[x]:
                indegree[y] += 1

        '''
        Enqueue bags with no prerequisites
        '''
        queue = deque()
        for x in list(bag_colours):
            if indegree[x] == 0:
                queue.append(x)
        
        '''
        Topological sort with Kahn's algorithm
        '''
        q2a = 0
        # q2a_list = [] 
        queries = [self.query]
        q2b = defaultdict(int)
        result = [] # optional checking for cycle
        while len(queue) != 0:
            v = queue.popleft()
            
            result.append(v) # optional checking for cycle

            if v in queries:
                '''
                count outer bags
                '''
                if v != self.query:
                    q2a += 1
                    # q2a_list.append(v) # optional record of all outer bags
                queries.remove(v)
                queries += list(prereqDict[v].keys())

            for x in prereqDict[v]:
                '''
                count inner bags bottom up
                '''
                if prereqDict[v][x] != 0: # just in case when value is 0
                    q2b[x] += q2b[v] * prereqDict[v][x]
                q2b[x] += prereqDict[v][x]
                # q2b[x] += q2b[v] * prereqDict[v][x] + prereqDict[v][x]
                indegree[x] -= 1
                if indegree[x] == 0:
                    queue.append(x)
        
        # optional checking for cycle
        if len(bag_colours) != len(result):
            return self.error_msg, self.error_msg
        
        return q2a, q2b[self.query]


if __name__ == '__main__':
    Question2().run('shiny gold', 'app/q2_pda_data.txt')