import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.DARK_SEA_GREEN_2 + style.BOLD}
Script by zeviel
Github : https://github.com/zeviel"""
)
print(figlet_format("13MINXW9LLADVFXKK", font="drpepper", width=78))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
print(
"""
[1] Send Wall Advertise to Online Users
[2] Send Wall Advertise to Recent Users
"""
)
select = int(input("-- Select::: "))

if select == 1:
    with ThreadPoolExecutor(max_workers=100) as executor:
        while True:
            try:
                for i in range(100, 2500, 15000):
                    online_users = sub_client.get_online_users(
                        start=i, size=100)
                    for user_id, nickname in zip(
                            online_users.profile.userId, online_users.profile.nickname):
                        print(f"Sent advertise to::: {nickname}|{user_id}")
                        _ = [
                            executor.submit(
                                sub_client.comment,
                                message,
                                user_id)]
            except Exception as e:
                print(e)

elif select == 2:
    with ThreadPoolExecutor(max_workers=100) as executor:
        while True:
            try:
                for i in range(100, 2500, 15000):
                    recent_users = sub_client.get_all_users(
                        type="recent", start=i, size=100)
                    for user_id, nickname in zip(
                            recent_users.profile.userId, recent_users.profile.nickname):
                        print(f"Sent advertise to::: {nickname}|{user_id}")
                        _ = [
                            executor.submit(
                                sub_client.comment,
                                message,
                                user_id)]
            except Exception as e:
                print(e)
