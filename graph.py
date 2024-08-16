import sys

smn = open(sys.argv[1],"r").read().splitlines()
commands = open(sys.argv[2],"r").read().splitlines()
output = open("output.txt", "w")
dic = {}

for i in smn:
    user , friends = i.split(":")
    dic[user] = friends.split(" ")

for i in dic.keys():
    if '' in dic[i]:
        dic[i].remove('')


def ANU(x):
    global dic
    if x in dic.keys():
        output.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!\n")
    else:
        output.write(f"User '{x}' has been added to the social network successfully\n")
        dic[x] = []

def DEU(x):
    global dic
    if x not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'DEU'! -- There is no user named '{x}'!\n")
    else:
        output.write(f"User '{x}' and his/her all relations have been deleted successfully\n")
        dic.pop(x)
        for i in dic.values():
            if x in i:
                i.remove(x)

def ANF(x,y):
    global dic
    if x and y not in dic.keys():
        output.write(f"ERROR: Wrong input type for! 'ANF'! -- No user named '{x}' and '{y}' found!\n")
    elif x not in dic.keys():
        output.write(f"ERROR: Wrong input type for! 'ANF'! -- No user named '{x}' found!\n")
    elif y not in dic.keys():
        output.write(f"ERROR: Wrong input type for! 'ANF'! -- No user named '{y}' found!\n")
    elif x in dic[y] or y in dic[x]:
        output.write(f"ERROR: A relation between '{x}' and '{y}' already exists!\n")
    else:
        output.write(f"Relation between '{x}' and '{y}' has been added successfully\n")
        dic[x].append(y)
        dic[y].append(x)

def DEF(x,y):
    global dic
    if x and y not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{x}' and '{y}' found!\n")
    elif x not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{x}' found!\n")
    elif y not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named '{y}' found!\n")
    elif x not in dic[y] or y not in dic[x]:
        output.write(f"EROOR: No relation between '{x}' and '{y}' found!\n")
    else:
        output.write(f"Relation between '{x}' and '{y}' has been deleted successfully!\n")
        dic[x].remove(y)
        dic[y].remove(x)

def CF(x):
    global dic
    if x not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{x}' found!\n")
    else:
        output.write(f"User '{x}' has {len(dic[x])} friends.\n")

def FPF(x,y):
    global dic
    possible_friends = []
    if y < 1 or y > 3:
        output.write(f"ERROR: Wrong input type! for 'FPF'! -- Maximum distance '{y}' is out of range!\n")
    elif x not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named '{x}' found!\n")
    else:
        if y == 1:
            for i in dic[x]:
                possible_friends.append(i)
        elif y == 2:
            for i in dic[x]:
                possible_friends.append(i)
                for j in dic[i] :
                    possible_friends.append(j)
        elif y == 3:
            for i in dic[x]:
                possible_friends.append(i)
                for j in dic[i]:
                    possible_friends.append(j)
                    for k in dic[j]:
                        possible_friends.append(k)

        my_set = {i for i in possible_friends}
        possible_friends = sorted(my_set)
        if x in possible_friends:
            possible_friends.remove(x)

        output.write(f"User '{x}' has {len(possible_friends)} possible friends when maximum distance is '{y}'.\n")
        output.write("These possible friends: {'")
        output.write(("','").join(possible_friends))
        output.write("'}\n")

def SF(x,y):
    global dic
    all_friends = []
    md2_list = []
    md3_list = []
    if x not in dic.keys():
        output.write(f"ERROR: Wrong input type! for 'SF'! -- No user named '{x}' found!\n")
    elif y < 2 or y > 3:
        output.write(f"ERROR: Mutuality Degree can't be less than 2 or greater than 3\n")
    elif y > len(dic[x]):
        output.write(f"EROOR: Mutuality Degree can't be greater than friend count\n")
    else:
        for i in dic[x]:
            for j in dic[i]:
                all_friends.append(j)
        myset = {i for i in all_friends}

        for i in myset:
            if all_friends.count(i) == 2:
                md2_list.append(i)
            elif all_friends.count(i) == 3:
                md3_list.append(i)

        if x in md2_list:
            md2_list.remove(x)
        elif x in md3_list:
            md3_list.remove(x)

        if y == 2:
            if len(md2_list) == 0 and len(md3_list) == 0:
                output.write(f"There is no suggested friends for '{x}' (when MD is {y})\n")
            else:
                output.write(f"Suggestion List for '{x}' (when MD is {y}):\n")

                if len(md2_list) != 0:
                    for i in sorted(md2_list):
                        output.write(f"'{x}' has 2 mutual friends with '{i}'\n")
                if len(md3_list) != 0:
                    for i in sorted(md3_list):
                        output.write(f"'{x}' has 3 mutual friends with '{i}'\n")

                output.write(f"The suggested friends for '{x}': '")
                output.write(("','").join(sorted(md3_list+md2_list)))
                output.write("'\n")

        elif y == 3:
            if len(md3_list) == 0:
                output.write(f"There is no suggested friends for '{x}' (when MD is {y})\n")
            else:
                output.write(f"Suggestion List for '{x}' (when MD is {y}):\n")
                for i in sorted(md3_list):
                    output.write(f"'{x}' has 3 mutual friends with '{i}'\n")
                output.write(f"The suggested friends for '{x}': '")
                output.write(("','").join(sorted(md3_list)))
                output.write("'\n")

for i in commands:
    command = i.split(" ")
    if command[0] == 'ANU':
        ANU(command[1])
    elif command[0] == 'DEU':
        DEU(command[1])
    elif command[0] == 'ANF':
        ANF(command[1],command[2])
    elif command [0] == 'DEF':
        DEF(command[1],command[2])
    elif command[0] == 'CF':
        CF(command[1])
    elif command[0] == 'FPF':
        FPF(command[1],int(command[2]))
    elif command[0] == 'SF':
        SF(command[1],int(command[2]))
    else:
        output.write("Invalid Command\n")

output.close()