my_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# def draw_stars(list):
#     for num in my_list:
#         print "*" * num 
# draw_stars(my_list) 

def draw_stars(list):
    for x in list:
        if isinstance(x,int):
            print "*" * x
        elif isinstance(x,str):
            print x[0].lower() * 4
draw_stars(my_list)
