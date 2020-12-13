from os import path

this_dir = path.dirname(path.realpath(__file__))
input_file = path.join(this_dir, "input.txt")

bag_parents_map = {}
bag_contents_map = {}

def get_parent_bags(bag_name, found_parent_bags):
    direct_parents = bag_parents_map.get(bag_name)
    if direct_parents:
        for bag in direct_parents:
            found_parent_bags.add(bag)
            get_parent_bags(bag, found_parent_bags)

def get_inner_bag_count(bag_name):
    total_inner_bags = 0
    direct_contents = bag_contents_map.get(bag_name)
    if direct_contents:
        for bag in direct_contents:
            this_bag_count = direct_contents[bag]
            total_inner_bags += this_bag_count + (this_bag_count * get_inner_bag_count(bag))
    return total_inner_bags

with open(input_file) as f:
    for entry in f:
        entry = entry.strip()
        rule = entry.split(" contain ")
        bag = rule[0].rstrip('s')
        contents = rule[1].rstrip('. ').split(', ')
        if contents[0] == "no other bags":
            content = {}
        else:
            content = {item.split(" ", 1)[1].rstrip('s'): int(item.split(" ", 1)[0]) for item in contents}
        
        bag_contents_map[bag] = content

        parents = set()
        for inner_bag in content:
            if not bag_parents_map.get(inner_bag):
                bag_parents_map[inner_bag] = set()
            bag_parents_map[inner_bag].add(bag)
        

parent_bags_result = set()
get_parent_bags("shiny gold bag", parent_bags_result)

print(f"Part one: {len(parent_bags_result)}")
print(f"Part two: {get_inner_bag_count('shiny gold bag')}")