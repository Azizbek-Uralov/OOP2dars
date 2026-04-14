# class student:
#     def __init__(self, name:str, student_id:str):
#         self.name = name
#         self.id = student_id
#         self.lst = []
#     def add_gred(self, grade:int):
#         if 101>grade>0:
#             self.lst.append(grade)
#         # print(self.lst)   
#     def calculate_average(self):
#         a = float(sum(self.lst)//len(self.lst))
#         self.urtachasi = a
#     def get_status(self):
#         if 100>=self.urtachasi>=90:
#             return "90-100: A'lo"
#         elif 89>self.urtachasi>=80:
#             return "80-89: Yaxshi"
#         elif 79>=self.urtachasi>70:
#             return "70-79: Qoniqarli"
#         else:
#             return "70>: qoniqarsiz"
# t1 = student("Islom", "40504a")
# a = int(input("Nechta bahosini kiritasiz: "))
# for i in range(a):
#     t1.add_gred(int(input("Baho: ")))
# t1.calculate_average()
# print(t1.get_status())   

# 2-masala


# class employee:
#     def __init__(self, name:str, employee_id:str, hourly_rate:float):
#         self.name = name
#         self.id = employee_id
#         self.soatlari = []
#         self.price = hourly_rate
#     def log_hourse(self, hours:int):
#         if 24>=hours>0:
#             self.soatlari.append(hours)
#             return True
#         else:
#             return False
#     def employee_total_hours(self):
#         self.a = sum(self.soatlari)
#         return self.a
#     def calculate_salary(self):
#         return self.a*self.price
#     def reset_hours(self):
#         self.soatlari = []
#         self.price = 0.0
        
# xodim = employee("vali", "X005", 20.0)
# print(xodim.log_hourse(12))
# print(xodim.log_hourse(18))
# print(xodim.log_hourse(15))
# print(xodim.employee_total_hours())
# print(xodim.calculate_salary())
# xodim.reset_hours()
# print(xodim.employee_total_hours())
# print(xodim.calculate_salary)

# 3-masala

# class Playlist_Manager:
#     def __init__(self,owner:str):
#         self.egasi = owner
#         self.royxat = []
#     def add_track(self, track:str, title:str):
#         a = list()
#         a.append(track)
#         a.append(title)
#         self.royxat.append(tuple(a))
#     def remove_last(self):
#         return self.royxat.pop(-1)
#     def total_track(self):
#         return len(self.royxat)
#     def unique_tracks(self):
#         lst = []
#         for i in self.royxat:
#             if i not in lst:
#                 lst.append(i)
#         return lst
#     def search_by_title(self, title:str):
#         lst = []
#         for i in self.royxat:
#             if title in i:
#                 lst.append(i)
#         return lst
#     def filter_by_artist(self, artist:str):
#         lst = []
#         for i in self.royxat:
#             if i[-1]==artist:
#                 lst.append(i)
#         return lst        
# u1 = Playlist_Manager(input("Owner: "))
# print(u1.total_track(), end = "\n\n")
# son = int(input("Nechta track kiritasiz: "))
# for i in range(son):
#     u1.add_track(input("Track: "), input("Title: "))
# print(u1.unique_tracks(), end = "\n\n")
# print(u1.remove_last(), end = "\n\n")
# print(u1.total_track(), end = "\n\n")
# print(u1.search_by_title("Shahzoda"))
# print(u1.filter_by_artist("Lola"))