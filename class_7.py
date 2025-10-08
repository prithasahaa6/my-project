# myfamily={
#     "child1":{"name":"Emil","year":2004},
#     "child2":{"name":"Tobias","year":2007}, 
#     "child3":{"name":"Linus","year":2011}
# }   
# x=myfamily["child2"]["name"]
# print(x)
# x=myfamily["child3"]["year"]
# print(x)
# print(myfamily["child1"]["name"])

students={
    "s001":{
        "name":"anu",
        "age":21,
        "course":{"math":{"grade":"A","credit":3},
                "physics":{"grade":"B","credit":4},}}
}
print(students["s001"]["course"]["math"]["grade"])
print(students["s001"]["course"]["physics"]["credit"])