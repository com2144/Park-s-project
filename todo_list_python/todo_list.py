import json
import os


class Todolist:
    def __init__(self):
        self.todo_list = []
        self.complete_list = []
        self.add_lists = ''

    def json_file_quest(self):
        print("Input json file name if you want to load json file from home folder")
        print("If you don't want to import file, press anything")
        file_name = input("Ex) test.json : ")
        file_path = os.path.expanduser(f'~/{file_name}')
        if os.path.isfile(file_path) and os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.to_do_list = (data["todo_list"])
                self.complete_list = (data["complete_list"])
        else:
            print("\nAdd tasks. Type 'Q' when finished")
            print("""
            Ex)
            modeling
            rigging
            comp
            end""")
            while True:
                self.add_lists = input("")
                if self.add_lists in ['q', 'Q', 'ㅁ']:
                    break
                if self.add_lists == '':
                    continue
                else:
                    if self.add_lists in self.todo_list:
                        print("is already in the list.")
                        continue
                    else:
                        self.todo_list.append(self.add_lists)   

    def input_check_for_todolist(self, input_num):
        if type(input_num) is not int:
            self.error('must_use_digit')
        elif input_num > len(self.todo_list):
            self.error('out_of_list_range')
        elif input_num < 1:
            self.error('out_of_list_range')
        else:
            return input_num

    def input_check_for_complist(self, input_num):
        if type(input_num) is not int:
            self.error('must_use_digit')
        elif input_num > len(self.complete_list):
            self.error('out_of_list_range')
        elif input_num < 1:
            self.error('out_of_list_range')
        else:
            return input_num

    def is_todo_list_empty(self):
        if len(self.todo_list) == 0:
            self.error('no_task_to_execute')
        else:
            pass

    def is_complete_list_empty(self):
        if len(self.complete_list) == 0:
            self.error('no_task_to_execute')
        else:
            pass                  
              
    def task_input(self, addtask):
        if addtask in self.todo_list:
            self.error('task_overlap')
        else:
            self.todo_list.append(addtask)
            self.briefing()
        
    def completed_task_input(self, addtask):
        if addtask in self.complete_list:
            self.error('task_overlap')
        else:
            self.complete_list.append(addtask)
            self.briefing()

    def task_delete(self, input_num):
        self.todo_list.remove(self.todo_list[int(input_num) - 1])
        self.briefing()
        
    def completed_task_delete(self, input_num):
        self.complete_list.remove(self.complete_list[int(input_num) - 1])
        self.briefing()

    def task_edit(self, input_num, newdata):
        self.todo_list[int(input_num) - 1] = newdata
        self.briefing()
    
    def completed_task_edit(self, input_num, newdata):
        self.complete_list[int(input_num) - 1] = newdata
        self.briefing()
    
    def task_complete(self, input_num):
        self.complete_list.append(self.todo_list[int(input_num) - 1])
        self.todo_list.remove(self.todo_list[int(input_num) - 1])
        self.briefing()
    
    def task_incomplete(self, input_num):
        self.todo_list.append(self.complete_list[int(input_num) - 1])
        self.complete_list.remove(self.complete_list[int(input_num) - 1])
        self.briefing()
    
    def briefing(self):
        n = 1
        if len(self.todo_list) == 0:
            print('\nno task to do\n')
        else:
            print('\nTasks to do')
            for i in self.todo_list:
                print(f'{n}. {i}')
                n += 1
        n = 1
        if len(self.complete_list) == 0:
            print('no task done')
        else:  
            print('\nCompleted Task')
            for i in self.complete_list:
                print(f'{n}. {i}')
                n += 1
        print("")
        self.task_loop()
        
    def task_loop(self):
        print("Press 'A' to add task, 'C' to complete task, 'D' to delete task, 'E' to edit task, 'Q' to quit program.")
        print("If you want to make changes in completed list, press 'M'.")
        print("If you want to see task list again, press 'R'.\n")
        answer = input('press here : ')
        print("")
        if answer in ['a', 'A', 'ㅁ']:
            addtask = input("Input next task : ")
            self.task_input(addtask)
        elif answer in ['d', 'D', 'ㅇ']:
            self.is_todo_list_empty()
            input_num = input("Input task number : ")
            self.input_check_for_todolist(input_num)
            self.task_delete(input_num)
        elif answer in ['c', 'C', 'ㅊ']:
            self.is_todo_list_empty()
            input_num = input("Input task number : ")
            self.input_check_for_todolist(input_num)
            self.task_complete(input_num)
        elif answer in ['e', 'E', 'ㄷ', 'ㄸ']:
            self.is_todo_list_empty()
            input_num = input("Input task number : ")
            self.input_check_for_todolist(input_num)
            editedtask = input("Input new task : ")
            self.task_edit(input_num, editedtask)
        elif answer in ['q', 'Q', 'ㅂ']:
            self.finish_list()
        elif answer in ['m', 'M', 'ㅡ']:
            self.is_complete_list_empty()
            self.comp_list_change()
        elif answer in ['r', 'R', 'ㄱ', 'ㄲ']:
            self.briefing()
        else:
            self.error('wrong_task_input')
    
    def comp_list_change(self):
        print("Press 'A' to add task, 'C' to make task incomplete, 'D' to delete task, 'E' to edit task.")
        print("If you want to make changes in task list, press 'M'.\n")
        answer = input('press here : ')
        print("")
        if answer in ['a', 'A', 'ㅁ']:
            addtask = input("Input next task : ")
            self.completed_task_input(addtask)
        elif answer in ['d', 'D', 'ㅇ']:
            input_num = input("Input task number : ")
            self.input_check_for_complist(input_num)
            self.completed_task_delete(input_num)
        elif answer in ['c', 'C', 'ㅊ']:
            input_num = input("Input task number : ")
            self.input_check_for_complist(input_num)
            self.task_incomplete(input_num)
        elif answer in ['e', 'E', 'ㄷ', 'ㄸ']:
            input_num = input("Input task number : ")
            self.input_check_for_complist(input_num)
            editedtask = input("Input new task : ")
            self.completed_task_edit(input_num, editedtask)
        elif answer in ['m', 'M', 'ㅡ']:
            self.task_loop()
        else:
            self.error('wrong_task_input')  
          
    def finish_list(self):
        print('Completed Tasks')
        n = 1
        for i in self.complete_list:
            print(f'{n}. {i}')
            n += 1
        n = 1
        print('Incomplete Tasks')
        for i in self.todo_list:
            print(f'{n}. {i}')
            n += 1
        whether = input("Press y to save files : ")
        if whether in ['y', 'Y', 'ㅛ']:
            output_json = {'todo_list' : self.todo_list, 'complete_list' : self.complete_list}
            file_name = input("Save as : ")
            file_path = os.path.expanduser(f'~/{file_name}.json')
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(output_json, file)
        else:
            print("bye")
        quit()

    def error(self, error_code):
        if error_code == 'must_use_digit':
            print("ERROR : You must input numbers\n")
            self.task_loop()
        elif error_code == 'out_of_list_range':
            print(f"ERROR : Your number is out of task list range. You must input right number.")
            print(f"You have {len(self.todo_list)} task(s) in list.\n")
            self.task_loop()
        elif error_code == 'wrong_task_input':
            print("ERROR : You must input a, c, d, e, m, q or r\n")
            self.task_loop()
        elif error_code == 'nothing_to_edit_in_complete_list':
            print("ERROR : Completed task list is empty. You must complete task first\n")
            self.task_loop()
        elif error_code == 'task_overlap':
            print("ERROR : Tasks can't be overlapped.")
            self.task_loop()
        elif error_code == 'no_task_to_execute':
            print("ERROR : There's no task to execute.\n")
            self.task_loop()  

def main():
    me = Todolist()
    me.json_file_quest()
    me.briefing()

if __name__ == "__main__":
    main()

    