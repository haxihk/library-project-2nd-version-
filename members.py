from datas import*

def add_member(file_name):
    quantity = int(input("how many members do you want to add? "))
    count= 1
    while count<=quantity:
        member_name = input("Enter the name of the member: ")
        member_id = input("Enter the ID of the member: ")
        subscription_time = input("Enter the subscription time (YYYY-MM-DD): ")

        member = {
            "name": member_name,
            "id": member_id,
            "subscription_time": subscription_time
        }
        count+=1
    members = load_data(file_name)
    members.append(member)
    save_data(file_name, members)


def is_not_expired(subscription_time, current_date):
    subscription_year, subscription_month, subscription_day = map(int, subscription_time.split('-'))
    current_year, current_month, current_day = map(int, current_date.split('-'))
    if current_year > subscription_year:
        return False
    elif current_year == subscription_year:
        if current_month > subscription_month:
            return False
        elif current_month == subscription_month and current_day > subscription_day:
            return False
    return True


def remove_expired_members(file_name):
    members = load_data(file_name)
    current_date = input("Enter the current date (YYYY-MM-DD): ")
    valid_members = [member for member in members if is_not_expired(member['subscription_time'], current_date)]
    save_data(file_name, valid_members)


def renew_subscription(file_name):
    members = load_data(file_name)
    member_id = input("Enter the ID of the member to renew the subscription: ")
    new_subscription_time = input("Enter the new subscription time (YYYY-MM-DD): ")
    for member in members:
        if member['id'] == member_id:
            member['subscription_time'] = new_subscription_time
            save_data(file_name, members)
            print(f"Subscription renewed for member with ID {member_id}.")
            break
    else:
        print(f"Member with ID {member_id} not found.")
