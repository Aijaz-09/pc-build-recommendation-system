import json

def load_data():
    with open('components.json') as f:
        data=json.load(f)
    return data

def get_user_input():
    budget=int(input('Enter total budget: '))
    return budget

def cpu_budget(total_budget): #let cpu get 30% for a test
    return total_budget*0.3

def filter_cpus(cpu_list, max_price):
    valid_cpus=[]
    for cpu in cpu_list:
        if cpu['price'] <= max_price:
            valid_cpus.append(cpu)
    return valid_cpus

def sel_best_cpu(cpus):
    best=None
    best_score=-1
    for cpu in cpus:
        if cpu['score'] > best_score:
            best=cpu
            best_score=cpu['score']
    return best

def main():
    data=load_data()
    budget=get_user_input()
    max_cpu_price=cpu_budget(budget)
    cpu_list=data['cpu']
    valid_cpus=filter_cpus(cpu_list,max_cpu_price)
    # Need to add exception handling here (when no cpu is valid)
    best_cpu=sel_best_cpu(valid_cpus)

    print("\nRecommended CPU: ")
    print(best_cpu['name'], ': RS->', best_cpu['price'])