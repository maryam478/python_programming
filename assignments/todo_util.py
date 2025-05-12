# id=1
# number_clicked = input('Enter 1 to ADD TASK, 2 to REMOVE task, 3 to mark COMPLETE TASK and 4 to VIEW TO-DO--')
def main(num):
    if num == 1:
        add_tasks = input(' Pleaase enter the task =>')
        add_task(add_tasks)
    if num == 2:
        task_id = input('Enter the ID of task to be removed')
        remove_task(task_id)
    if num == 3:
        task_id = input('Enter the ID of task to mark it Done')
        complete_task(task_id)
    if num == 4:
        show_unfinished_tasks()

# main(number_clicked)

def add_task(add_tasks):
    with open('task.txt','a+') as f:
        f.seek(0)
        lines = f.readlines()
        print(lines)
        if(len(lines)>1):
              id = len(lines)
        else:
              id = 1
              
        progress = str(id)+'-'+str(add_tasks)+'--'+str('unfinished')
        
        print(progress)
        f.write(progress+'\n')
        
def remove_task(id):
    with open('task.txt','r') as f:
        lines=f.readlines()
        new_lines = [line for line in lines if id not in line]
        print(new_lines)
        with open('task.txt','w') as f:
            f.writelines(new_lines)

def complete_task(id):
    # id = input('enter the id')

    with open('task.txt','r') as f:
            lines = f.readlines()
    updated_lines = []
    for line in lines:
            if line.startswith(f'{id}-'):
                    line=line.replace('unfinished','DONE')
            updated_lines.append(line)
            print(updated_lines)

    with open('task.txt','w') as f:
            f.writelines(updated_lines)  


def show_unfinished_tasks():
      with open('task.txt','r') as f:
            lines = f.readlines()
            print(lines)
            active_task=[]
            for line in lines:
                    if 'unfinished' in line:
                            active_task.append(line)
            for todo in active_task:
                    print(todo)


# def main():
#       number_clicked = input('Enter 1 to ADD TASK, 2 to REMOVE task, 3 to mark COMPLETE TASK and 4 to VIEW TO-DO')
#       if number_clicked == 1:
#             add_task()
#       if number_clicked == 2:
#             task_id = input('Enter the ID of task to be removed')
#             remove_task(task_id)
#       if number_clicked == 3:
#             task_id = input('Enter the ID of task to mark it Done')
#             complete_task(task_id)
#       if number_clicked == 4:
#             add_task()
            