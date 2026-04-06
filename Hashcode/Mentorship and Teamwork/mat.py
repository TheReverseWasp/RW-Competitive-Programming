import pandas as pd
import numpy as np

l_files = [
"a_an_example.in.txt",
 "b_better_start_small.in.txt",
 "c_collaboration.in.txt",
 "d_dense_schedule.in.txt",
 "e_exceptional_skills.in.txt",
 "f_find_great_mentors.in.txt",
]

for file in l_files:
    collaborators_skills = {}
    skill_set = set()
    projects_dict = {}
    with open(f"input_data/{file}", "r") as f:
        ## Collaborators
        people, projects = map(int, f.readline().split())
        for ppl in range(people):
            contributor, num_skills = f.readline().split()
            num_skills = int(num_skills)
            collaborators_skills[contributor] = [num_skills, []]
            for i in range(num_skills):
                skill, lvl = f.readline().split()
                lvl = int(lvl)
                collaborators_skills[contributor][-1].append([skill, lvl])
                skill_set.add(skill)
        ## Projects
        for prj in range(projects):
            project_name, duration, score, deadline, skills = f.readline().split()
            [duration, score, deadline, skills] = list(map(int, [duration, score, deadline, skills]))
            projects_dict[project_name] = [duration, score, deadline, skills, []]
            for skill in range(skills):
                sk, lvl = f.readline().split()
                lvl = int(lvl)
                projects_dict[project_name][-1].append([sk, lvl])

    #Collaborators df
    dic_to_df = {}
    dic_to_df["collaborator"] = []
    dic_to_df["num_skills"] = []
    for i in skill_set:
        dic_to_df[i] = []
    for key, values in collaborators_skills.items():
        dic_to_df["collaborator"].append(key)
        dic_to_df["num_skills"].append(values[0])
        for skill in skill_set:
            dic_to_df[skill].append(0)
        for elem in values[-1]:
            dic_to_df[elem[0]][-1] = elem[1]

    collaborators_df = pd.DataFrame.from_dict(dic_to_df)

    # Projects_df
    dic_to_pj_df = {}
    dic_to_pj_df["project"] = []
    dic_to_pj_df["duration"] = []
    dic_to_pj_df["score"] = []
    dic_to_pj_df["deadline"] = []
    dic_to_pj_df["skills"] = []
    for i in skill_set:
        dic_to_pj_df[i] = []
    for key, values in projects_dict.items():
        dic_to_pj_df["project"].append(key)
        dic_to_pj_df["duration"].append(values[0])
        dic_to_pj_df["score"].append(values[1])
        dic_to_pj_df["deadline"].append(values[2])
        dic_to_pj_df["skills"].append(values[3])
        for skill in skill_set:
            dic_to_pj_df[skill].append(0)
        for item in values[-1]:
            dic_to_pj_df[item[0]][-1] = item[1]

    projects_df = pd.DataFrame.from_dict(dic_to_pj_df)

    projects_df["euristic"] = ((projects_df["score"] / projects_df["duration"]) / projects_df["deadline"]) * projects_df["skills"]

    projects_df = projects_df.sort_values(by = "euristic", ascending = False).reset_index(drop=True)


    ######################## Functions #########################

    def calc_possible(project_series, collaborators):
        collaborator_list = []
        skill_dic = {skill: 0 for skill in skill_set}
        sorted_same = 0
        collaborator_set = set()
        # equal score:
        for skill in skill_set:
            if project_series[skill] != 0:
                same = collaborators[collaborators[skill] == project_series[skill]]
                if len(same) != 0:
                    sorted_same = same.sort_values(by = "num_skills").reset_index(drop=True)
                    sorted_same = sorted_same.iloc[:1].reset_index(drop=True)
                    collaborator_list.append([sorted_same, skill])
                    for skill in skill_set:
                        skill_dic[skill] = max(skill_dic[skill], sorted_same[skill][0])
        # best mentors
        if project_series[skills] != len(collaborator_list):
            completed_set = set([elem[1] for elem in collaborator_list])
            collaborator_set = set([elem[0]["collaborator"][0] for elem in collaborator_list])
            for skill in skill_set:
                if project_series[skill] != 0 and not skill in completed_set:
                    less_one = collaborators[collaborators[skill] == project_series[skill] - 1].sort_values(by = "num_skills").reset_index(drop=True)
                    for it, row in less_one.iterrows():
                        if not row["collaborator"] in collaborator_set:
                            collaborator_set.add(row["collaborator"])
                            completed_set.add(skill)
                            collaborator_list.append([row, skill])
                            for skill_ in skill_set:
                                skill_dic[skill_] = max(skill_dic[skill_], row[skill_])
                            break

        if project_series[skills] != len(collaborator_list):
            for skill in skill_set:
                if project_series[skill] != 0 and not skill in completed_set:
                    upper = collaborators[collaborators[skill] > project_series[skill]].sort_values(by = "num_skills").reset_index(drop=True)
                    for it, row in upper.iterrows():
                        if not row["collaborator"] in collaborator_set:
                            collaborator_set.add(row["collaborator"])
                            completed_set.add(skill)
                            collaborator_list.append([row, skill])
                            for skill_ in skill_set:
                                skill_dic[skill_] = max(skill_dic[skill_], row[skill_])
                            break



        if project_series["skills"] != len(collaborator_set):
            return False, collaborator_set
        return True, collaborator_set








    ######################## End Functions #########################



    projects_df["end_date"] = -1
    actual = 0
    ans = {}
    collaborators_busy = {row["collaborator"]: -1 for it, row in collaborators_df.iterrows()}
    min_change = 99999999999999999999999999
    flag_no_change_counter = 0
    while len(projects_df) != 0:
        flag_no_change = True
        for it, row in projects_df.iterrows():
            if row["end_date"] == -1:
                 temp_collaborators = collaborators_df[collaborators_df["collaborator"].isin(set([coll for coll, busy_until in collaborators_busy.items() if collaborators_busy[coll] <= actual]))]
                 answer, collabs = calc_possible(row, temp_collaborators)
                 if answer:
                     flag_no_change = False
                     ans[row["project"]] = [coll for coll in collabs]
                     projects_df.at[it, "end_date"] = row["duration"] + actual
                     min_change = min(min_change, row["duration"] + actual)

        if flag_no_change:
            actual = min_change + 0
            min_change = 99999999999999999999999999
            flag_no_change_counter += 1
        else:
            flag_no_change_counter = 0
        if flag_no_change_counter >= 2:
            break

    output_str = f"{len(ans)}\n"
    for key, val in ans.items():
        output_str += f"{key}\n"
        output_str += " ".join(list(val)) + "\n"
    output_str = output_str[:-1]
    with open(f"{file[:-6]}out.txt", "w") as out_file:
        out_file.write(output_str)
