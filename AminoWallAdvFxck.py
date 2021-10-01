import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_SEA_GREEN_2 + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminowalladvfxck", font="drpepper", width=78))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
message = input("Message >> ")
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
print("""[1] Send Wall Advertise to Online Users
[2] Send Wall Advertise to Recent Users""")
select = input("Select >> ")

if select == "1":
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        while True:
            try:
                for i in range(100, 1000, 5000):
                    online_users = client.get_online_members(
                        ndc_Id=ndc_Id, start=i, size=100)
                    for user_id, nickname in zip(
                            online_users.user_Id, online_users.nickname):
                        print(f"Sended Advertise, {nickname} > {user_id}")
                        _ = [
                            executor.submit(
                                client.submit_comment,
                                ndc_Id,
                                message,
                                user_id)]
            except Exception as e:
                print(e)

elif select == "2":
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        while True:
            try:
                for i in range(100, 1000, 5000):
                    recent_users = client.get_recent_members(
                        ndc_Id=ndc_Id, start=i, size=100)
                    for user_id, nickname in zip(
                            recent_users.user_Id, recent_users.nickname):
                        print(f"Sended Advertise, {nickname} > {user_id}")
                        _ = [
                            executor.submit(
                                client.submit_comment,
                                ndc_Id,
                                message,
                                user_id)]
            except Exception as e:
                print(e)
