import os

def display_menu():
    print("\n===== 待辦事項管理系統 =====")
    print("1. 新增任務")
    print("2. 查看任務")
    print("3. 刪除任務")
    print("4. 離開程式")
    print("=======================")

def add_task(task_list):
    task = input("請輸入新任務: ")
    task_list.append(task)
    print(f"已新增任務: {task}")

def view_tasks(task_list):
    if not task_list:
        print("目前沒有任何任務。")
    else:
        print("\n目前的任務:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_number = int(input("請輸入要刪除的任務編號: "))
            if 1 <= task_number <= len(task_list):
                removed_task = task_list.pop(task_number - 1)
                print(f"已刪除任務: {removed_task}")
            else:
                print("無效的任務編號！")
        except ValueError:
            print("請輸入有效的數字！")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("請選擇功能 (1-4): ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            print("感謝使用，再見！")
            break
        else:
            print("無效的選項，請重新輸入！")

if __name__ == "__main__":
    main()
