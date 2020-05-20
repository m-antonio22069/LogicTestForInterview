import json

def save(final_dict, person):
    with open(person+'.json', 'w') as json_file:
        json.dump(final_dict, json_file, indent=4)
    
def return_projects(names, person, dados):
    managers_project = []
    for name in range(len(names)):
        managers_project.append({})
    
        for index in dados:
            for test in range(len(index[person])):
                if index[person][test] == names[name]:
                    managers_project[name].update(dict([(index['name'],index['priority'])]))
        
        managers_project[name]=sorted(managers_project[name], key = managers_project[name].get)
    
    final_dict = {}
    for name in range(len(names)):
        final_dict.update(dict([(names[name],managers_project[name])]))
    
    return save(final_dict, person)

def organize(dados,person):
    names = []
    for i in range(len(dados)):
        for j in range(len(dados[i][person])):
            if dados[i][person][j] not in names:
                names.append(dados[i][person][j])
    return return_projects(names, person, dados)


with open(r'source_file_2.json') as json_file:
    dados = json.load(json_file)

managers_organized = organize(dados,'managers')
watchers_organized = organize(dados,'watchers')

