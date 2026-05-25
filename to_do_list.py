def TO_Do_List():
    to_do_list = []
    while True:
        task = input("Enter a tas k (of type 'done to finish') :")
        if task.lower() == 'done':
            break
        to_do_list.append(task)
    print("\nYour To-Do List:")
    for idx, task in enumerate(to_do_list, start=1):
        print(f"{idx}. {task}")
if __name__ == "__main__":
    TO_Do_List()
    